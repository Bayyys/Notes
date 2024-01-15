class A:
    @staticmethod
    def f(x):
        print(x)

    @classmethod
    def g(cls, x):
        print(cls, x)


A.f(1)  # 1
a = A()
a.f(1)  # 1

A.g(1)  # <class '__main__.A'> 1
a.g(1)  # <class '__main__.A'> 1

""" f """
print(A.__dict__["f"])  # <staticmethod(<function A.f at 0x0000013FBED64CC0>)>
