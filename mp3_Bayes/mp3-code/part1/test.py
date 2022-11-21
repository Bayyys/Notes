from image_main import load_dataset
import numpy as np
import math

# x_train is 55000*784 y_train is 55000*1  x_test is 10000*784 y_test is 10000*1
x_train, y_train, x_test, y_test = load_dataset('./part1')


def train(train_set, train_label, num_class, feature_dim, num_value):
    prior = np.zeros(num_class)
    likelihood = np.zeros((feature_dim, num_value, num_class))

    # 计算prior，获取10个class的image数，除以总image数，得到各个class的prior
    for i in range(len(y_train)):
        label = y_train[i]
        prior[label] += 1
    prior /= len(y_train)
    prior = np.log(prior)

    # likehood计算
    x = x_train.reshape(-1, 1)
    for i in range(len(x)):
        label = y_train[i // 10]
        likelihood[i % 10, x[i, 0] - 1, label - 1] += 1

    for i in range(likelihood.shape[0]):
        likelihood[i] = likelihood[i] / np.sum(likelihood[i], axis=0)
    likelihood = np.log(likelihood)

    return prior, likelihood


# 8张图片，10个像素，5个值, 3个分类
x_train = np.random.randint(1, 6, (8, 10))
y_train = np.random.randint(1, 4, 8)
likelihood = np.zeros((10, 5, 3))
# 按行遍历图片的每个特征

x = x_train.reshape(-1, 1)
for i in range(len(x)):
    label = y_train[i // 10]
    likelihood[i % 10, x[i, 0]-1, label-1] += 1
print(likelihood)
# print(likelihood.shape[0])

for i in range(likelihood.shape[0]):
    # print(np.sum(likelihood[i], axis=0))
    likelihood[i] = likelihood[i] / np.sum(likelihood[i], axis=0)
# likelihood = likelihood / np.sum(likelihood, axis=0)
# print(likelihood)

likelihood = np.log(likelihood)
print(likelihood)


