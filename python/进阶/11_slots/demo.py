class A:
    __slots__ = ("name", "age")


o = A()
o.name = "a"
o.age = 18
o.error = "error"  # AttributeError: 'A' object has no attribute 'error'
