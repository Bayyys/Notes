## 1.1 A

### 1.1.1 abs(x)

> 返回一个数的绝对值。 参数可以是整数、浮点数或任何实现了 `__abs__()` 的对象。 如果参数是一个复数，则返回它的模。

```python
def absTest(self):
    """
    abs(x) 函数返回数字的绝对值. 参数可以是整数、浮点数或任何实现了 `__abs__()` 的对象。 如果参数是一个复数，则返回它的模。
	"""
    # 整数, 浮点数
    print(abs(-1))    # 1
    print(abs(-1.1))    # 1.1
    # 复数
    print(abs(1+1j))    # 1.4142135623730951
```

### 1.1.2 aiter(async_iterable)

> 返回 `asynchronous iterable` 的 `asynchronous iterator`. 相当于调用 `x.__aiter__()`.
>
> 注意：与 `iter()` 不同，`aiter()` 没有两个参数的版本。
>
> > 3.10 新版本

```python
def aiterTest(self):
    """
    aiter(async_iterable) 函数返回 `asynchronous iterable` 的 `asynchronous iterator`. 相当于调用 `x.__aiter__()`.
    注意：与 `iter()` 不同，`aiter()` 没有两个参数的版本。
    """
    # 3.10 新版本
    pass
```

### 1.1.3 all(iterable)

> 如果 iterable 的所有元素均为真值（或可迭代对象为空）则返回 True
>
> 等价于:
>
> ```python
> def all(iterable):
> for element in iterable:
>     if not element:
>         return False
> return True
> ```

- 等价于:

  - ```python
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True
    ```

```python
def allTest(self):
    """
    all(iterable): 如果 `iterable` 的所有元素都为真值（或者 `iterable` 为空），返回 `True`. 相当于调用 `all(x) for x in iterable`.
    """
    pass
```

### 1.1.4 any(iterable)

> 如果 iterable 的任一元素为真值则返回 True。 如果可迭代对象为空，返回 False.

- 等价于:

  - ```python
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False
    ```

```python
def anyTest(self):
    """
    any(iterable): 如果 `iterable` 的任一元素为真值则返回 `True`. 如果 `iterable` 为空，返回 `False`. 相当于调用 `any(x) for x in iterable`.
    """
    list_1 = [0, 1, 2]
    list_2 = [0, False, None]
    print(any(list_1))    # True
    print(any(list_2))    # False
```

### 1.1.5 anext(async_iterator[, default])

> 当进入 await 状态时，从给定 asynchronous iterator 返回下一数据项，迭代完毕则返回 default。

- 内置函数 `next()` 的异步版本. 
  - 当进入await状态时，从给定asynchronous iterator返回下一项数据, 迭代完毕则返回 `default` (如果提供了的话), 否则引发 `StopAsyncIteration`.
- 相当于调用 `x.__anext__()`.
  - 调用 `async_iterator` 的 `__anext__()` 方法，返回一个 `awaitable`。等待返回迭代器的下一个值。若有给出 `default`，则在迭代完毕后会返回给出的值，否则会触发 `StopAsyncIteration`。

```python
def anextTest(self):
    """
    anext(asynchronous_iterator[, default]): 返回 `asynchronous iterator` 的下一个元素. 如果没有更多元素，则返回 `default`，如果没有提供 `default`，则引发 `StopAsyncIteration`.
    """
    pass
```

### 1.1.6 ascii(object)

> 与 `repr()` 类似，返回一个字符串，表示对象的可打印形式，但在 repr() 返回的字符串中，非 ASCII 字符会用 \x、\u 和 \U 进行转义。
>
> 生成的字符串类似于 Python 2 中 repr() 的返回结果。

```python
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
```

## 1.2 B

### 1.2.1 bin(x)

> 将整数转换为前缀为“0b”的二进制字符串。 结果是一个有效的 Python 表达式。 如果 x 不是 Python int 对象，则它必须定义一个返回整数的 `__index__()` 方法。

```python
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
```

### 1.2.2 class bool([x])

> 返回布尔值，True 或 False。如果 x 为 False 或省略，则返回 False；否则返回 True
>
> bool 类是 int 的子类。它不能再被继承。它唯一的实例就是 False 和 True。

```python
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
```

### 1.2.3 breakpoint(*args, **kws)

> 该函数将您置于调用站点的调试器中。具体来说，它调用 `sys.breakpointhook()`，直接传递参数和信息。默认情况下，`sys.breakpointhook()` 调用 `pdb.set_trace()` 时不需要任何参数。
>
> 可以将`sys.breakpointhook()`设置为其他函数，`breakpoint()` 将自动调用该函数，从而允许您进入所选择的调试器。如果`sys.breakpointhook()`不可访问，此函数将引发RuntimeError。
>
> 默认情况下，breakpoint()的行为可以通过PYTHONBREAKPOINT环境变量来改变。

```python
def breakpointTest(self):
    """
    breakpoint(*args, **kws): 调用内置的 `breakpoint()` 函数。这是一个便利的别名，用于调试器支持。它的参数是相同的，返回值是 `None`.
    """
    pass
```

### 1.2.4 bytearray([source[, encoding[, errors]]])

> 返回一个新的 bytes 数组
>
> 可选形参 source 可以用不同的方式来初始化数组：
>
> - 如果是一个 string，您必须提供 encoding 参数（errors 参数仍是可选的）；bytearray() 会使用 str.encode() 方法来将 string 转变成 bytes。
> - 如果是一个 integer，会初始化大小为该数字的数组，并使用 null 字节填充。
> - 如果是一个遵循 缓冲区接口 的对象，该对象的只读缓冲区将被用来初始化字节数组。
> - 如果是一个 iterable 可迭代对象，它的元素的范围必须是 0 <= x < 256 的整数，它会被用作数组的初始内容。
>
> 如果没有实参，则创建大小为 0 的数组。

```python
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
```

### 1.2.5 bytes([source[, encoding[, errors]]])

> 返回一个新的“bytes”对象，这是一个不可变序列，包含范围为 0 <= x < 256 的整数。
>
> `bytes()` 是 `bytearray()` 的不可变版本. 它有同样的非字符串参数，但是 `bytes()` 会返回一个不可变的 bytes 对象而不是可变的 bytearray 对象。

```python
def bytesTest(self):
    """
    class bytes([source[, encoding[, errors]]]): 返回一个新的 bytes 对象，是一个不可变序列，包含范围为 0 <= x < 256 的整数。bytes 是 bytearray 的不可变版本 - 它有类似的方法和相同的索引和切片行为。
    """
    print(bytes())    # b''
    print(bytes(1))    # b'\x00'
    print(bytes([1, 2, 3]))    # b'\x01\x02\x03'
```

## 1.3 C

### 1.3.1 callable(object)

> 如果参数 object 是可调用的就返回 True，否则返回 False。 如果返回 True，调用仍可能失败，但如果返回 False，则调用 object 将肯定不会成功。 
>
> 请注意类是可调用的（调用类将返回一个新的实例）；如果实例所属的类有 __call__() 则它就是可调用的。

```python
def callableTest(self):
    """
    callable(object): 如果参数 `object` 是可调用的，则返回 `True`，否则返回 `False`. 如果返回 `True`，调用仍可能失败，但如果返回 `False`，则调用将肯定失败。
    """
    pass
```

### 1.3.2 chr(i)

> 返回 Unicode 码位为整数 i 的字符的字符串格式。例如，chr(97) 返回字符串 `a`，chr(8364) 返回字符串 `€`。这是 ord() 的逆函数。
>
> 实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。如果 i 超过这个范围，会触发 `ValueError` 异常。

```python
def chrTest(self):
    """
    chr(i): 返回 Unicode 码位为整数 `i` 的字符的字符串格式。例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。
    """
    print(chr(97))    # a
    print(chr(8364))    # €
```

### 1.3.3 @classmethod

> 把一个方法封装成类方法。
>
> 类方法隐含的第一个参数就是类，就像实例方法接收实例作为参数一样。要声明一个类方法，按惯例请使用以下方案：
>
> ```python
> class C:
>  @classmethod
>  def f(cls, arg1, arg2, ...): ...
> ```
>
> 类方法的调用可以在类上进行 (例如 C.f()) 也可以在实例上进行 (例如 C().f())。 其所属类以外的类实例会被忽略。 如果类方法在其所属类的派生类上调用，则该派生类对象会被作为隐含的第一个参数被传入。
>
> > 版本变化：
> >
> > - 在 3.9 版更改: 类方法现在可以包装其他 描述器 例如 property()。
> >
> > - 类方法现在继承了方法的属性（`__module__`、`__name__`、`__qualname__`、`__doc__` 和 `__annotations__`），并拥有一个新的`__wrapped__` 属性。
> >
> > - 类方法不能再包装其他描述符，如property()。

```python

```

### 1.3.4 compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

> 将 source 编译成代码或 AST 对象。代码对象可以被 `exec()` 或 `eval()` 执行。source 可以是常规的字符串、字节字符串，或者 AST 对象。
>
> filename 实参需要是代码读取的文件名；如果代码不需要从文件中读取，可以传入一些可辨识的值（经常会使用 '<string>'）。
>
> mode 实参指定了编译代码必须用的模式。如果 source 是语句序列，可以是 'exec'；如果是单一表达式，可以是 'eval'；如果是单个交互式语句，可以是 'single'。（在最后一种情况下，如果表达式执行结果不是 None 将会被打印出来。）
>
> 可选参数 `flags` 和 `dont_inherit` 控制应当激活哪个 `编译器选项` 以及应当允许哪个 `future` 特性。 
>
> - 如果两者都未提供 (或都为零) 则代码会应用与调用 `compile()` 的代码相同的旗标来编译。
> - 如果给出了 `flags` 参数而未给出 `dont_inherit` (或者为零) 则会在无论如何都将被使用的旗标之外还会额外使用 `flags` 参数所指定的编译器选项和 `future` 语句。
> - 如果 `dont_inherit` 为非零整数，则只使用 `flags` 参数 -- 外围代码中的旗标 (future 特性和编译器选项) 会被忽略。
>
> optimize 实参指定编译器的优化级别；默认值 -1 选择与解释器的 -O 选项相同的优化级别。显式级别为 0 （没有优化；`__debug__` 为真）、1 （断言被删除， `__debug__` 为假）或 2 （文档字符串也被删除）
>
> - 备注: 在 'single' 或 'eval' 模式编译多行代码字符串时，输入必须以至少一个换行符结尾。 这使 code 模块更容易检测语句的完整性。
>
> > 版本更改：
> >
> > 在 3.2 版更改: Windows 和 Mac 的换行符均可使用。而且在 'exec' 模式下的输入不必再以换行符结尾了。另增加了 optimize 参数。
> >
> > 在 3.5 版更改: 之前 source 中包含 null 字节的话会触发 TypeError 异常。
> >
> > 3.8 新版功能: `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` 现在可在旗标中传入以启用对最高层级 `await`, `async for` 和 `async with` 的支持。

```python
def compileTest(self):
    """
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1): 将 `source` 编译为代码或 AST 对象。代码对象可以由 `exec()` 或 `eval()` 执行。`source` 可以是普通字符串，字节字符串或 AST 对象。
    """
    print(compile('a = 1', '', 'exec'))    # <code object <module> at 0x0000020E0F6F9C10, file "", line 1>
    print(compile('a = 1', '', 'exec', 0, True))    # <code object <module> at 0x0000020E0F6F9C10, file "", line 1>
```

### 1.3.5 complex([real[, imag]])

> 返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。
>
> > 如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。
> >
> > 第二个形参不能是字符串。
> >
> > 每个实参都可以是任意的数值类型（包括复数）。
> >
> > 如果省略了 imag，则默认值为零，构造函数会像 int 和 float 一样进行数值转换。
> >
> > 如果两个实参都省略，则返回 0j。
>
> - 备注: 当从字符串转换时，字符串在 + 或 - 的周围必须不能有空格。例如 complex('1+2j') 是合法的，但 complex('1 + 2j') 会触发 ValueError 异常。
>
> > 版本更改：
> >
> > 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。
> >
> > 在 3.8 版更改: 如果没有定义`__complex__()`和`__float__()`，则回退到`__index__()`。

```python
def complexTest(self):
    """
    complex([real[, imag]]): 返回一个值为 `real + imag * j` 的复数或转换一个字符串或数字为复数。如果第一个参数为字符串，则不需要指定第二个参数。第二个参数默认为 0.0。
    """
    print(complex(1, 2))    # (1+2j)
    print(complex(1))    # (1+0j)
    print(complex('1+2j'))    # (1+2j)
    print(complex('1'))    # (1+0j)
```

## 1.4 D

### 1.4.1 delattr(object, name)

> 参数是一个对象和一个字符串, 该字符串必须是对象属性之一的名称, 如果对象允许，该函数将删除指定的属性。与 `setattr()` 相呼应
>
> - `delattr(x, 'foobar') `相当于 `del x.foobar`

### 1.4.2 class dict(iterable, **kwarg)

> 创建一个新的字典。`dict` 对象是一个字典类。
>
> ```python
> class dict(**kwarg)
> class dict(mapping, **kwarg)
>      class dict(iterable, **kwarg)
> ```

```python
def dictTest(self):
    """
    class dict(**kwarg): class dict(mapping, **kwarg): class dict(iterable, **kwarg): 返回一个新的字典。dict 是字典的构造器。
    """
    print(dict())
    print(dict(a=1, b=2))
    print(dict([('a', 1), ('b', 2)]))
```

### 1.4.3 dir(object)

> 如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表(返回的列表按字母表排序)。
>
> - 如果对象有一个名为 `__dir__()` 的方法，那么该方法将被调用，并且必须返回一个属性列表。这允许实现自定义`___getattr__()` 或 `__getattribute__()` 函数的对象能够自定义 `dir()` 来报告它们的属性。
>
> - 如果对象未提供 `__dir__()`方法，该函数会尽量从对象的 `__dict__` 属性和其类型对象中收集信息。得到的列表不一定是完整，如果对象带有自定义 `__getattr__()` 方法时，结果可能不准确。
>
> 默认的 `dir()` 机制对不同类型的对象行为不同，它会试图返回最相关而不是最全的信息：
>
> - 如果对象是模块对象，则列表包含模块的属性名称。
> - 如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。
> - 否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。

```python
def dirTest(self):
    '''
    dir(object): 不带参数时，返回当前本地作用域中的名称列表。带参数时，返回参数的属性、方法列表。
    '''
    print(dir())    # ['self']
    print(dir([]))  # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    print(dir({}))  # ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

### 1.4.4 divmod(a, b)

> 以两个（非复数）数字为参数，在作整数除法时，返回商和余数。若操作数为混合类型，则适用二进制算术运算符的规则。对于整数而言，结果与 (a // b, a % b) 相同。对于浮点数则结果为``(q, a % b)``，其中 q 通常为 math.floor(a / b)，但可能比它小 1。在任何情况下，q * b + a % b 都非常接近 a，如果 a % b 非零，则结果符号与 b 相同，并且 0 <= abs(a % b) < abs(b)。

```python
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
```

## 1.5 E

### 1.5.1 enumerate(iterable, start=0)

> 返回一个枚举对象。iterable 必须是一个序列，或 `iterator`，或其他支持迭代的对象。` enumerate()` 返回的迭代器的 `__next__()` 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 `iterable` 获得的值。

```python
def enumerateTest(self):
    """
    enumerate(iterable, start=0): 返回一个枚举对象。iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。enumerate() 返回的迭代器的 __next__() 方法返回一个元组，里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。
    """
    print(enumerate(['a', 'b', 'c']))    # <enumerate object at 0x0000020E0F6F9F00>
    print(list(enumerate(['a', 'b', 'c'])))   # [(0, 'a'), (1, 'b'), (2, 'c')]
    print(enumerate(['a', 'b', 'c'], 1))    # <enumerate object at 0x0000020E0F6F9F00>
    print(list(enumerate(['a', 'b', 'c'], 1)))   # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 1.5.2 eval(expression, globals=None, locals=None)

> 实参是一个字符串，以及可选的 globals 和 locals。globals 实参必须是一个字典。locals 可以是任何映射对象。
>
> 返回值就是表达式的求值结果。 语法错误将作为异常被报告。 

```python
def evalTest(self):
    """
    eval(expression, globals=None, locals=None): 将字符串作为表达式来求值，并返回结果。
    """
    print(eval('1 + 1'))    # 2
    print(eval('1 + 1', {'__builtins__': None}, {}))    # 2
```

### 1.5.3 exec(object, globals=None, locals=None, /, *, closure=None)

> 这个函数支持动态执行 Python 代码。
>
> - nobject 必须是字符串或者代码对象。 
>   - 如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。
>   - 如果是代码对象，它将被直接执行。 
> - 在任何情况下，被执行的代码都应当是有效的文件输入

```python
def execTest(self):
    """
	exec(object[, globals[, locals]]): 动态执行 Python 代码。object 必须是字符串或代码对象。如果是字符串，该字符串会先被解析为一组 Python 语句，然后在执行（除非发生语法错误）。[1] 如果是代码对象，它只是被简单地执行。在这两种情况下，exec() 的返回值都将为 None。
	"""
    print(exec('print(1 + 1)'))    # 2
    print(exec('print(1 + 1)', {'__builtins__': None}, {}))    # 2
```

## 1.6 F

### 1.6.1 filter(function, iterable)

> 从 iterable 的那些 function 为 true 的元素构造一个迭代器。 iterable 可以是序列、支持迭代的容器或迭代器。 如果 function 为 None，则假定为恒等函数，即移除 iterable 中所有为 false 的元素。
>
> - filter(function, iterable) 相当于一个生成器表达式，当 function 不是 None 的时候为 `(item for item in iterable if function(item))`；function 是 None 的时候为` (item for item in iterable if item) `。

```python
def filterTest(object):
    """
    filter(function, iterable): 构造一个迭代器，其中包含 iterable 中的那些元素，其函数 function 返回 true。如果未指定 function，则将返回可迭代对象中为真值的元素。
    """
    print(filter(lambda x: x > 0, [1, -1, 2, -2]))  # <filter object at 0x000001EDB4CD7580>
```

### 1.6.2 class float(x=0.0)

> 返回从数字或字符串 x 生成的浮点数。
>
> - 如果参数是字符串，则它应包含一个十进制数，可以选择在前面加一个符号，也可以选择嵌入空格。 可选符号可以是“+”或“-”； “+”号对产生的值没有影响。 参数也可以是表示 NaN（非数字）或正无穷大或负无穷大的字符串。 更准确地说，在删除前导和尾随空白字符后，输入必须符合以下语法中的 floatvalue 生成规则：
>
>   - ```python
>     sign        ::=  "+" | "-"
>     infinity    ::=  "Infinity" | "inf"
>     nan         ::=  "nan"
>     digitpart   ::=  digit (["_"] digit)*
>     number      ::=  [digitpart] "." digitpart | digitpart ["."]
>     exponent    ::=  ("e" | "E") ["+" | "-"] digitpart
>     floatnumber ::=  number [exponent]
>     floatvalue  ::=  [sign] (floatnumber | infinity | nan)
>     ```
>
> - 如果实参是整数或浮点数，则返回具有相同值（在 Python 浮点精度范围内）的浮点数。如果实参在 Python 浮点精度范围外，则会触发 OverflowError。
>
>   - 对于一般的 Python 对象 x，float(x) 委托给 `x.__float__()`。 如果` __float__() `未定义，则返回到` __index__()`。
>
> - 如果没有实参，则返回 0.0 
>
> - 版本更新：
>
>   - 在 3.6 版更改: 您可以使用下划线将代码文字中的数字进行分组。
>   - 在 3.7 版更改: x 现在只能作为位置参数。
>   - 在 3.8 版更改: 如果` __float__() `未定义，则返回到` __index__()`。

```python
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
```

### 1.6.3 format(value, format_spec='')

> 将 value 转换为“格式化后”的形式，格式由 `format_spec` 进行控制。`format_spec` 的解释方式取决于 value 参数的类型；但大多数内置类型使用一种标准的格式化语法： 格式规格迷你语言。
>
> 默认的 format_spec 是一个空字符串，它通常给出与调用 str(value) 相同的结果。
>
> 在 3.4 版更改: 当 format_spec 不是空字符串时， object().__format__(format_spec) 会触发 TypeError。

### 1.6.4 class frozenset(iterable=set())

> 返回一个新的 frozenset 对象，它包含可选参数 iterable 中的元素。 frozenset 是一个内置的类。有关此类的文档，请参阅 frozenset 和 集合类型 --- set, frozenset。

## 1.7 G

### 1.7.1 getattr(object, name[, default])

> 返回对象的命名属性的值。 名称必须是字符串。 如果字符串是对象属性之一的名称，则结果是该属性的值。 例如，getattr(x, 'foobar') 相当于 x.foobar。 如果指定的属性不存在，则返回默认值（如果提供），否则引发 AttributeError。
>
> - 备注: 由于 `私有名称混合` 发生在编译时，因此必须 `手动混合私有属性`（以两个下划线打头的属性）名称以使使用 getattr() 来提取它。

### 1.7.2 globals()

> 返回实现当前模块命名空间的字典。对于函数内的代码，这是在定义函数时设置的，无论函数在哪里被调用都保持不变。

## 1.8 H

### 1.8.1 hasattr(object, name)

> 该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。
>
> - 此功能是通过调用 `getattr(object, name)` 看是否有 `AttributeError` 异常来实现的。

### 1.8.2 hash(object)

> 返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。
>
> - 备注: 如果对象实现了自己的 __hash__() 方法，请注意，hash() 根据机器的字长来截断返回值。另请参阅 __hash__()。

### 1.8.3 help([request])

> 启动内置的帮助系统（此函数主要在交互式中使用）。如果没有实参，解释器控制台里会启动交互式帮助系统。如果实参是一个字符串，则在模块、函数、类、方法、关键字或文档主题中搜索该字符串，并在控制台上打印帮助信息。如果实参是其他任意对象，则会生成该对象的帮助页。
>
> - 注意: 如果在调用 help() 时，目标函数的形参列表中存在斜杠（/），则意味着斜杠之前的参数只能是位置参数。

### 1.8.4 hex(x)

> 将整数转换为以“0x”为前缀的小写十六进制字符串。如果x不是Python int对象，它必须定义一个返回整数的`__index__()`方法。

## 1.9 I

### 1.9.1 id(object)

> 返回对象的“标识值”。该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。两个生命期不重叠的对象可能具有相同的 id() 值。

### 1.9.2 input([prompt])

> 如果存在 `prompt` 实参，则将其写入标准输出，末尾不带换行符。接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。当读取到 `EOF `时，则触发 `EOFError`
>
> - 如果加载了 `readline` 模块，input() 将使用它来提供复杂的行编辑和历史记录功能。

### 1.9.3 class int(x, [base=10])

> 返回一个由数字或字符串x构造的整数对象，如果没有给出参数则返回0。
>
> - 根据函数定义：
>
>   - 如果x定义`__int__ ()`, `int (x)`返回`x.__int__()`
>
>   - 如果x定义了`__index__()`，它返回`x.__index__()`
>
>   - 如果x定义了`__trunc__()`，它返回`x.__trunc__()`
>
>   - 对于浮点数，它会向零截断
>
> - 如果x不是数字或者给定了基数，则x必须是一个字符串、bytes或bytearray实例，表示基数形式的整数。字符串的前面可以有+或-(中间没有空格)，可以有前导零，可以用空格包围，也可以在数字之间有单个下划线。
> - 以n为基数的整数字符串包含数字，每个数字表示从0到n-1的值。值0—9可以用任何Unicode十进制数字表示。值10—35可以用a到z(或a到z)表示。默认基数是10。允许的底数是0和2——36。基数为2、-8和-16的字符串可以选择性地以0b/ 0b、00 / 0o或0x/ 0x作为前缀，就像代码中的整数字面值一样。对于基数0，字符串的解释方式与代码中的整数字面值类似，因为实际的基数是由前缀确定的2、8、10或16。基数0也不允许前导零:int('010'， 0)是不合法的，而int('010')和int('010'， 8)是合法的。

### 1.9.4 isinstance(object, classinfo)

> 如果object参数是`classinfo`参数或其(直接、间接或虚拟)子类的实例，则返回True。如果object不是给定类型的对象，则该函数始终返回False。如果`classinfo`是类型对象的元组(或递归地，其他类似的元组)或多个类型的联合元组，则如果object是任何类型的实例，则返回True。如果`classinfo`不是类型或由类型和此类元组组成的元组，则会引发`TypeError`异常。如果先前的检查成功，则可能不会引发无效类型的`TypeError`。

### 1.9.5 issubclass(class, classinfo)

> 如果 class 是 `classinfo` 的子类（直接、间接或 虚的 ），则返回 True。类将视为自己的子类。`classinfo `可为类对象的元组（或递归地，其他这样的元组）或 union 类型，这时如果 class 是 `classinfo` 中任何条目的子类，则返回 True 。任何其他情况都会触发 `TypeError` 异常。

### 1.9.6 iter(object[, sentinel])

> 返回一个` iterator` 对象。根据是否存在第二个实参，第一个实参的解释是非常不同的。如果没有第二个实参，`object` 必须是支持` iterable `协议（有 `__iter__() `方法）的集合对象，或必须支持序列协议（有 `__getitem__()` 方法，且数字参数从 0 开始）。如果它不支持这些协议，会触发 `TypeError`。如果有第二个实参 `sentinel`，那么 `object` 必须是可调用的对象。这种情况下生成的迭代器，每次迭代调用它的 `__next__()` 方法时都会不带实参地调用 object；如果返回的结果是 `sentinel `则触发 `StopIteration`，否则返回调用结果。

## 1.10 L

### 1.10.1 len(s)

> 返回对象的长度（元素个数）。实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。

### 1.10.2 class list([iterable])

> 虽然被称为函数，list 实际上是一种可变序列类型。

### 1.10.3 locals()

> 更新并返回表示当前本地符号表的字典。 在函数代码块但不是类代码块中调用 locals() 时将返回自由变量。 请注意在模块层级上，locals() 和 globals() 是同一个字典
>
> - 备注: 不要更改此字典的内容；更改不会影响解释器使用的局部变量或自由变量的值。

## 1.11 M

### 1.11.1 map(function, iterable, *iterables)

> 返回一个迭代器，将函数应用于`iterable`的每一项，从而产生结果。如果传递了额外的可迭代对象参数，则函数必须接受相同数量的参数，并并行应用于所有可迭代对象中的项。对于多个可迭代对象，迭代器在最短的可迭代对象耗尽时停止。

### 1.11.2 max(iterable, *, key=None)

> 返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。

### 1.11.3 class memoryview(object)

> 返回由给定实参创建的“内存视图”对象。有关详细信息，请参阅 内存视图。

### 1.11.4 min(iterable, *, default, key=None)

> 返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。

## 1.12 N

### 1.12.1 next(iterator[, default])

> 通过调用 iterator 的 __next__() 方法获取下一个元素。如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。

## 1.13 O

### 1.13.1 class object

> 返回一个不带特征的新对象。object 是所有类的基类。它带有所有 Python 类实例均通用的方法。本函数不接受任何参数。
>
> - 备注: 由于 object 没有 __dict__，因此无法将任意属性赋给 object 的实例。

### 1.13.2 oct(x)

> 将整数转换为以“0”为前缀的八进制字符串。结果是一个有效的Python表达式。如果x不是Python int对象，它必须定义一个返回整数的`__index__()`方法。例如:

### 1.13.3 open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

> 打开 file 并返回对应的 file object。 如果该文件不能被打开，则引发 `OSError`。 
>
> file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者相对当前工作目录的路径），也可以是要封装文件对应的整数类型文件描述符。（如果给出的是文件描述符，则当返回的 I/O 对象关闭时它也会关闭，除非将 closefd 设为 False 。）
>
> | 字符  | 含意                                       |
> | :---- | :----------------------------------------- |
> | `'r'` | 读取（默认）                               |
> | `'w'` | 写入，并先截断文件                         |
> | `'x'` | 排它性创建，如果文件已存在则失败           |
> | `'a'` | 打开文件用于写入，如果文件存在则在末尾追加 |
> | `'b'` | 二进制模式                                 |
> | `'t'` | 文本模式（默认）                           |
> | `'+'` | 打开用于更新（读取与写入）                 |
>
> - errirs: 
>   - 如果存在编码错误，`'strict'` 会引发 `ValueError异常。 默认值 `None` 具有相同的效果。
>   - `'ignore'` 忽略错误。请注意，忽略编码错误可能会导致数据丢失。
>   - `'replace'` 会将替换标记（例如 `'?'` ）插入有错误数据的地方。
>   - `'surrogateescape'` 将把任何不正确的字节表示为 U+DC80 至 U+DCFF 范围内的下方替代码位。 当在写入数据时使用 `surrogateescape` 错误处理句柄时这些替代码位会被转回到相同的字节。 这适用于处理具有未知编码格式的文件。
>   - 只有在写入文件时才支持 `'xmlcharrefreplace'`。编码不支持的字符将替换为相应的XML字符引用 `&#nnn;`。
>   - `'backslashreplace'` 用Python的反向转义序列替换格式错误的数据。
>   - `'namereplace'` （也只在编写时支持）用 `\N{...}` 转义序列替换不支持的字符。
> - newline:
>   - 从流中读取输入时，如果 newline 为 None，则启用通用换行模式。输入中的行可以以 '\n'，'\r' 或 '\r\n' 结尾，这些行被翻译成 '\n' 在返回呼叫者之前。如果它是 ''，则启用通用换行模式，但行结尾将返回给调用者未翻译。如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。

### 1.13.4 ord(c)

> 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。例如 ord('a') 返回整数 97， ord('€') （欧元符号）返回 8364 。这是 chr() 的逆函数。

## 1.14 P

### 1.14.1 pow(base, exp, mod=None)

> 返回 base 的 exp 次幂；如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）。 两参数形式 pow(base, exp) 等价于乘方运算符: base**exp。
>
> 参数必须为数值类型。 对于混用的操作数类型，则适用二元算术运算符的类型强制转换规则。 对于 int 操作数，结果具有与操作数相同的类型（转换后），除非第二个参数为负值；在这种情况下，所有参数将被转换为浮点数并输出浮点数结果。 例如，pow(10, 2) 返回 100，但 pow(10, -2) 返回 0.01。 对于 int 或 float 类型的负基和一个非整数的指数，会产生一个复杂的结果。 例如， pow(-9, 0.5) 返回一个接近于 3j 的值。
>
> 对于 int 操作数 base 和 exp，如果给出 mod，则 mod 必须为整数类型并且 mod 必须不为零。 如果给出 mod 并且 exp 为负值，则 base 必须相对于 mod 不可整除。 在这种情况下，将会返回 pow(inv_base, -exp, mod)，其中 inv_base 为 base 的倒数对 mod 取余。

### 1.14.2 print(*objects, sep=' ', end='\n', file=None, flush=False)

> 将 `objects `打印输出至 file 指定的文本流，以 `sep` 分隔并在末尾加上 end。 sep 、 end 、 file 和 flush 必须以关键字参数的形式给出。

### 1.14.3 class property(fget=None, fset=None, fdel=None, doc=None)

> 返回 property 属性。
>
> fget 是获取属性值的函数。 fset 是用于设置属性值的函数。 fdel 是用于删除属性值的函数。并且 doc 为属性对象创建文档字符串。

## 1.15 R

### 1.15.1 class range([start, ]stop[, step=1])

> 虽然被称为函数，但 range 实际上是一个不可变的序列类型，参见在 range 对象 与 序列类型 --- list, tuple, range 中的文档说明。

### 1.15.2 repr(object)

> 返回一个字符串，其中包含对象的可打印表示形式。对于许多类型，此函数尝试返回一个字符串，该字符串将在传递给eval()时产生具有相同值的对象;否则，表示是一个用尖括号括起来的字符串，其中包含对象类型的名称以及通常包括对象的名称和地址的附加信息。类可以通过定义`__repr__()`方法来控制此函数为其实例返回的内容。如果`sys.displayhook()`不可访问，此函数将引发`RuntimeError`。

### 1.15.3 reversed(seq)

> 返回一个反向的 iterator。 seq 必须是一个具有 __reversed__() 方法的对象或者是支持该序列协议（具有从 0 开始的整数类型参数的 __len__() 方法和 __getitem__() 方法）。

### 1.15.4 round(number, ndigits=None)

> 返回 number 舍入到小数点后 ndigits 位精度的值。 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。
>
> 对于支持 round() 方法的内置类型，结果值会舍入至最接近的 10 的负 ndigits 次幂的倍数；如果与两个倍数同样接近，则选用偶数。因此，round(0.5) 和 round(-0.5) 均得出 0 而 round(1.5) 则为 2。ndigits 可为任意整数值（正数、零或负数）。如果省略了 ndigits 或为 None ，则返回值将为整数。否则返回值与 number 的类型相同。

## 1.16 S

### 1.16.1 class set([iterable])

> 返回一个新的 set 对象，可以选择带有从 iterable 获取的元素。 set 是一个内置类型。 请查看 set 和 集合类型 --- set, frozenset 获取关于这个类的文档。

### 1.16.2 setattr(object, name, value)

> 本函数与 getattr() 相对应。其参数为一个对象、一个字符串和一个任意值。字符串可以为某现有属性的名称，或为新属性。只要对象允许，函数会将值赋给属性。如 setattr(x, 'foobar', 123) 等价于 x.foobar = 123。

### 1.16.3 class slice([start,] stop[, step=1])

> 返回一个 slice 对象，代表由 range(start, stop, step) 指定索引集的切片。 其中参数 start 和 step 的默认值为 None。切片对象具有只读数据属性 start 、stop 和 step，只是返回对应的参数值（或默认值）。这几个属性没有其他明确的功能；不过 NumPy 和其他第三方扩展会用到。在使用扩展索引语法时，也会生成切片对象。例如： a[start:stop:step] 或 a[start:stop, i]。 另一种方案是返回迭代器对象，可参阅 itertools.islice() 。

### 1.16.4 sorted(iterable, /, *, key=None, reverse=False)

> 根据 iterable 中的项返回一个新的已排序列表。
>
> - 具有两个可选参数，它们都必须指定为关键字参数。
>   - key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。
>   - reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。

### 1.16.5 @staticmethod

> 将方法转换为静态方法。
>
> 静态方法不会接收隐式的第一个参数。要声明一个静态方法，请使用此语法
>
> - ```python
>   class C:
>       @staticmethod
>       def f(arg1, arg2, argN): ...
>   ```
>
> @staticmethod 这样的形式称为函数的 decorator -- 详情参阅 函数定义。
>
> 静态方法既可以由类中调用（如 C.f()），也可以由实例中调用（如```C().f()``）。此外，还可以作为普通的函数进行调用（如``f()``）。

### 1.16.6 class str(object=b''[, encoding='utf-8', errors='strict'])

> 返回一个 str 版本的 object 。
>
> str 是内置字符串 class 。更多关于字符串的信息查看 文本序列类型 --- str。

### 1.16.7 sum(iterable, /, start=0)

> 从 start 开始自左向右对 iterable 的项求和并返回总计值。 iterable 的项通常为数字，而 start 值则不允许为字符串。
>
> 对某些用例来说，存在 sum() 的更好替代。 拼接字符串序列的更好更快方式是调用 ''.join(sequence)。 要以扩展精度对浮点值求和，请参阅 math.fsum()。 要拼接一系列可迭代对象，请考虑使用 itertools.chain()。

### 1.16.8 class super(type, object_or_type=None)

> 返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。 这对于访问已在类中被重载的继承方法很有用。

## 1.17 T

### 1.17.1 class tuple([iterable])

> 虽然被称为函数，但 tuple 实际上是一个不可变的序列类型，参见在 元组 与 序列类型 --- list, tuple, range 中的文档说明。

### 1.17.2 class type(name, bases, dict, **kwds)

> 传入一个参数时，返回 object 的类型。 返回值是一个 type 对象，通常与 object.__class__ 所返回的对象相同。
>
> - 推荐使用 isinstance() 内置函数来检测对象的类型，因为它会考虑子类的情况。
>
> 传入三个参数时，返回一个新的 type 对象。 这在本质上是 class 语句的一种动态形式，name 字符串即类名并会成为 __name__ 属性；bases 元组包含基类并会成为 __bases__ 属性；如果为空则会添加所有类的终极基类 object。 dict 字典包含类主体的属性和方法定义；它在成为 __dict__ 属性之前可能会被拷贝或包装。 下面两条语句会创建相同的 type 对象:

## 1.18 V

### 1.18.1 vars([object])

> 返回模块、类、实例或任何其它具有 __dict__ 属性的对象的 __dict__ 属性。
>
> 模块和实例这样的对象具有可更新的 __dict__ 属性；但是，其它对象的 __dict__ 属性可能会设为限制写入（例如，类会使用 types.MappingProxyType 来防止直接更新字典）。
>
> 不带参数时，vars() 的行为类似 locals()。 请注意，locals 字典仅对于读取起作用，因为对 locals 字典的更新会被忽略。
>
> 如果指定了一个对象但它没有 __dict__ 属性（例如，当它所属的类定义了 __slots__ 属性时）则会引发 TypeError 异常。

## 1.19 V

### 1.19.1 zip(*iterables, strict=False)

>  在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。
>
>  zip() 是延迟执行的：直至迭代时才会对元素进行处理，比如 for 循环或放入 list 中。

## 1.20 \_

### 1.20.1 \_\_import__(name, globals=None, locals=None, fromlist=(), level=0)

> 备注: 与` importlib.import_module()` 不同，这是一个日常 Python 编程中不需要用到的高级函数。
>
> - 此函数会由 import 语句发起调用。 它可以被替换 (通过导入 builtins 模块并赋值给 builtins.__import__) 以便修改 import 语句的语义，但是 强烈 不建议这样做，因为使用导入钩子 (参见 PEP 302) 通常更容易实现同样的目标，并且不会导致代码问题，因为许多代码都会假定所用的是默认实现。 同样也不建议直接使用 __import__() 而应该用 importlib.import_module()。