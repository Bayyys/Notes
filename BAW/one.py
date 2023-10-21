import numpy as np
import matplotlib.pyplot as plt


class Q:
    def __init__(self) -> None:
        self.initParams()
        self.drawInit()

    def initParams(self):
        self.N = 50  # 初识种群个数
        self.d = 2  # 个体维度
        self.limit = [-5, 5]  # 限制条件
        self.vlimit = [-10, 10]  # 速度限制
        self.w = 0.8  # 惯性权重
        self.c1 = 0.5  # 个体学习因子
        self.c2 = 0.5  # 群体学习因子
        self.x = np.random.uniform(
            self.limit[0], self.limit[1], (self.N, self.d)
        )  # 初始化位置
        self.v = np.random.uniform(
            self.vlimit[0], self.vlimit[1], (self.N, self.d)
        )  # 初始化速度
        self.xm = self.x
        self.ym = self.fun(self.xm[:, 0], self.xm[:, 1])
        self.fxm = np.ones((self.N, 1)) * float("inf")
        self.fym = float("inf")
        print(self.v.shape)
        print(self.xm.shape)
        print(self.x.shape)
        print(self.ym.shape)

    def drawInit(self):
        # 绘制函数图像
        x = y = np.linspace(self.limit[0], self.limit[1], 5000)
        fig = plt.figure("初始化状态")
        # 绘制三维曲面的图像
        ax = fig.add_subplot(projection="3d")
        X, Y = np.meshgrid(x, y)
        Z = self.fun(X, Y)
        ax.plot_surface(X, Y, Z, cmap="rainbow")
        ax.scatter(
            self.x[:, 0], self.x[:, 1], self.fun(self.x[:, 0], self.x[:, 1]), c="r"
        )

    def run(self, ger_all: int = 20):
        plt.ion()
        # 解决中文乱码问题
        plt.rcParams["font.sans-serif"] = ["SimHei"]
        ax = plt.figure("迭代过程").add_subplot(projection="3d")
        X = Y = np.linspace(self.limit[0], self.limit[1], 2000)
        X, Y = np.meshgrid(X, Y)
        ax.plot_surface(
            X,
            Y,
            self.fun(X, Y),
            cmap="rainbow",
        )
        ax.scatter(
            self.x[:, 0], self.x[:, 1], self.fun(self.x[:, 0], self.x[:, 1]), c="r"
        )
        ger = ger_all
        while ger:
            self.update(ax)
            plt.title(f"迭代次数：{ger_all - ger + 1}")
            plt.pause(0.01)
            ger -= 1
        # plt.ioff()
        plt.clf()  # 清除之前的图像
        X = self.x[:, 0]
        Y = self.x[:, 1]
        X, Y = np.meshgrid(X, Y)
        ax.plot_surface(X, Y, self.fun(X, Y), cmap="rainbow")
        ax.scatter(X, Y, self.fun(X, Y), c="r")
        print(f"最优解: {self.fym}")
        print("最优解取值为: ", self.ym)

    def update(self, ax):
        self.fx = self.fun(self.x[:, 0], self.x[:, 1])  # 个体当前适应度
        for i in range(1, self.N):
            if self.fx[i] < self.fxm[i]:
                self.xm[i] = self.x[i]  # 更新个体最优位置
                self.fxm[i] = self.fx[i]  # 更新个体最优适应度

        if np.min(self.fxm) < self.fym:
            self.ym = self.xm[np.argmin(self.fxm)]  # 更新群体最优位置
            self.fym = np.min(self.fxm)  # 更新群体最优适应度

        self.v = (
            self.w * self.v
            + self.c1 * np.random.rand() * (self.xm - self.x)
            + self.c2 * np.random.rand() * (self.ym - self.x)
        )  # 更新速度

        # 边界速度处理
        self.v[self.v < self.vlimit[0]] = self.vlimit[0]
        self.v[self.v > self.vlimit[1]] = self.vlimit[1]

        # 边界位置处理
        self.x = self.x + self.v
        self.x[self.x < self.limit[0]] = self.limit[0]
        self.x[self.x > self.limit[1]] = self.limit[1]

        # 更新图像
        # plt.clf()  # 清除之前的图像
        # X = self.x[:, 0]
        # Y = self.x[:, 1]
        # X, Y = np.meshgrid(X, Y)
        # ax.plot_surface(X, Y, self.fun(X, Y), cmap="rainbow")
        # ax.scatter(X, Y, self.fun(X, Y), c="r")

    def fun(self, x, y):
        return (
            20
            + x**2
            + y**2
            - 10 * np.cos(2 * np.pi * x)
            - 10 * np.cos(2 * np.pi * y)
        )


if __name__ == "__main__":
    q = Q()
    # q.run(200)
    plt.show()
