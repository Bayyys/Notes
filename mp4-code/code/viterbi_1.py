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

"""
Part 2: This is the simplest version of viterbi that doesn't do anything special for unseen words
but it should do better than the baseline at words with multiple tags (because now you're using context
to predict the tag).
"""
import numpy as np
import math

def viterbi_1(train, test):
    '''
    input:  training data (list of sentences, with tags on the words)
            test data (list of sentences, no tags on the words)
    output: list of sentences with tags on the words
            E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
    '''
    predicts = []

    tw_pair = {}  # tag-word pair
    tag_set = {}  # tag matrix

    tag_index = {}   # tag index
    tag_count = 0  # index count

    for sentence in train:
        for pair in sentence:
            word, tag = pair    # word, tag

            if tag in tag_set:
                tag_set[tag] += 1
            else:
                tag_set[tag] = 1
                tag_index[tag] = tag_count
                tag_count += 1

            if word not in tw_pair:
                tw_pair[word] = {}

            if tag in tw_pair[word]:
                tw_pair[word][tag] += 1
            else:
                tw_pair[word][tag] = 1

    emission_smooth_param = 0.001   # emission smooth parameter
    transition_smooth_param = 0.001  # transition smooth parameter

    # tag count per word/ total tag count - emission probability
    for key in tw_pair.keys():
        for tag in tw_pair[key].keys():
            tw_pair[key][tag] = (emission_smooth_param + tw_pair[key][tag]) / (
                    tag_set[tag] + emission_smooth_param * len(tag_set))

    initial_tag_probabilities = np.zeros(tag_count)
    transition_matrix = np.zeros(shape=(tag_count, tag_count))

    for sentence in train:
        first = True
        for i in range(len(sentence[:-1])):
            word, tag = sentence[i]

            curr_tag_idx = tag_index[tag]

            if first:
                initial_tag_probabilities[curr_tag_idx] += 1
                first = False

            next_tag = sentence[i + 1][1]
            transition_matrix[curr_tag_idx][tag_index[next_tag]] += 1

    # not needed
    init_smooth_param = 0.5

    # count tag starts sentence / total num sentences
    for i in range(len(initial_tag_probabilities)):
        initial_tag_probabilities[i] = (initial_tag_probabilities[i]) / (len(train))

    # LaPlace smoothing: (1+transition occurances)/(tag occurences + num tags)
    for tag, count in tag_set.items():
        prev_idx = tag_index[tag]
        for i in range(len(transition_matrix)):
            transition_matrix[prev_idx][i] = (transition_matrix[prev_idx][i] + transition_smooth_param) / (
                    count + transition_smooth_param * len(tag_set))

    tag_names = []
    for tag in tag_index.keys():
        tag_names.append(tag)

    for sentence in test:
        trellis = []

        for i in range(len(sentence)):
            temp = []
            curr_word = sentence[i]

            if i == 0:  # first word in sentence
                if curr_word not in tw_pair:
                    for tag in tag_index.keys():
                        probability = emission_smooth_param / (
                                tag_set[tag] + emission_smooth_param * len(tag_set))
                        tuple = (initial_tag_probabilities[tag_index[tag]] * probability, tag)
                        temp.append(tuple)

                else:
                    for tag in tag_index.keys():

                        if tag not in tw_pair[curr_word]:
                            probability = emission_smooth_param / (
                                    tag_set[tag] + emission_smooth_param * len(tag_set))
                            tuple = (initial_tag_probabilities[tag_index[tag]] * probability, tag)
                            temp.append(tuple)
                        else:
                            probability = tw_pair[curr_word][tag]
                            tuple = (initial_tag_probabilities[tag_index[tag]] * probability, tag)
                            temp.append(tuple)
            else:
                probability = 0
                for tag in tag_index.keys():
                    prev_idx = tag_index[tag]

                    for j in range(len(tag_index)):
                        probability = -99999
                        if curr_word not in tw_pair:
                            probability = emission_smooth_param / (
                                    tag_set[tag] + emission_smooth_param * len(tag_set))
                        else:
                            if tag not in tw_pair[curr_word]:
                                probability = emission_smooth_param / (
                                        tag_set[tag] + emission_smooth_param * len(tag_set))
                            else:
                                probability = tw_pair[curr_word][tag]

                        prev_prob = trellis[i - 1][prev_idx]

                        log2 = np.log(transition_matrix[prev_idx][j])
                        log3 = np.log(probability)
                        probability = prev_prob[0] + log2 + log3

                        tuple = (probability, tag_names[prev_idx])
                        if prev_idx == 0:
                            temp.append(tuple)
                        elif (temp[j][0] < probability):
                            temp[j] = tuple
            trellis.append(temp)

        if len(trellis) == 0:
            predicts.append([])
            continue

        tuple_list = trellis[len(trellis) - 1]
        predicted_sentence = []

        max_tag_idx = tuple_list.index((max(tuple_list, key=lambda pair: pair[0])))
        predicted_sentence.append(tag_names[max_tag_idx])

        prev_tag = max(tuple_list, key=lambda pair: pair[0])

        for i in range(len(trellis) - 1, 0, -1):
            prev_tag = trellis[i - 1][tag_index[prev_tag[1]]]
            predicted_sentence.insert(0, prev_tag[1])

        max_start_tag = max(trellis[0], key=lambda pair: pair[0])[1]
        predicted_sentence[0] = max_start_tag

        predicts.append(list(zip(sentence, predicted_sentence)))

    return predicts