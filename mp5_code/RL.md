# Assignment 5: Reinforcement Learning and Deep Learning 

[TOC]

# Part 1: Q-learning (Snake) 

Snake是一款著名的电子游戏，起源于1976年的街机游戏《封锁》。玩家使用上下左右来控制蛇的长度(当它吃食物时)，蛇的身体和周围环境的墙壁是主要障碍。在这个作业中，你将使用强化学习来训练AI代理玩一个简单版本的游戏蛇。您将实现Q-learning算法的TD版本。

## Provided Snake Environment 

![snake](https://s2.loli.net/2022/12/19/9zoxBjfH1C4plG7.png)

在这项任务中，整个游戏板的大小为560x560。绿色的矩形是蛇剂，红色的矩形是食物。蛇头用较厚的木板标记，以方便识别。

一旦最初的食物被吃掉，食物就会在棋盘上随机产生。墙的每一面(用蓝色填充)的尺寸是**40**。蛇的头部、身体部分和食物的大小都是40x40。蛇以每帧40的速度移动。在这个设置中，我们的蛇代理可以移动的整个棋盘的大小为480x480，可以被视为一个12x12的网格。每当它吃下一种食物，点数就会增加1，它的身体就会增长一段。在实施Q-learning算法之前，我们必须首先将Snake定义为一个马尔可夫决策过程(MDP)。

**注意在Q-learning中，状态变量不需要代表整个棋盘，它只需要代表足够的信息来让代理做决定。(所以一旦你得到环境状态，你需要把它转换成下面定义的状态空间)。另外，状态空间越小，代理人就能越快地探索它的全部。**

- **State**: 一个元组`(adjoining_wall_x, adjoining_wall_y, food_dir_x, food_dir_y, adjoining_body_top, adjoining_body_bottom, adjoining_body_left, adjoining_body_right)`

  -   **[adjoining_wall_x, adjoining_wall_y]** 给出蛇头旁边是否有墙。它有9种状态：

     **adjoining_wall_x**: **0** (x轴上没有相邻的墙), **1** (墙在蛇头左边), **2** (墙在蛇头右边)

    **adjoining_wall_y:** **0**(y轴上没有相邻的墙), **1**(蛇头顶部的墙), **2**(蛇头底部的墙)

    **(注意[0, 0]也是蛇跑出480x480板的情况)**

  -  **[food_dir_x, food_dir_y]** 给出食物到蛇头的方向。它有9种状态： **food_dir_x**: **0** (x轴上的坐标相同), **1** (食物在蛇头左边), **2** (食物在蛇头右边)  **food_dir_y**: **0**(Y轴上的坐标相同)，**1**(食物在蛇头顶部)，**2**(食物在蛇头底部)。

  - **[adjoining_body_top, adjoining_body_bottom, adjoining_body_left, adjoining_body_right]** 检查蛇头的相邻方格中是否有蛇体。它有8种状态：

    **adjoining_body_top**: **1**(相邻的顶部方格有蛇的身体)，**0**(否则) 

    **adjoining_body_bottom**: **1**(相邻的底部方格有蛇的身体)，**0**(否则) 

    **adjoining_body_left**: **1**(相邻的左侧方格有蛇的身体)，**0**(否则) 

    **adjoining_body_right**: **1**(相邻的右侧方格有蛇的身体)，**0**(否则)

- **Actions** :你的代理人的行动是从{上、下、左、右}集合中选择的。

- **Rewards** :当你的行动导致获得食物时，奖励+1(蛇头位置与食物位置相同)，当蛇死亡时，即蛇头撞到墙，其身体部分或蛇头试图向其相邻的身体部分移动(向后移动)，奖励-1。否则为-0.1(不死亡也不获得食物)。

## Q-learning Agent 

在这部分作业中，你将创建一个蛇代理，学习如何在不死亡的情况下尽可能多地获得食物。为了做到这一点，你必须使用Q-learning。实施 `TD Q-learning` 算法，并在上述的MDP上训练它。
$$
Q(s,a) \gets Q(s,a) + \alpha(R(s)+\gamma\underset{a'}{max}-Q(s,a))
$$
另外，使用课堂上提到的探索政策，用**1**表示**R+**:
$$
a=\underset{a'\in A(s)}{argmax} \underset{ \underset{exploration function}{\uparrow}}{f}(A(s,a'), \underset{\underset{Number of times we've taken action a' in state s}{\uparrow}}{N(s,a')})
$$

$$
f(u,n)=
\begin{cases}
R^+ & if \quad n<N_e \quad (optimistic reward estimate)\\
u &otherwise\\
\end{cases}
$$

在训练过程中，你的代理需要先更新你的Q表(当初始状态和行动为无时，这一步会被跳过)，使用上述探索策略获得下一个行动，然后用该行动更新N表。如果游戏结束了，也就是当死亡变量变成真的时候，你只需要更新你的Q表，并重置游戏。在测试期间，你的代理只需要使用Q表给出最佳行动。只要你认为有必要，就训练它，计算你的代理人能得到的平均分。在1000个测试游戏中，你的平均分应该至少是20分。 

**为了评分的目的，请提交带有上述探索策略、状态配置和奖励模型的代码。我们将用不同的参数(Ne、C、gamma)初始化你的代理类，用不同的初始蛇和食物位置初始化环境，并在训练时比较第一个食物被吃掉时的Q表结果(Q表生成细节见Snake_main.py)。**

一旦你有了这个工作，你将需要调整学习率α(一个固定的学习率或其他C值如何？)、贴现因子γ以及你用来权衡探索与开发的设置。

 在你的报告中，请包括α、γ的值，以及你所使用的探索设置的任何参数，并讨论你如何获得这些值。当你调整这些变量时，游戏中会发生什么变化？你的代理人在学习最佳政策之前需要模拟多少场游戏？在你的Q-learning似乎已经收敛到一个好的政策之后，在大量的测试游戏(≥1000)上运行你的算法，并报告平均得分的数量。

 除了讨论这些事情之外，还可以尝试调整上面定义的状态配置。如果你认为有好处，你也可以改变奖励模型，为代理人提供更多信息反馈。试着找到允许代理学习比你之前发现的更好的政策的修改。在你的报告中，描述你所做的修改以及代理人能够得到的新的点数。这对训练你的代理人的时间有什么影响？包括任何其他有趣的观察。

**提示**

- 为了更好地理解Q学习算法，请阅读教科书的第21.3节。

- 最初，所有的Q值估计值都应该是0。
- 学习率应该以 $C/(C+N(s,a))$ 的方式衰减，其中N(s,a)是你看到给定状态-动作对的次数。
- 在调整状态配置的时候，尽量使状态数变小，以使训练更容易进行。如果状态数过大。蛇可能会陷于无限循环。
- 在一个合理的实现中，你应该看到你的平均分在几秒钟内增加。
- 你可以运行`python snake_main.py --human`来自己玩游戏。

## Debug Convenience

为了调试方便，我们为你提供了三个Q表的调试例子。**每个Q表都是在训练过程中蛇吃了第一个食物后生成的。更确切地说，是蛇在训练中第一次正好达到1个点的时候**，请看**snake_main.py**中的Q表是如何在训练中生成和保存的。例如，你可以运行`diff checkpoint.npy checkpoint1.npy`来看看是否有区别。这三个调试例子的唯一区别是参数的设置(蛇头和食物的初始化位置、Ne、C和gamma)。

注意，如果探索函数的动作得分相等，那么优先级应该是 **右>左>下>上**。

  - [调试实例1] `snake_head_x=200, snake_head_y=200, food_x=80, food_y=80, Ne=40, C=40, gamma=0.7 checkpoint1.npy `
  - [调试实例2] `snake_head_x=200, snake_head_y=200, food_x=80, food_y=80, Ne=20, C=60, gamma=0。 5 checkpoint2.npy `
  - [调试实例3] `snake_head_x=80, snake_head_y=80, food_x=200, food_y=200, Ne=40, C=40, gamma=0.7 checkpoint3.npy `

确保你能通过这些调试实例将对你有很大帮助。此外，**平均分超过20分的1000个测试游戏**应该可以获得这部分的全额学分。

---

# Part 2: Classical Neural Network

在这一部分，你将使用PyTorch和NumPy库来实现神经网络。PyTorch库将为你完成大部分繁重的工作，但还是要靠你来实现正确的高层指令来训练模型。

基本的神经网络模型由一连串的隐藏层组成，中间夹着一个输入和输出层。输入是由输入层输入的，数据通过隐藏层并输出到输出层。每个神经网络诱导的都是一个函数$F_W$，它是通过将数据通过层传播而得到的。

为了更精确地说明问题，在讲座中你学到了一个函数$f_W = \sum^n_{i=1}w_ix_i+b$ 。在这项作业中，给定权重矩阵$W_1,W_2$ 为 $ W_1 \in R^{h \times d},W_2 \in R^{h \times 2} $， 以及偏置向量$b_1 \in R^h \quad and \quad b_2 \in R^2 $ 你将学习一个函数 $F_W$，定义为
$$
F_w(x)=W_2\sigma(W_1x+b_1)+b_2
$$
其中 $\sigma$ 是激活函数。在第2部分，你应该使用[**sigmoid**]([Sigmoid — PyTorch 1.13 documentation](https://pytorch.org/docs/stable/generated/torch.nn.Sigmoid.html))或[**ReLU**]([ReLU — PyTorch 1.13 documentation](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html))**激活函数**。你将使用32个隐藏单元(h=32)和3072个输入单元，图像中每个像素的每个通道都有一个($d=(32)^2(3)=3072$)。

## Dataset

该数据集包括10000张32x32的彩色图像([CIFAR-10数据集]([CIFAR-10 and CIFAR-100 datasets (toronto.edu)](https://www.cs.toronto.edu/~kriz/cifar.html))的一个子集，由Alex Krizhevsky提供)，为你分成7500个训练实例(其中2999个是负面的，4501个是正面的)和2500个开发实例。

该数据集包含在编码模板中。当你解压缩时，你会发现一个二进制对象，我们的阅读器代码将为你解压。

## Training and Development

- 训练: 为了训练神经网络，你需要使经验风险 $R(W)R(W)$ 最小化，它被定义为由某个损失函数决定的平均损失。对于这项任务，你可以使用交叉熵来计算该损失函数。在二元分类的情况下。经验风险由
  $$
  \mathbb{R}(W)=\frac{1}{n}\sum^n_{i=1}y_i\log \widehat{y_i}+(1-y_i)\log (1-\widehat{y_i})
  $$
  

   其中$y_i$是标签，$\widehat{y_i}$ 取决于$\widehat{y_i}=\sigma(F_W)(x_i)$ ，$\sigma(x)=\frac{1}{1+e^{-x}}$是sigmoid函数。对于这项作业，你不必自己实现这些函数；你可以使用PyTorch的内置函数。

  注意，由于PyTorch的**CrossEntropyLoss**包含了一个sigmoid函数，你不需要在网络的最后一层明确包含一个激活函数。

- 开发: 在你训练好你的神经网络模型后，你将让你的模型决定开发集中的图像是否包含动物。这是通过在开发集的每个例子上评估你的网络 $F_W$，然后取两个输出的最大值(argmax)的指数来实现的。

- 数据标准化: 通过简单地集中你的输入数据，减去样本平均值并除以样本标准差，可以极大地提高收敛速度和准确度。更准确地说，你可以通过简单地设置 来改变数据矩阵 $ X =(X-\mu)/\sigma$

 有了上述的模型设计和提示，你应该期望有大约0.84的偏差设定精度。

### Extra credit: CIFAR-100 superclasses

对于这个MP的额外10%的分数，你的任务是从CIFAR-100数据集(与CIFAR-10在同一个地方描述)中挑选任意两个超类，并在必要时重做第二部分的神经网络，以区分这两个超类。一个超类包含2500张训练图像和500张测试图像，因此在两个超类之间，你要处理的数据量是总数的3/5(这里的图像总数为6000张，而主MP中的总数为10000张)。

要开始进行额外的工作，我们建议你复制整个目录，其中包含你对主要**MP**的第二部分的解决方案。然后替换数据目录和文件 **reader.py**，并修改你的文件 **neuralnet.py**，如下面两段所述。

- 用CIFAR-100替换CIFAR-10，并下载新的阅读器

你可以在这里[下载](https://urldefense.com/v3/__https:/www.cs.toronto.edu/*kriz/cifar-100-python.tar.gz__;fg!!DZ3fjg!rLzUb6heg749voJk2iylBPHHiCf5sQOW9YYJHhWIVxbL5osVegL5yVerRpTR-Qb4ebU$)CIFAR-100的数据，并将其提取到你放置主MP数据的同一个地方。[这里](https://courses.grainger.illinois.edu/ece448/sp2022/mps/mp2/reader_ec.zip)提供了一个`custom reader`；为了将其用于CIFAR-100的数据，你应该将其重命名为**reader.py**，并替换工作目录中现有的该名称的文件。

- 修改**neuralnet.py**，以便选择你想分类的两个CIFAR-100类

在**neuralnet.py**文件的顶层(也就是NeuralNet类之外)定义两个全局变量_class1_和_class2_。将这些变量的值设置为整数，以便选择你想分类的两个类作为加分项。CIFAR描述页面上列出的超类的顺序提示了每个超类的索引；例如，"aquatic mammals "是0，"vehicles 2 "是19。

- 现在你有了新的分类任务，你应该做的第一件事是尝试运行你在常规MP第二部分中使用的相同代码，在这些新数据上重新训练你的神经网络，然后测试它，看它的表现如何。这可以作为你的基线；你的加分目标将是找到新的算法，给你更好的准确性。你的新算法可以是任何你喜欢的东西(一个有更多层的网络，或每个隐藏层有更多的节点，或卷积神经网络，或任何其他你选择的算法)。

# Provided Code Skeleton

我们提供了skeleton.zip和下面的描述。对于第1部分，**除了pygame(pygame 1.9.4版)和numpy，不要导入任何非标准的库。**

## Part 1

- **snake.py** - 这个文件定义了蛇的环境并创建了游戏的GUI。

- **utils.py** - 这个文件定义了上面定义的一些离散化常数，并包含保存和加载模型的函数。

- **agent.py** - 这是你将进行所有工作的文件。该文件包含代理类。这是你要实现的在蛇的环境中行动的代理。下面是Agent类中的实例变量和函数的列表。

  - **self._train**: 这是一个布尔标志变量，你应该用它来确定代理是处于训练还是测试模式。在训练模式下，代理应该根据Q表进行探索(基于探索函数)和利用。在测试模式下，代理应该纯粹地利用，并始终采取最佳行动。

  - **train()** : 这个函数将self._train设为True。这个函数在snake_main.py的训练循环运行之前被调用 o test()。这个函数将self._train设置为False。这个函数在snake_main.py的测试循环运行前被调用。 o save_model(): 这个函数保存self.Q表。在snake_main.py的训练循环之后调用。

  - **load_model()** : 这个函数加载self.Q表。在snake_main.py的测试循环之前调用。

  - **act(state, points, dead)** : 这是你要实现的主要函数，在游戏运行时由**snake_main.py**反复调用。"state "是来自蛇环境的状态，是一个[snake_head_x, snake_head_y, snake_body, food_x, food_y]的列表(**注意，在act函数中，你首先需要将其离散化为我们上面定义的状态配置**)。"点 "是蛇吃过的食物的数量。"死 "是一个布尔值，表示蛇是否已经死亡。"积分"、"死亡 "应该用来定义你的奖励函数。 act应该从{0,1,2,3}的集合中返回一个数字。返回0将使蛇代理向上移动，返回1将使蛇代理向下移动，而返回2将使代理向左移动，返回3将使代理向右移动。如果**self._train**是True，这个函数应该更新Q表并返回一个动作(**注意，如果探索函数的动作得分相等，优先级应该是右>左>下>上**)。如果**self._train**是假的，代理应该简单地返回基于Q表的最佳行动。

- **snake_main.py** - 这是启动程序的主文件。这个文件运行蛇形游戏，你实现的代理在其中行动。该代码先运行一些训练游戏，然后运行一些测试游戏，最后显示示例游戏。

**你只需要修改agent.py即可。**

## Part 2 

- **reader.py** - 这个文件负责读入数据集。它创建了一个巨大的NumPy数组，该数组中的特征向量对应于每张图像。

- **mp5_part2.py** - 这是启动程序的主文件，并使用你的实现计算准确率、精确度、召回率和F1分数 

- **neuralnet.py** - 是你将在第二部分做所有工作的文件。你会得到一个**NeuralNet**类，它实现了**torch.nn.module**。这个类由**\_\_init\_\_()**、**forward()**和**step()**函数组成。(除了下面的重要细节外，在骨架代码中给出了更多关于 NeuralNet 类中每个方法应该做什么的信息。) 

  -  **\_\_init\_\_()** 是你需要构建网络结构的地方。有多种方法可以做到这一点。

    - 一种方法是使用 [Linear]([Linear — PyTorch 1.13 documentation](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)) 和 [Sequential]([Sequential — PyTorch 1.13 documentation](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html)) 对象。请记住，Linear使用Kaiming He统一初始化来初始化权重矩阵，并将偏置项设置为全零。


    - 另一种方法是明确定义权重矩阵$W_1,W_2,\ldots$和偏置项$b_1,b_2,\ldots$，将它们定义为[Tensors]([torch.Tensor — PyTorch 1.13 documentation](https://pytorch.org/docs/stable/tensors.html))。这种方法更容易上手，可以让你选择自己的初始化。然而，对于这项任务来说，何凯明统一初始化应该足够了，应该是一个不错的选择。

    此外，你可以在这个函数中初始化一个[optimizer]([torch.optim — PyTorch 1.13 documentation](https://pytorch.org/docs/stable/optim.html))对象，用于在`step()`函数中优化你的网络。

  - **forward() **应该在你的网络中执行一个前向传递。这意味着它应该明确地评估㼿㼿$F_W(x)$。这可以通过简单地调用你在`__init__()`中定义的Sequential对象或者(如果你选择明确地定义张量)用你的数据乘以权重矩阵来完成。

  - **step()**  应该进行一次迭代训练。这意味着它应该通过一批训练数据(而不是整个训练数据集)执行一次梯度更新。你可以通过调用 `loss_fn(yhat,y).backward() `然后自己直接更新权重来实现，或者你可以使用你在 `__init__() ` 中初始化的优化器对象来帮助你更新网络。请确保在你的优化器上调用`zero_grad()`，以清除梯度缓冲区。当你从这个函数返回loss_value时，确保你返回`loss_value.item()`(如果它只是一个单一的数字就可以)或`loss_value.detach().cpu().numpy()`(它将损失值与导致它的计算分离，将它移到CPU上--如果你决定在本地的GPU上工作，这一点很重要，记住Gradescope不会被配置为GPU，然后将它转换为NumPy数组)。这样就可以进行适当的垃圾回收(以免你的程序可能超过Gradescope上固定的内存限制)。

  - **fit()** 将训练数据、训练标签、开发集和最大迭代次数作为输入。提供的训练数据是 **reader.py** 的输出。训练标签是一个张量，由训练数据中每张图片对应的标签组成。开发集是一个由图像组成的张量，你将在上面测试你的实现。迭代的最大数量是你用`--max_iter`指定的数量(默认是500)。 `fit()`输出预测的标签。它应该构建一个NeuralNet对象，并迭代调用神经网络的`step()`来训练网络。这应该通过输入由批次大小决定的数据批次来完成。max_iter是你训练过程中的批次数(不是epochs的数量！)。

- **mp5_data** 是数据集的文件。请参阅reader.py和mp5_part2.py了解如何加载和处理数据。

要了解更多关于如何运行MP的信息，请在终端运行`python3 mp5_part2.py -h`。

你肯定应该使用本页面上多次链接的[PyTorch文档]([Training a Classifier — PyTorch Tutorials 1.13.0+cu117 documentation](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html))来帮助你了解实现细节。你也可以使用这个PyTorch教程作为参考来帮助你实现。还有其他的指南，比如[这个](https://medium.com/biaslyai/pytorch-introduction-to-neural-network-feedforward-neural-network-model-e7231cff47cb)。

# Deliverables

本MP将通过Bb提交。请只上传以下文件到Bb。

 - **agent.py** 具有上述相同的探索策略、状态配置和奖励模型。

- **q_agent.npy** 你用上述相同的状态配置训练的最佳numpy阵列。(可以通过在snake_main.py中传递"`--model_name q_agent.npy `"来保存)。**请注意，上面的这个模型应该在不修改agent.py以外的任何代码文件的情况下工作。**

- **neuralnet.py ** 于第二部分。

- **report.pdf**

# Report Checklist

## Part 1

1. 简要描述你的代理蛇的实施。

   - 代理在训练阶段是如何行动的？ 
   - 代理在测试阶段是如何行动的？2. 

2. 使用你认为最好的Ne, C (或固定的alpha?), gamma。在训练收敛后，在1000个测试游戏上运行你的算法，并报告平均点。

   - 给出你认为最好的Ne、C(或固定α)的值。


   - 报告训练收敛时间。


   - 报告1000个测试游戏的平均分。


3. 描述你对你的MDP所做的修改(状态配置、探索策略和奖励模型)，**至少要对状态配置进行修改**。报告性能(1000个测试游戏的平均分)。注意，训练你修改后的状态空间应该在1000个测试游戏中给你至少10分的平均分。解释为什么这些改变是合理的，观察蛇在改变后的行为，分析它们的积极和消极影响。**再次注意，确保你提交的agent.py和q_agent.npy没有这些变化，你改变的MDP不应该被提交。**

 Part 2 

1. 报告你的实现的平均分类率、精确度、召回率和F1分数。

2. 添加一个图表，绘制出历时与该历时的损失。
3. 描述你看到的任何趋势。这是预期的还是令人惊讶的？你认为对这些观察的解释是什么？
3. 报告额外信贷部分，如果有的话。