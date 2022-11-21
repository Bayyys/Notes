# TextClassifier.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Dhruv Agarwal (dhruva2@illinois.edu) on 02/21/2019

"""
You should only modify code within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
import math

class TextClassifier(object):
    def __init__(self):
        """Implementation of Naive Bayes for multiclass classification

        :param lambda_mixture - (Extra Credit) This param controls the proportion of contribution of Bigram
        and Unigram model in the mixture model. Hard Code the value you find to be most suitable for your model
        """
        self.class_num = 14
        self.lambda_mixture = 0.1
        self.prior = []
        self.likelihood = []
        self.word_bag = []

    def fit(self, train_set, train_label):
        """
        :param train_set - List of list of words corresponding with each text
            example: suppose I had two emails 'i like pie' and 'i like cake' in my training set
            Then train_set := [['i','like','pie'], ['i','like','cake']]

        :param train_labels - List of labels corresponding with train_set
            example: Suppose I had two texts, first one was class 0 and second one was class 1.
            Then train_labels := [0,1]
        """

        # prior of 14 class
        # 获得每个class的prior
        self.prior = [0] * self.class_num
        prior = [0] * self.class_num
        prior_log = [0] * self.class_num
        for i in range(len(train_label)):
            self.prior[train_label[i] - 1] += 1
        for i in range(len(self.prior)):
            prior[i] = self.prior[i] / len(train_label)
            prior_log[i] = math.log(prior[i])
        self.prior = prior_log

        # word_bag (24906)
        # text任务相比image不同点在于，image中feature的value只有255中，
        # 而text中每个feature的value应该包含所有可能的单词数为value数
        # 根据train数据集，将所有word遍历，获得一个词包，共有24906种
        for i in range(len(train_set)):
            for j in range(len(train_set[i])):
                word = train_set[i][j]
                if word not in self.word_bag:
                    self.word_bag.append(word)

        # likelihood 14 sublist, every sublist have 24906
        # 获得likelihood， 没有考虑word出现的位置，只获得了每个class下，word bag中每个单词出现的次数作为likelihood
        self.likelihood = []
        for i in range(self.class_num):
            list = [0] * len(self.word_bag)
            self.likelihood.append(list)
        for i in range(len(train_set)):
            for j in range(len(train_set[i])):
                word = train_set[i][j]
                # print(word)
                word_index = self.word_bag.index(word)
                # print(word_index)
                class_idx = train_label[i]
                # print(class_idx)
                self.likelihood[class_idx - 1][word_index] += 1
        # print(len(self.likelihood[0]))

        sum = [0] * self.class_num
        for i in range(len(self.likelihood)):
            for j in range(len(self.likelihood[i])):
                sum[i] += self.likelihood[i][j]

        for i in range(len(self.likelihood)):
            for j in range(len(self.likelihood[i])):
                self.likelihood[i][j] = (self.likelihood[i][j] + self.lambda_mixture) / (sum[i] + self.lambda_mixture)
                self.likelihood[i][j] = math.log(self.likelihood[i][j])

    def predict(self, x_set, dev_label, lambda_mix=0.0):
        """
        :param dev_set: List of list of words corresponding with each text in dev set that we are testing on
              It follows the same format as train_set
        :param dev_label : List of class labels corresponding to each text
        :param lambda_mix : Will be supplied the value you hard code for self.lambda_mixture if you attempt extra credit

        :return:
                accuracy(float): average accuracy value for dev dataset
                result (list) : predicted class for each text
        """

        accuracy = 0.0
        result = [0] * len(x_set)
        class_prob = []

        # class_prob 计算出x属于每个class的概率
        for i in range(len(x_set)):
            list = [0] * self.class_num
            class_prob.append(list)
        # 先为class_prob 加入每个class的prior
        for i in range(len(class_prob)):
            for j in range(len(class_prob[i])):
                class_prob[i][j] = self.prior[j]
        # 将x_set中出现的word的属于每个class的likelihood分别加入
        for i in range(len(x_set)):
            for j in range(len(x_set[i])):
                word = x_set[i][j]
                if word in self.word_bag:
                    word_index = self.word_bag.index(word)
                    for class_idx in range(self.class_num):
                        class_prob[i][class_idx] += self.likelihood[class_idx][word_index]
        # print(class_prob)

        # 对于class_prob找出最大概率的class来最为预测的概率
        for i in range(len(class_prob)):
            for j in range(len(class_prob[i])):
                if class_prob[i][j] > class_prob[i][result[i]]:
                    result[i] = j
            result[i] += 1

        # 判断准确率
        num_correct = 0
        for i in range(len(result)):
            if result[i] == dev_label[i]:
                num_correct += 1
        accuracy = num_correct / len(dev_label)

        return accuracy, result
