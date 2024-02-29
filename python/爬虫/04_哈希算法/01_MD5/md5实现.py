import hashlib


def MD5(str: str) -> str:
    """MD5加密算法

    Args:
        str (str): 需要加密的字符串

    Returns:
        str: 加密后的字符串(32位16进制数)
    """
    return hashlib.md5(str.encode("utf-8")).hexdigest()


md5 = lambda str: hashlib.md5(str.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    data = "123456"
    print(f"编码后的数据, {MD5(data)}")  # e10adc3949ba59abbe56e057f20f883e
    print(f"编码后的数据, {md5(data)}")  # e10adc3949ba59abbe56e057f20f883e
