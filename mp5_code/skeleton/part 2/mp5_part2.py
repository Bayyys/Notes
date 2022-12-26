# mp5.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 10/27/2018
# Modified by Mahir Morshed for the spring 2021 semester

import sys
import argparse
import configparser
import copy

import numpy as np
import torch

import reader
import neuralnet as p


"""
This file contains the main application that is run for this MP.
"""

def compute_accuracies(predicted_labels,dev_set,dev_labels):
    yhats = predicted_labels
    if len(yhats) != len(dev_labels):
        print("Lengths of predicted labels don't match length of actual labels", len(yhats),len(dev_labels))
        return 0.,0.,0.,0.

    accuracy = np.mean(yhats == dev_labels)

    tp = np.sum([yhats[i] == dev_labels[i] and yhats[i] == 1 for i in range(len(dev_labels))])
    fp = np.sum([yhats[i] != dev_labels[i] and yhats[i] == 1 for i in range(len(dev_labels))])
    fn = np.sum([yhats[i] != dev_labels[i] and yhats[i] == 0 for i in range(len(dev_labels))])

    precision = tp / (tp + fp)
    recall = tp / (fn + tp)
    f1 = 2 * (precision * recall) / (precision + recall)

    return accuracy, f1, precision, recall

def main(args):
    reader.init_seeds(args.seed)

    train_set, train_labels, dev_set, dev_labels = reader.load_dataset(args.dataset_file)


    train_set = torch.tensor(train_set, dtype=torch.float32)
    train_labels = torch.tensor(train_labels, dtype=torch.int64)
    dev_set = torch.tensor(dev_set, dtype=torch.float32)

    _, predicted_labels, net = p.fit(train_set, train_labels, dev_set, args.max_iter)
    accuracy, f1, precision, recall = compute_accuracies(predicted_labels, dev_set, dev_labels)

    print("Accuracy:", accuracy)
    print("F1-Score:", f1)
    print("Precision:", precision)
    print("Recall:", recall)

    # Check if dev accuracy reaches threshold
    total_score = 0
    for threshold in [0.6, 0.75, 0.794, 0.82, 0.83]:
        if (accuracy >= threshold):
            total_score += 5
            print("+5 points for dev accuracy above", str(threshold))
        else:
            print("Dev accuracy needs to be above", str(threshold))
            break

    # Test number of parameters
    num_parameters = sum([np.prod(w.shape) for w in net.parameters()])
    threshold = 500000
    low_threshold = 10000
    if num_parameters >= threshold:
        print("Num_parameters: " + str(num_parameters) + ". This is should be below " + str(threshold) + "!")
    if num_parameters <= low_threshold:
        print("Num_parameters: " + str(num_parameters) + ". This is should be above " + str(threshold) + "!")

    # Test network architecture
    for param_tensor in net.state_dict():
        print(param_tensor, "\t", net.state_dict()[param_tensor].size())
    state_dict = [torch.Size([32, 3072]), torch.Size([32]), torch.Size([2, 32]), torch.Size([2])]
    state_dict_student = []
    for param_tensor in net.state_dict():
        # print(param_tensor, "\t", net.state_dict()[param_tensor].size())
        state_dict_student.append(net.state_dict()[param_tensor].size())
    if state_dict == state_dict_student:
        print('The architecture matches with the given one')
    else:
        print('The architecture used is different than what was asked for')
    torch.save(net, "net.model")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CS440/ECE448 MP5: Neural Nets and PyTorch')

    parser.add_argument('--dataset', dest='dataset_file', type=str, default = 'mp5_data',
                        help='directory containing the training data')
    parser.add_argument('--max_iter',dest="max_iter", type=int, default = 500,
                        help='Maximum iterations: default 500')
    parser.add_argument('--seed', dest="seed", type=int, default=42,
                        help='seed source for randomness')


    args = parser.parse_args()
    main(args)