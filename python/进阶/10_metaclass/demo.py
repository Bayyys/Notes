from typing import Any


class M(type):
    def __new__(cls, name, bases, attrs):
        print(name, bases, attrs)
        return type.__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        print(name, bases, attrs)
        return type.__init__(self, name, bases, attrs)

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        print(f"call 方法在生成实例时调用")
        return type.__call__(cls, *args, **kwds)


class A(metaclass=M):
    pass


print(f"定义实例")

o = A() # call 方法在生成实例时调用


# A = M("A", (), {})

# o = A()
