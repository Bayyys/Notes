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
Part 3: Here you should improve viterbi to use better laplace smoothing for unseen words
This should do better than baseline and your first implementation of viterbi, especially on unseen words
"""


def viterbi_2(train, test):
    """
    input:  training data (list of sentences, with tags on the words)
            test data (list of sentences, no tags on the words)
    output: list of sentences with tags on the words
            E.g., [[(word1, tag1), (word2, tag2)], [(word3, tag3), (word4, tag4)]]
    """

    tag_set, tag_count, num_of_tags, tw_pair = get_tw_pair(train)

    hapax = find_hapax(train, tag_set)

    # How often does each tag occur at the start of a sentence?)
    initial = initial_p(train)

    # How often does tag tb follow tag ta?
    transition = transition_p(train, tag_count)

    # how often does tag t yield word w?
    emission = hapax_emission_p(train, tag_count, tag_set, hapax)

    predicts = []

    for sentence in test:
        num_of_words = len(sentence)
        trellis = populate_trellis(sentence, tag_set, emission)

        for i in range(len(sentence)):
            for j, cur_tag in enumerate(tag_set):
                probability = {}
                maxx = -1
                for k, prev_tag in enumerate(tag_set):
                    t_pair = (cur_tag, prev_tag)

                    if (i == 0):
                        tra = get_initial(initial, cur_tag)
                    else:
                        tra = get_probs(transition, t_pair)

                    if (i == 0):
                        prev_emi = 1
                    else:
                        prev_emi = trellis[k][i - 1].probability

                    cur_emi = trellis[j][i].probability
                    probability[prev_tag] = prev_emi * tra * cur_emi
                    if (probability[prev_tag] > maxx):
                        maxx = probability[prev_tag]
                        if (i != 0):
                            prev_node = trellis[k][i - 1]

                the_pre_tag = max(probability, key=probability.get)
                trellis[j][i].probability = probability[the_pre_tag]
                if (i == 0):
                    trellis[j][i].prev = "start"
                else:
                    trellis[j][i].prev = prev_node

        maxx = -1

        for j in range(num_of_tags):
            if (trellis[j][num_of_words - 1].probability > maxx):
                last_node = trellis[j][num_of_words - 1]

                maxx = trellis[j][num_of_words - 1].probability

        output = []
        pair = (last_node.word, last_node.tag)
        output.append(pair)
        while (last_node.prev != "start"):
            last_node = last_node.prev
            pair = (last_node.word, last_node.tag)
            output.append(pair)

        output.reverse()
        predicts.append(output)

    return predicts


class node:
    def __init__(self, tag, prev, probability, word):
        self.tag = tag
        self.prev = prev
        self.probability = probability
        self.word = word

    def __str__(self):
        # return "TAG:" + str(self.tag) + "    prob: "+ str(self.probability) + "  prev: " + str(self.prev)
        return "  word: " + str(self.word) + "   tag:" + str(self.tag)

    def __lt__(self, other):
        return self.probability < other.probability


def populate_trellis(sentence, tag_set, emission):
    """
    :param sentence: sentence to be tagged
    :param tag_set: set of tags
    :param emission: dictionary of emission probabilities
    :return: trellis: 2D array of nodes
    """
    num_of_words = len(sentence)
    num_of_tags = len(tag_set)
    trellis = [[node('NONE', 0, 'NONE', 'NONE') for i in range(num_of_words)] for j in range(num_of_tags)]
    for j, tag in enumerate(tag_set):
        for i, word in enumerate(sentence):
            pair = (word, tag)
            trellis[j][i].probability = get_emission(pair, emission)
            trellis[j][i].tag = tag
            trellis[j][i].word = word

    return trellis


def get_emission(pair, emission):
    """
    :param pair: tuple of word and tag
    :param emission: dictionary of emission probabilities
    :return: num: emission probability of pair
    """
    if pair not in emission:
        num = emission[pair[1]]
    else:
        num = emission[pair]
    return num


def get_probs(transition, t_pair):
    """
    :param transition: dictionary of transition probabilities
    :param t_pair: tuple of tags
    :return: tra: transition probability of t_pair
    """
    if t_pair not in transition:
        tra = transition["UNK"]
    else:
        tra = transition[t_pair]

    return tra


def get_initial(initial, tag):
    """
    :param initial: dictionary of initial probabilities
    :param tag: tag
    :return: out: initial probability of tag
    """
    if tag in initial:
        out = initial[tag]
    else:
        out = initial["UNK"]
    return out


def find_hapax(train, tag_set):
    """
    :param:  training data (list of sentences, with tags on the words)
            tag_set (set of tags)
    :return: hapax: a dictionary of hapax legomena
    """
    hapax_set = {}
    hapax_prob = {}
    total_count = 0
    for tag in tag_set:
        hapax_prob[tag] = 0

    for sentence in train:
        for word, tag in sentence:
            pair = (word, tag)
            if pair not in hapax_set:
                hapax_set[pair] = 1
                hapax_prob[tag] += 1
                total_count += 1

    for tag in tag_set:
        hapax_prob[tag] /= total_count
    hapax_prob["UNK"] = 1 / total_count

    return hapax_prob


def get_tw_pair(train):
    """
    :param train: training data (list of sentences, with tags on the words)
    :returns: tag_set: a set of all tags
            tag_count: the number of tags
            tags: a dictionary of tags and their counts
            tw_pair: a dictionary of (word, tag) pairs and their counts
    """
    tag_count = {}  # for the number of tags
    num_of_tags = 0  # number of tags
    tag_set = []  # for the order of tags
    tw_pair = {}  # for the number of data

    for sentence in train:
        for word, tag in sentence:
            if tag not in tag_count:
                tag_set.append(tag)
                num_of_tags += 1
                tag_count[tag] = 1
            else:
                tag_count[tag] += 1
            if word not in tw_pair:
                tw_pair[word] = {tag: 1}
            else:
                if tag not in tw_pair[word]:
                    tw_pair[word][tag] = 1
                else:
                    tw_pair[word][tag] += 1
    return tag_set, tag_count, num_of_tags, tw_pair
#  return tags,tag_set,tag_count
# tag_set,tag_count, num_of_tags = get_tag_num(train)



def initial_p(train):
    """
    :param train: training data (list of sentences, with tags on the words)
    :return: initial: a dictionary of initial probabilities
    """
    init_p = {}
    tag_count = 0
    for sentence in train:
        first_tag = sentence[0][1]
        if first_tag not in init_p:
            init_p[first_tag] = 1
            tag_count += 1
        else:
            init_p[first_tag] += 1

    for key in init_p:
        init_p[key] = (init_p[key] + 0.001) / (len(train) + 0.001 * tag_count)
    init_p["UNK"] = 0.001 / (len(train) + 0.001 * tag_count)

    return init_p


def transition_p(train, tag_count):
    """
    :param train: training data (list of sentences, with tags on the words)
    :param tags: a list of tags
    :return: transition: a dictionary of transition probabilities
    """
    tp = {}

    for sentence in train:
        for i in range(1, len(sentence)):
            prev_tag = sentence[i - 1][1]
            cur_tag = sentence[i][1]
            tag_tuple = (cur_tag, prev_tag)
            if tag_tuple not in tp:
                tp[tag_tuple] = 1
            else:
                tp[tag_tuple] += 1

    for key in tp:
        # tp[key] /= tag_set[key[1]]
        tp[key] = (tp[key] + 0.00001) / (tag_count[key[1]] + 0.00001 * len(tp))

    tp["UNK"] = 0.00001 / (sum(tp.values()) + 0.00001 * len(tp))

    return tp


def emission_p(train, tag_count, tag_set):
    """
    :param train: training data (list of sentences, with tags on the words)
    :param tag_count: the number of tags
    :param tag_set: a set of all tags
    :return: emission: a dictionary of emission probabilities
    """
    emission = {}
    total_tag_count = 0
    for sentence in train:
        for pair in sentence:
            if pair not in emission:
                emission[pair] = 1
            else:
                emission[pair] += 1

    for key in emission:
        # emission[key] /= tag_count[key[1]]
        emission[key] = (emission[key] + 0.00001) / (tag_count[key[1]] + 0.00001 * len(emission))

    for tag in tag_set:
        # emission[tag] = 0.000001/tag_count[tag]
        emission[tag] = 0.00001 / (tag_count[tag] + 0.00001 * len(emission))

    return emission


def hapax_emission_p(train, tag_count, tag_set, hapax):
    """
    :param train: training data (list of sentences, with tags on the words)
    :param tag_count: the number of tags
    :param tag_set: a set of all tags
    :return: emission: a dictionary of emission probabilities
    """
    emission = {}
    total_tag_count = 0
    for sentence in train:
        for pair in sentence:
            if pair not in emission:
                emission[pair] = 1
            else:
                emission[pair] += 1

    for key in emission:
        # emission[key] /= tag_count[key[1]]
        emission[key] = (emission[key] + 0.00001) / (tag_count[key[1]] + 0.00001 * len(emission))

    for tag in tag_set:
        # emission[tag] = 0.000001/tag_count[tag]
        emission[tag] = (0.00001 * hapax[tag]) / (tag_count[tag] + 0.00001 * len(emission))

    return emission
