# 测试内置函数
class Built_In(object):
    def __init__(self) -> None:
        super().__init__()
    
        
    class A(object):
        def __init__(self) -> None:
            super().__init__()
            
        def absTest(self):
            """
            abs(x): 函数返回数字的绝对值. 参数可以是整数、浮点数或任何实现了 `__abs__()` 的对象。 如果参数是一个复数，则返回它的模。
            """
            # 整数, 浮点数
            print(abs(-1))    # 1
            print(abs(-1.1))    # 1.1
            # 复数
            print(abs(1+1j))    # 1.4142135623730951
        
        def aiterTest(self):
            """
            aiter(async_iterable): 返回 `asynchronous iterable` 的 `asynchronous iterator`. 相当于调用 `x.__aiter__()`.
            """
            pass
        
        def allTest(self):
            """
            all(iterable): 如果 `iterable` 的所有元素都为真值（或者 `iterable` 为空），返回 `True`. 相当于调用 `all(x) for x in iterable`.
            """
            pass

        def anyTest(self):
            """
            any(iterable): 如果 `iterable` 的任一元素为真值则返回 `True`. 如果 `iterable` 为空，返回 `False`. 相当于调用 `any(x) for x in iterable`.
            """
            list_1 = [0, 1, 2]
            list_2 = [0, False, None]
            print(any(list_1))    # True
            print(any(list_2))    # False
        
        def anextTest(self):
            """
            anext(asynchronous_iterator[, default]): 返回 `asynchronous iterator` 的下一个元素. 如果没有更多元素，则返回 `default`，如果没有提供 `default`，则引发 `StopAsyncIteration`.
            """
            pass
        
        def asciiTest(self):
            """
            ascii(object): 返回一个包含对象的可打印表示形式的字符串，用于表示值时，应该使用 `repr()` 或 `str()` 代替此函数.
            """
            str = "abc"
            print(ascii(str))    # 'abc'
            print(repr(str))    # 'abc'
            str = b'abc'
            print(ascii(str))    # b'abc'
            print(repr(str))    # b'abc'
            str = 'Pythön!'
            print(ascii(str))    # 'Pyth\xf6n!'
            print(repr(str))    # 'Pythön!'

    class B(object):

        def __init__(self) -> None:
            super().__init__()
        
        def binTest(self):
            """
            bin(x): 将一个整数转换为一个前缀为“0b”的二进制字符串。结果是一个有效的 Python 表达式。如果 x 不是 Python 的 int 对象，则必须定义返回整数的 `__index__()` 方法。
            """
            print(bin(3))    # 0b11
            print(bin(-10))    # -0b1010
            # 字符串控制是否显示前缀“0b”两种方式
            print(format(14, 'b'))    # 1110
            print(format(14, '#b'))    # 0b1110
            print(format(14, '0b'))    # 1110
            print(f'{14:#b}')    # 0b1110
        
        def boolTest(self):
            """
            class bool([x]): 返回一个布尔值，即一个 `True` 或 `False` 的值。 `x` 会被转换为一个布尔值，如果 `x` 为假或省略，则返回 `False`；否则返回 `True`
            """
            print(bool())    # False
            print(bool(0))    # False
            print(bool(1))    # True
            print(bool(2))    # True
            print(bool(-1))    # True
            print(bool(''))    # False
            print(bool('abc'))    # True
            print(bool([]))    # False
            print(bool([1, 2]))    # True
        
        def breakpointTest(self):
            """
            breakpoint(*args, **kws): 调用内置的 `breakpoint()` 函数。这是一个便利的别名，用于调试器支持。它的参数是相同的，返回值是 `None`.
            """
            pass
            
        def bytearrayTest(self):
            """
            class bytearray([source[, encoding[, errors]]]): 返回一个新的字节数组。如果没有给出参数，则返回一个长度为 0 的数组。
            """
            print(bytearray())    # bytearray(b'')
            print(bytearray(1))    # bytearray(b'\x00')
            print(bytearray([1, 2, 3]))    # bytearray(b'\x01\x02\x03')
            print(bytearray(b'abc'))    # bytearray(b'abc')
            print(bytearray('abc', 'utf-8'))    # bytearray(b'abc')
            print(bytearray('中文', 'utf-8'))    # bytearray(b'\xe4\xb8\xad\xe6\x96\x87')
            print(bytearray('中文', 'gbk'))    # bytearray(b'\xd6\xd0\xce\xc4')

        def bytesTest(self):
            """
            class bytes([source[, encoding[, errors]]]): 返回一个新的 bytes 对象，是一个不可变序列，包含范围为 0 <= x < 256 的整数。bytes 是 bytearray 的不可变版本 - 它有类似的方法和相同的索引和切片行为。
            """
            print(bytes())    # b''
            print(bytes(1))    # b'\x00'
            print(bytes([1, 2, 3]))    # b'\x01\x02\x03'

    class C(object):

        def __init__(self) -> None:
            super().__init__()
        
        def callableTest(self):
            """
            callable(object): 如果参数 `object` 是可调用的，则返回 `True`，否则返回 `False`. 如果返回 `True`，调用仍可能失败，但如果返回 `False`，则调用将肯定失败。
            """
            pass
    
        def chrTest(self):
            """
            chr(i): 返回 Unicode 码位为整数 `i` 的字符的字符串格式。例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。
            """
            print(chr(97))    # a
            print(chr(8364))    # €

        def classmethod(self):
            """
            @classmethod: 用于声明类方法，类方法的第一个参数为类对象，一般以 `cls` 作为第一个参数，类方法可以通过类对象、实例对象调用.
            """

            class ClassTest:
                @classmethod
                def classMethod(cls): ...

        def compileTest(self):
            """
            compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1): 将 `source` 编译为代码或 AST 对象。代码对象可以由 `exec()` 或 `eval()` 执行。`source` 可以是普通字符串，字节字符串或 AST 对象。
            """
            print(compile('a = 1', '', 'exec'))    # <code object <module> at 0x0000020E0F6F9C10, file "", line 1>
            print(compile('a = 1', '', 'exec', 0, True))    # <code object <module> at 0x0000020E0F6F9C10, file "", line 1>

        def complexTest(self):
            """
            complex([real[, imag]]): 返回一个值为 `real + imag * j` 的复数或转换一个字符串或数字为复数。如果第一个参数为字符串，则不需要指定第二个参数。第二个参数默认为 0.0。
            """
            print(complex(1, 2))    # (1+2j)
            print(complex(1))    # (1+0j)
            print(complex('1+2j'))    # (1+2j)
            print(complex('1'))    # (1+0j)
    
    class D:

        def __init__(self) -> None:
            super().__init__()
        
        def delattrTest(self):
            """
            delattr(object, name): 删除具有名称 `name` 的属性。例如，delattr(x, 'foobar') 等同于 del x.foobar。
            """
            pass
        
        def dictTest(self):
            """
            class dict(**kwarg): class dict(mapping, **kwarg): class dict(iterable, **kwarg): 返回一个新的字典。dict 是字典的构造器。
            """
            print(dict())   # {}
            print(dict(a=1, b=2))   # {'a': 1, 'b': 2}
            print(dict([('a', 1), ('b', 2)]))   # {'a': 1, 'b': 2}
        
        def dirTest(self):
            '''
            dir(object): 不带参数时，返回当前本地作用域中的名称列表。带参数时，返回参数的属性、方法列表。
            '''
            print(dir())    # ['self']
            print(dir([]))  # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
            print(dir({}))  # ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

        def divmodTest(self):
            '''
            divmod(a, b): 将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。对于混合操作数类型，适用双目运算符的规则。
            '''
            print(divmod(1, 2))    # (0, 1)
            print(divmod(2, 1))    # (2, 0)
            print(divmod(2, 1.0))    # (2.0, 0.0)
            print(divmod(2.0, 1))    # (2.0, 0.0)
            print(divmod(2.0, 1.0))    # (2.0, 0.0)
            print(divmod(2.0, 1.5))    # (1.0, 0.5)
    
    class E(object):

        def __init__(self) -> None:
            super().__init__()
        
        def enumerateTest(self):
            """
            enumerate(iterable, start=0): 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
            """
            print(enumerate(['a', 'b', 'c']))    # <enumerate object at 0x0000020E0F6F9F00>
            print(list(enumerate(['a', 'b', 'c'])))   # [(0, 'a'), (1, 'b'), (2, 'c')]
            print(enumerate(['a', 'b', 'c'], 1))    # <enumerate object at 0x0000020E0F6F9F00>
            print(list(enumerate(['a', 'b', 'c'], 1)))   # [(1, 'a'), (2, 'b'), (3, 'c')]
        
        def evalTest(self):
            """
            eval(expression, globals=None, locals=None): 将字符串作为表达式来求值，并返回结果。
            """
            print(eval('1 + 1'))    # 2
            print(eval('1 + 1', {'__builtins__': None}, {}))    # 2

        def execTest(self):
            """
            exec(object[, globals[, locals]]): 动态执行 Python 代码。object 必须是字符串或代码对象。如果是字符串，该字符串会先被解析为一组 Python 语句，然后在执行（除非发生语法错误）。[1] 如果是代码对象，它只是被简单地执行。在这两种情况下，exec() 的返回值都将为 None。
            """
            print(exec('print(1 + 1)'))    # 2
            print(exec('print(1 + 1)', {'__builtins__': None}, {}))    # 2

    class F(object):

        def __init__(self) -> None:
            super().__init__()
        
        def filterTest(self):
            """
            filter(function, iterable): 构造一个迭代器，其中包含 iterable 中的那些元素，其函数 function 返回 true。如果未指定 function，则将返回可迭代对象中为真值的元素。
            """
            print(filter(lambda x: x > 0, [1, -1, 2, -2]))  # <filter object at 0x000001EDB4CD7580>
        
        def floatTest(self):
            """
            class float([x]): 返回一个浮点数对象构造器。如果没有参数，则返回 0.0。
            """
            print(float())  # 0.0
            print(float(1))  # 1.0
            print(float(1.0))  # 1.0
            print(float('1'))  # 1.0
            print(float('1.0'))  # 1.0
            print(float('1.0e-3'))  # 0.001
            print(float('1.0e3'))  # 1000.0
            print(float('1.0e+3'))  # 1000.0
            print(float('+1.23'))   # 1.23
            print(float('   -12345\n')) # -12345.0
            print(float('+1E6'))    # 1000000.0
            print(float('-Infinity'))   # -inf


if __name__ == "__main__":
    # a = Built_In.A()
    # a.asciiTest()
    # b = Built_In.B()
    # b.boolTest()
    # c = Built_In.C()
    # c.compileTest()
    # d = Built_In.D()
    # d.dirTest()
    # e = Built_In.E()
    # e.execTest()
    f = Built_In.F()
    f.floatTest()