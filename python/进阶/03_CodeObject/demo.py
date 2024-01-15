def f():
    pass


code = f.__code__

print(
    dir(code)
)  # <code object f at 0x0000016AED654930, file "e:\Coding\test\temp\python\进阶\CodeObject\demo.py", line 1>
print(
    code
)  # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_co_code_adaptive', '_varname_from_oparg', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_exceptiontable', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lines', 'co_linetable', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_positions', 'co_posonlyargcount', 'co_qualname', 'co_stacksize', 'co_varnames', 'replace']
"""
co_code: 字节码
co_lnotab: 行号与字节码的对应关系
co_name: 函数名

co_flags: 标志位(是否有参数, 是否有变量, 是否有注解等)
co_stacksize: 栈大小

co_argcount: 参数个数
co_posonlyargcount: 位置参数个数(定义参数时, /前面的参数必须使用位置传参)
co_kwonlyargcount: 关键字参数个数(定义参数时, *后面的参数必须使用关键字传参)
"""


import dis


def f(a):
    import math as m

    b = a.attr
    b = a.method()
    c = {}

    def g():
        c["a"] = 1
        return c

    return b, f


print("-----f-----")
fcode = f.__code__
print(f"co_nlocals: {fcode.co_nlocals}")  # 参数个数: 4
print(f"co_varnames: {fcode.co_varnames}")  # 参数名: ('a', 'm', 'c', 'g')
print(f"co_names: {fcode.co_names}")  # 全局变量名 ('math', 'attr', 'method', 'f')
print(f"co_cellvars: {fcode.co_cellvars}")  # 闭包变量名 ('c', )
print(f"co_freevars: {fcode.co_freevars}")  # 自由变量名 ()
print(
    f"co_consts: {fcode.co_consts}"
)  # 常量 (None, 0, <code object g at 0x000002752F47A4C0, file "e:\Coding\test\temp\python\ 进阶\CodeObject\demo.py", line 37>)


"""
co_nlocals: 局部变量个数(包括参数)
co_varnames: 局部变量名(包括参数)
co_names: 全局变量名(函数名, 模块名, 类名等)
co_cellvars: 闭包变量名(外部函数的局部变量)
co_freevars: 自由变量名
co_consts: 常量(数字, 字符串, None, True, False)
"""
