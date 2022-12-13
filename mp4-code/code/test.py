# mp4.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created Fall 2018: Margaret Fleck, Renxuan Wang, Tiantian Fang, Edward Huang (adapted from a U. Penn assignment)
# Modified Spring 2020: Jialu Li, Guannan Guo, and Kiran Ramnath
# Modified Fall 2020: Amnon Attali, Jatin Arora
# Modified Spring 2021 by Kiran Ramnath (kiranr2@illinois.edu)

import argparse
import sys

from baseline import baseline
from viterbi_1 import viterbi_1
from viterbi_2 import viterbi_2
from viterbi_ec import viterbi_ec

import utils

import numpy as np
import math
Inf = float('inf')

"""
This file contains the main application that is run for this MP.
"""

def viterbi_1(train, test):

    START_TAG = "START"
    END_TAG = "END"
    UNKNOWN = "UNKNOWN"

    # Part1: Count occurrences of tags, tag pairs, tag/word pairs

    tot_ini = 0

    tagMat = {}
    for sentence in train:
        tot_ini += 1
        for i in range(len(sentence)):
            word = sentence[i][0]
            tag = sentence[i][1]
            if tag not in tagMat:
                tagMat[tag] = 1
            else:
                tagMat[tag] += 1
    del tagMat[START_TAG]
    del tagMat[END_TAG]

    tagPair = {START_TAG: {}}
    twPair = {}
    for key in tagMat.keys():
        tagPair.setdefault(key, {})
        twPair.setdefault(key, {})

    wordList = [UNKNOWN]
    for sentence in train:
        for i in range(1, len(sentence) - 1):

            preTag = sentence[i - 1][1]
            word = sentence[i][0]
            tag = sentence[i][1]

            if tag not in tagPair[preTag]:
                tagPair[preTag][tag] = 1
            else:
                tagPair[preTag][tag] += 1

            if word not in twPair[tag]:
                twPair[tag][word] = 1
            else:
                twPair[tag][word] += 1

            if word not in wordList:
                wordList.append(word)

    # Part2: Compute smoothed probabilities

    keyList = list(tagMat.keys())
    keyNum = len(keyList)

    alpha = 1e-10  # smoothing factor

    initial = {}
    logIni = {}
    for key in tagMat.keys():
        if key in tagPair[START_TAG]:
            sub_ini = tagPair[START_TAG][key]
        else:
            sub_ini = 0
        p = (sub_ini + alpha) / (tot_ini + keyNum * alpha)
        initial.setdefault(key, p)
        logIni.setdefault(key, math.log(p))

    transition = {}
    logTrans = {}
    for key_1 in tagMat.keys():
        tot_trans = sum(tagPair[key_1].values())
        for key_2 in tagMat.keys():
            if key_2 in tagPair[key_1]:
                sub_trans = tagPair[key_1][key_2]
            else:
                sub_trans = 0
            pTrans = (sub_trans + alpha) / (tot_trans + keyNum * alpha)
            transition.setdefault(key_1, {}).update({key_2: pTrans})
            logTrans.setdefault(key_1, {}).update({key_2: math.log(pTrans)})

    emission = {}
    logEmiss = {}
    for w in wordList:
        tot_emiss = 0
        sub_emiss = [0 for i in range(keyNum)]
        num_emiss = -1
        for key in tagMat.keys():
            num_emiss += 1
            if w in twPair[key].keys():
                sub_emiss[num_emiss] = twPair[key][w]
                tot_emiss += twPair[key][w]
        num_emiss = -1
        for key in tagMat.keys():
            num_emiss += 1
            pEmiss = (sub_emiss[num_emiss] + alpha) / (tot_emiss + keyNum * alpha)
            emission.setdefault(key, {}).update({w: pEmiss})
            logEmiss.setdefault(key, {}).update({w: math.log(pEmiss)})

    # # Part3: Take the log of each probability

    # logIni = {}
    # for key in initial.keys():
    #     logIni[key] = np.log(initial[key])

    # logTrans = {}
    # for key_1 in transition.keys():
    #     for key_2 in transition.keys():
    #         logTrans[key_1][key_2] = np.log(transition[key_1][key_2])
    #         logTrans.setdefault(key_1,{}).update({key_2:pTrans})

    # logEmiss = {}
    # for key in emission.keys():
    #     for w in emission[key].keys():
    #         logEmiss[key][w] = np.log(emission[key][w])

    # Part4: Construct the trellis. Notice that for each tag/time pair,
    # you must store not only the probability of the best path but also
    # a pointer to the previous tag/time pair in that path.

    retMat = []
    for item in test:
        N = keyNum
        T = len(item) - 2
        Viterbi = np.zeros((N, T))
        Backpointer = np.zeros((N, T))

        for n in range(N):
            key = keyList[n]
            word = item[1]
            if word not in wordList:
                word = UNKNOWN
            Viterbi[n][0] = logIni[key] + logEmiss[key][word]
            Backpointer[n][0] = 0

        for t in range(1, T):
            for n in range(N):
                key = keyList[n]
                word = item[t + 1]
                if word not in wordList:
                    word = UNKNOWN
                viterbi = 0
                backpointer = 0
                for nPast in range(N):
                    keyPast = keyList[nPast]
                    ProSum = Viterbi[nPast][t - 1] + logTrans[keyPast][key] + logEmiss[key][word]
                    if ProSum > viterbi:
                        viterbi = ProSum
                        backpointer = nPast
                Viterbi[n][t] = viterbi
                Backpointer[n][t] = backpointer

        # BestPro = [np.max(Viterbi[:,-1])]
        TagIndex = np.argmax(Viterbi[:, -1])
        retSent = [(item[-2], keyList[TagIndex])]
        Pointer = Backpointer[TagIndex, -1]
        for t in range(T - 2, -1, -1):
            TagIndex = int(Pointer)
            outTuple = (item[t + 1], keyList[TagIndex])
            retSent.append(outTuple)
            Pointer = Backpointer[TagIndex, t]

        retSent.append((START_TAG, START_TAG))
        retSent.reverse()
        retSent.append((END_TAG, END_TAG))
        retMat.append(retSent)

    # Part5: Return the best path through the trellis

    return retMat

def baseline(train, test):
    '''
    input:  training data (list of sentences, with tags on the words)
            test data (list of sentences, no tags on the words)
    output: list of sentences, each sentence is a list of (word,tag) pairs.
            E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
    '''
    START_TAG = "START"
    END_TAG = "END"
    UNKNOWN = "UNKNOWN"

    tagMat = {}  # tagMat is a dictionary that stores the number of times each tag appears
    twPair = {}  # twPair is a dictionary that stores the number of times each tag-word pair appears
    wordList = [UNKNOWN]    # wordList is a list that stores all the words in the training set

    for sentence in train:
        # sentence is a list of (word, tag) pairs
        for i in range(len(sentence)):
            # sentence[i] is a tuple (word, tag)
            word = sentence[i][0]
            tag = sentence[i][1]

            if tag not in tagMat:   # if the tag is not in the dictionary, add it
                tagMat[tag] = 1
            else:   # if the tag is in the dictionary, increment its count
                tagMat[tag] += 1

            if word not in wordList:    # if the word is not in the list, add it
                wordList.append(word)

            if tag not in twPair:   # if the tag is not in the dictionary, add it
                twPair[tag] = {word: 1}
            else:
                if word not in twPair[tag]: # if the word is not in the dictionary, add it
                    twPair[tag][word] = 1
                else:   # if the word is in the dictionary, increment its count
                    twPair[tag][word] += 1
    del tagMat[START_TAG]   # remove the START tag from the dictionary
    del tagMat[END_TAG]  # remove the END tag from the dictionary
    del twPair[START_TAG]   # remove the START tag from the dictionary
    del twPair[END_TAG]  # remove the END tag from the dictionary
    for tag in twPair:
        # if tag in {START_TAG, END_TAG}:
        #     continue
        for word in twPair[tag]:
            twPair[tag][word] = math.log(twPair[tag][word] / tagMat[tag])  # calculate the log probability of the tag-word pair
    for tag in twPair:
        # if tag in {START_TAG, END_TAG}:
        #     continue
        twPair[tag][UNKNOWN] = math.log(1 / tagMat[tag])  # calculate the log probability of the tag-UNKNOWN pair
    prediction = []  # prediction is a list of sentences, each sentence is a list of (word, tag) pairs
    for sentence in test:
        temp = []
        for i in range(len(sentence)):
            word = sentence[i]
            if word in {START_TAG, END_TAG}:
                temp.append((word, word))
                continue
            if word not in wordList:
                word = UNKNOWN  # if the word is not in the list, replace it with UNKNOWN
            maxTag = ""
            maxProb = -Inf
            for tag in twPair:
                if word not in twPair[tag]:
                    continue
                if twPair[tag][word] > maxProb:
                    maxProb = twPair[tag][word]
                    maxTag = tag
            if word == UNKNOWN:
                temp.append((sentence[i], maxTag))
            else:
                temp.append((word, maxTag))  # append the (word, tag) pair to the list
        prediction.append(temp)  # append the list to the list of sentences

    return prediction

def main(args):
    print("Loading dataset...")
    train_set = utils.load_dataset(args.training_file)
    test_set = utils.load_dataset(args.test_file)
    print("Loaded dataset")
    print("train_set: ", train_set)
    print()

    algorithms = {"baseline": baseline, "viterbi_1": viterbi_1, "viterbi_2": viterbi_2, "viterbi_ec": viterbi_ec}
    algorithm = algorithms[args.algorithm]

    print("Running {}...".format(args.algorithm))
    # testtag_predictions = algorithm(train_set, utils.strip_tags(test_set))
    # baseline_acc, correct_wordtagcounter, wrong_wordtagcounter = utils.evaluate_accuracies(testtag_predictions,
    #                                                                                        test_set)
    # multitags_acc, unseen_acc, = utils.specialword_accuracies(train_set, testtag_predictions, test_set)
    #
    # print("Accuracy: {:.2f}%".format(baseline_acc * 100))
    # print("\tMultitags Accuracy: {:.2f}%".format(multitags_acc * 100))
    # print("\tUnseen words Accuracy: {:.2f}%".format(unseen_acc * 100))
    # print("\tTop K Wrong Word-Tag Predictions: {}".format(utils.topk_wordtagcounter(wrong_wordtagcounter, k=4)))
    # print("\tTop K Correct Word-Tag Predictions: {}".format(utils.topk_wordtagcounter(correct_wordtagcounter, k=4)))
    #
    # print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CS440 MP4 HMM')
    parser.add_argument('--train', dest='training_file', type=str, default="data/brown-training.txt",
                        help='the file of the training data')
    parser.add_argument('--test', dest='test_file', type=str, default="data/brown-dev.txt",
                        help='the file of the testing data')
    parser.add_argument('--algorithm', dest='algorithm', type=str, default="baseline",
                        help='which algorithm to run: baseline, viterbi_1, viterbi_2, viterbi_ec')
    args = parser.parse_args()
    if args.training_file == None or args.test_file == None:
        sys.exit('You must specify training file and testing file!')

    main(args)
