# 闭包的概念
def outer(x):
    def inner(y):
        return x + y

    return inner


print(outer(1)(2))  # 3


# 闭包无法修改外部函数的局部变量
def outer2():
    x = 0

    def inner():
        x += 1
        return x

    print("outer x before call inner: ", x)
    inner()
    print("outer x after call inner: ", x)


# outer2()  # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value


# 循环中不包含域的概念
flist = []
for i in range(3):

    def makefun(i):
        def func(x):
            return x * i

        return func

    flist.append(makefun(i))

for f in flist:
    print(f(2))  # 4 4 4
