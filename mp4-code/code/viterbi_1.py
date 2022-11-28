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
    
    tagPair = {START_TAG:{}}
    twPair = {}
    for key in tagMat.keys():
        tagPair.setdefault(key,{})
        twPair.setdefault(key,{})
    
    wordList = [UNKNOWN]
    for sentence in train:
        for i in range(1,len(sentence)-1):
            
            preTag = sentence[i-1][1]
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
    
    alpha = 1e-10 # smoothing factor
    
    initial = {}
    logIni = {}
    for key in tagMat.keys():
        if key in tagPair[START_TAG]:
            sub_ini = tagPair[START_TAG][key]
        else:
            sub_ini = 0
        p = (sub_ini+alpha)/(tot_ini+keyNum*alpha)
        initial.setdefault(key,p)
        logIni.setdefault(key,math.log(p))
    
    transition = {}
    logTrans = {}
    for key_1 in tagMat.keys():
        tot_trans = sum(tagPair[key_1].values())
        for key_2 in tagMat.keys():
            if key_2 in tagPair[key_1]:
                sub_trans = tagPair[key_1][key_2]
            else:
                sub_trans = 0
            pTrans = (sub_trans+alpha)/(tot_trans+keyNum*alpha)
            transition.setdefault(key_1,{}).update({key_2:pTrans})
            logTrans.setdefault(key_1,{}).update({key_2:math.log(pTrans)})
            
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
            pEmiss = (sub_emiss[num_emiss]+alpha)/(tot_emiss+keyNum*alpha)
            emission.setdefault(key,{}).update({w:pEmiss})
            logEmiss.setdefault(key,{}).update({w:math.log(pEmiss)})

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
        T = len(item)-2
        Viterbi = np.zeros((N,T))
        Backpointer = np.zeros((N,T))

        for n in range(N):
            key = keyList[n]
            word = item[1]
            if word not in wordList:
                word = UNKNOWN
            Viterbi[n][0] = logIni[key]+logEmiss[key][word]
            Backpointer[n][0] = 0
            
        for t in range(1,T):
            for n in range(N):
                key = keyList[n]
                word = item[t+1]
                if word not in wordList:
                    word = UNKNOWN
                viterbi = 0
                backpointer = 0
                for nPast in range(N):
                    keyPast = keyList[nPast]
                    ProSum = Viterbi[nPast][t-1]+logTrans[keyPast][key]+logEmiss[key][word]
                    if ProSum > viterbi:
                        viterbi = ProSum
                        backpointer = nPast
                Viterbi[n][t] = viterbi
                Backpointer[n][t] = backpointer
                
        # BestPro = [np.max(Viterbi[:,-1])]
        TagIndex = np.argmax(Viterbi[:,-1])
        retSent = [(item[-2],keyList[TagIndex])]
        Pointer = Backpointer[TagIndex,-1]
        for t in range(T-2,-1,-1):
            TagIndex = int(Pointer)
            outTuple = (item[t+1],keyList[TagIndex])
            retSent.append(outTuple)
            Pointer = Backpointer[TagIndex,t]
        
        retSent.reverse()
        retMat.append(retSent)
        
    # Part5: Return the best path through the trellis
    
    return retMat