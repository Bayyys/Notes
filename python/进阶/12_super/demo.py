print(type(super))  # <class 'super'>

# 完整形式
# super(type[, object-or-type])


class A:
    def __init__(self, name) -> None:
        self.name = name


class B(A):
    def __init__(self, name) -> None:
        # super().__init__(name)    # 必须在__init__中使用, 会自动寻找父类, 以及该函数的第一个参数
        # super(B, self).__init__(name) # arg1: 决定MRO寻找位置, 参数对应的是MRO中的下一个类    arg2: 决定使用该对象是谁, 以及MRO
        A.__init__(self, name)
        self.age = 18


obj = B("a")
# 可以在其他位置使用
super(B, obj).__init__("b")
print(obj.name)  # b
