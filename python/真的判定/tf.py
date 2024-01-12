# True/False
a = True

if a is True:  # 唯一 是 True (反: is not True)
    print("a is True")

if a == True:  # 可以是 True 也可以是 1 (== 可以被重载)
    print("a == True")

if a:  # bytecode: POP_JUMP_IF_FALSE → PyObject_IsTrue
    # None, 0, 0.0, 0j, Decimal(0), Fraction(0, 1), [], (), {}, set(), range(0) 都是 False
    # 自定义数据结构: __bool__ 或 __len__ 返回 0 时为 False
    print("a")

if bool(a): # bool 实际是一个 类
    print("bool(a)")
