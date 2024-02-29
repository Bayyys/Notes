import base64

if __name__ == "__main__":
    # 编码
    data = "Hello World"
    code = base64.b64encode(data.encode())
    print(f"编码后的数据：{code}")  # b'SGVsbG8gV29ybGQ='

    # 解码
    source = base64.b64decode(code)
    print(f"解码后的数据：{source.decode()}")  # Hello World
