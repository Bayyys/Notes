import inspect  # inspect: 检查模块

# from objprint import op  # objprint: 对象打印


def f():
    frame = inspect.currentframe()
    # op(frame, honor_existing=False, depth=2)


f()

"""
(
    <frame object at 0x000001F6B0B4B1C0
    .f_back = <frame xxxx ...>, # 上一帧
    .f_builtins = {...},     # 内置变量
    .f_code = <code xxx, >,    # 代码对象
    .f_globals = {...},     # 全局变量
    .f_lasti = 0,        # 最后执行的指令
    .f_lineno = 9,     # 行号
    .f_locals = {...},    # 局部变量
    .f_trace = None    # 跟踪函数
    .f_trace_lines = True,  # 跟踪行
    .f_trace_opcodes = False    # 跟踪指令
)
"""
