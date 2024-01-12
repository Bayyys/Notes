class Name:
    def __get__(self, obj, objtype):
        print("__get__")
        return "Bay"


class A:
    name = Name()


class B:
    def __init__(self) -> None:
        self.name = Name()


class C:
    name = Name()


"""
a.b 会调用 bytecode: STORE_ATTR ()
print(a.b) 会调用 bytecode: LOAD_ATTR
"""

obj = A()
print(obj.name)  # Bay
print(A.name)  # Bay
obj2 = B()
print(obj2.name)  # <__main__.Name object at 0x00000146BAAC2150>
obj3 = C()
obj3.name = "bayyy"
print(obj3.name)  # bayyy
Name.__set__ = lambda x, y, z: None
print(obj3.name)  # Bay
