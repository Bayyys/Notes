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
        
if __name__ == "__main__":
    # a = Built_In.A()
    # a.asciiTest()
    # b = Built_In.B()
    # b.boolTest()
    # c = Built_In.C()
    # c.compileTest()
    d = Built_In.D()