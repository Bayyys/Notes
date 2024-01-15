class A:
    def say(self):
        print("A")


class B:
    def say(self):
        print("B")


class C(A):
    pass


class M(B, C):
    pass


print(M.__mro__)
print(M.mro())
