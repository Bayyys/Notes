import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))




def logistic(X, y):
    '''
    LR Logistic Regression.

    INPUT:  X: training sample features, P-by-N matrix.
            y: training sample labels, 1-by-N row vector.

    OUTPUT: w: learned parameters, (P+1)-by-1 column vector.
    '''

    # P = 2, N = 100
    P, N = X.shape
    w = np.zeros((P+1, 1))
    # print(X)
    X = np.vstack((np.ones((1, N)), X))
    # print(X)
    learning_rate = 50

    for epoch in range(25000):
        predict_x = sigmoid(np.matmul(w.T, X))
        # 求出梯度
        gradient = (sigmoid(np.matmul(w.T, X)) - y) * sigmoid(np.matmul(w.T, X)) * (1 - sigmoid(np.matmul(w.T, X))) * X
        gradient = np.sum(gradient, axis=1) / y.shape[1]
        grad = np.zeros((P + 1, 1))
        grad[:, 0] = gradient
        # 更新权重
        w -= learning_rate * grad
        # print(w)

        # 计算损失
        if epoch % 1000 == 0:
            loss = np.sum(np.square(y - predict_x)) / (2 * y.shape[1])
            print('epoch is {}, loss is {}'.format(epoch, loss))
            # learning_rate /= 2

    print("training end")

    return w
