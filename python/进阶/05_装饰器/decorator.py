# 实际执行的是装饰器函数
def dec(f):
    return 1


@dec
def my_sleep(x):
    return x * 2


# print(dec(double))    # 1

# 实际使用
import time


def time_log(f):
    def log(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        print("time: ", time.time() - start)
        return res

    return log


@time_log
def my_sleep(x):
    time.sleep(x)
    print("excuted")


# my_sleep(2)  # 等效于执行 time_log(my_sleep)(2)


# 带参数的装饰器
def time_log_with_print(text):
    print("text: ", text)

    def inner(f):
        def log(*args, **kwargs):
            start = time.time()
            res = f(*args, **kwargs)
            print("time: ", time.time() - start)
            return res

        return log

    return inner


# @time_log_with_print(
#     "hello world"
# )  # 等效于执行 time_log_with_print("hello world")(my_sleep)
def my_sleep(x):
    time.sleep(x)


# my_sleep(2)  # 等效于执行 time_log_with_print("hello world")(my_sleep)(2)


# 类装饰器
class TimeLog:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        start = time.time()
        res = self.f(*args, **kwargs)
        print("time: ", time.time() - start)
        return res


@TimeLog
def my_sleep_class(x):
    time.sleep(x)
    return x


# print(my_sleep_class(2))  # 等效于执行 TimeLog(my_sleep)(2)


# 带参数的类装饰器
class TimeLog:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.prefix)
            start = time.time()
            res = func(*args, **kwargs)
            print("time: ", time.time() - start)
            return res

        return wrapper


@TimeLog("hello world")
def my_sleep_class(x):
    time.sleep(x)
    return x


# print(my_sleep_class(2))  # 等效于执行 TimeLog(my_sleep)(2)


# 类的装饰器
def add_str(cls):
    def __str__(self):
        return str(self.__dict__)

    cls.__str__ = __str__
    return cls


# @add_str
class MyObject:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


# 等价于
MyObject = add_str(MyObject)

obj = MyObject(1, 2)
# print(obj)  # {'a': 1, 'b': 2}


# 装饰器的类封装: 如何将装饰器定义在类内，并且装饰该类的对象？
class MyDecorators:
    def log_function(func):
        def wrapper(*args, **kwargs):
            print(f"function start")
            print(f"args: {args}, kwargs: {kwargs}")
            print("log_function")
            res = func(*args, **kwargs)
            print(f"function end")
            return res

        return wrapper

    @log_function
    def fib(self, n):
        if n < 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


d = MyDecorators()
print(d.fib(3))
