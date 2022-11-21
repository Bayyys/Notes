import numpy as np

class NaiveBayes(object):
    def __init__(self, num_class, feature_dim, num_value):
        """Initialize a naive bayes model.

        This function will initialize prior and likelihood, where
        prior is P(class) with a dimension of (# of class,)
            that estimates the empirical frequencies of different classes in the training set.
        likelihood is P(F_i = f | class) with a dimension of
            (# of features/pixels per image, # of possible values per pixel, # of class),
            that computes the probability of every pixel location i being value f for every class label.

        Args:
            num_class(int): number of classes to classify
            feature_dim(int): feature dimension for each example
            num_value(int): number of possible values for each pixel
        """

        self.num_value = num_value
        self.num_class = num_class			# 10
        self.feature_dim = feature_dim		# 784

        self.prior = np.zeros(num_class)
        self.likelihood = np.zeros((feature_dim, num_value, num_class))

    def train(self, train_set, train_label, k_smooth):
        """ Train naive bayes model (self.prior and self.likelihood) with training dataset.
            self.prior(numpy.ndarray): training set class prior (in log) with a dimension of (# of class,),
            self.likelihood(numpy.ndarray): traing set likelihood (in log) with a dimension of
                (# of features/pixels per image, # of possible values per pixel, # of class).
            You should apply Laplace smoothing to compute the likelihood.

        Args:
            train_set(numpy.ndarray): training examples with a dimension of (# of examples, feature_dim)
            train_label(numpy.ndarray): training labels with a dimension of (# of examples, )
        """
        # k_smooth是拉普拉斯平滑处理，分别取了0 0.1 0.5 1 5 10

        # 计算prior，获取10个class的image数，除以总image数，得到各个class的prior
        # 共10类
        for i in range(len(train_label)):
            label = train_label[i]
            self.prior[label] += 1
        self.prior /= len(train_label)
        self.prior = np.log(self.prior)


        # likehood计算
        # likelihood是一个784*255*10的张量
        # 表示，在class=i的情况下， 784个feature中的某个feature取255个value的某个value的概率
        # 对train数据进行统计得到， 并转化为概率时进行laplace smooth，取对数

        x = train_set.reshape(-1, 1)
        for i in range(len(x)):
            label = train_label[i // self.feature_dim]
            self.likelihood[i % self.feature_dim, x[i, 0].astype('int'), label] += 1

        for i in range(self.likelihood.shape[0]):
            self.likelihood[i] = (self.likelihood[i] + k_smooth) / (np.sum(self.likelihood[i], axis=0) + k_smooth)
        self.likelihood = np.log(self.likelihood)



    def test(self,test_set,test_label):
        """ Test the trained naive bayes model (self.prior and self.likelihood) on testing dataset,
            by performing maximum a posteriori (MAP) classification.
            The accuracy is computed as the average of correctness
            by comparing between predicted label and true label.

        Args:
            test_set(numpy.ndarray): testing examples with a dimension of (# of examples, feature_dim)
            test_label(numpy.ndarray): testing labels with a dimension of (# of examples, )

        Returns:
            accuracy(float): average accuracy value
            pred_label(numpy.ndarray): predicted labels with a dimension of (# of examples, )
        """

        accuracy = 0
        pred_label = np.zeros((len(test_set)))

        # pred_prob为每一张图片预测的每一个class的概率，为10000*10
        pred_prob = np.zeros((len(test_set), self.num_class))   # (10000, 10)
        # print(pred_prob.shape)

        # pred_prob：class的prior概率 + 784个feature 分别去取 对应value的概率
        for set_idx in range(len(test_set)):
            for class_idx in range(self.num_class):
                pred_prob[set_idx, class_idx] = self.prior[class_idx]
                for feature_idx in range(self.feature_dim):
                    pred_prob[set_idx, class_idx] += self.likelihood[feature_idx, test_set[set_idx, feature_idx].astype('int'), class_idx]

        # 对pred_prob每一行找最大值， 即为预测的class
        pred_label = np.argmax(pred_prob, axis=1)

        correct = 0
        for i in range(len(test_set)):
            if pred_label[i] == test_label[i]:
                correct += 1
        accuracy = correct / len(test_set)

        return accuracy, pred_label

    def save_model(self, prior, likelihood):
        """ Save the trained model parameters
        """

        np.save(prior, self.prior)
        np.save(likelihood, self.likelihood)

    def load_model(self, prior, likelihood):
        """ Load the trained model parameters
        """

        self.prior = np.load(prior)
        self.likelihood = np.load(likelihood)

    def intensity_feature_likelihoods(self, likelihood):
        """
        Get the feature likelihoods for high intensity pixels for each of the classes,
            by sum the probabilities of the top 128 intensities at each pixel location,
            sum k<-128:255 P(F_i = k | c).
            This helps generate visualization of trained likelihood images.

        Args:
            likelihood(numpy.ndarray): likelihood (in log) with a dimension of
                (# of features/pixels per image, # of possible values per pixel, # of class)
        Returns:
            feature_likelihoods(numpy.ndarray): feature likelihoods for each class with a dimension of
                (# of features/pixels per image, # of class)
        """

        feature_likelihoods = np.zeros((likelihood.shape[0], likelihood.shape[2]))  # (784,10)
        feature_likelihoods = likelihood[:, 128:255, :].sum(axis = 1)

        return feature_likelihoods
