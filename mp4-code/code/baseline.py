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
# Modified Spring 2021 by Kiran Ramnath
"""
Part 1: Simple baseline that only uses word statistics to predict tags
"""
import math
import numpy as np

Inf = float('inf')

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

    predicts = []
    tw_pair = {}
    tag_set = {}

    for sentence in train:
        # sentence is a list of (word, tag) pairs
        for pair in sentence:
            # pair is a tuple (word, tag)
            word, tag = pair    # unpack the tuple
            if tag in tag_set:
                tag_set[tag] += 1    # if tag is already in tag_set, increment the count
            else:
                tag_set[tag] = 1    # if tag is not in tag_set, add it to tag_set with count 1

            if word not in tw_pair:
                tw_pair[word] = {}   # if word is not in tw_pair, add it to tw_pair with an empty dictionary

            if tag in tw_pair[word]:
                tw_pair[word][tag] += 1  # if tag is already in tw_pair[word], increment the count
            else:
                tw_pair[word][tag] = 1   # if tag is not in tw_pair[word], add it to tw_pair[word] with count 1

    max_tag = max(tag_set.keys(), key=(lambda key: tag_set[key]))   # get the tag with the highest count

    for sentence in test:
        sentence_prediction = []    # list of (word, tag) pairs
        for word in sentence:
            if word in tw_pair:
                tag_map = tw_pair[word]  # get the dictionary of tags and their counts for the word
                best_tag = max(tag_map.keys(), key=(lambda key: tag_map[key]))
                sentence_prediction.append((word, best_tag))
            else:
                sentence_prediction.append((word, max_tag))
        predicts.append(sentence_prediction)
    return predicts