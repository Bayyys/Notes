class A:
    def __init__(self) -> None:
        self.__v = 0

    def print_v(self):
        print(self.__v)


obj = A()
obj.print_v()  # 0

""" 实现机制 """
# 编译期间，解释器会将所有的私有变量名都改为 _类名__变量名
# obj._A__v
print(obj._A__v)  # 0

# 故不支持 setattr(obj, "__v", 1)   不会变成私有变量 
