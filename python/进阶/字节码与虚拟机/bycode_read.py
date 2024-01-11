import dis  # 字节码: 用来查看函数的字节码

with open("./python/进阶/字节码与虚拟机/demo.py", "rb") as f:
    s = f.read()

dis.dis(s)
