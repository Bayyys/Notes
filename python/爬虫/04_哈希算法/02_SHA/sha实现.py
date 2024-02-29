import hashlib


def SHA1(str: str) -> str:
    """SHA1加密算法

    Args:
        str (str): 需要加密的字符串

    Returns:
        str: 加密后的字符串(40位16进制数)
    """
    return hashlib.sha1(str.encode("utf-8")).hexdigest()


sha1 = lambda str: hashlib.sha1(str.encode("utf-8")).hexdigest()


def SHA256(str: str) -> str:
    """SHA256加密算法

    Args:
        str (str): 需要加密的字符串

    Returns:
        str: 加密后的字符串(64位16进制数)
    """
    return hashlib.sha256(str.encode("utf-8")).hexdigest()


sha256 = lambda str: hashlib.sha256(str.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    data = "123456"
    print(f"SHA1编码后的数据, {SHA1(data)}")  # 7c4a8d09ca3762af61e59520943dc26494f8941b
    print(f"SHA1编码后的数据, {sha1(data)}")  # 7c4a8d09ca3762af61e59520943dc26494f8941b
    print(
        f"SHA256编码后的数据, {SHA256(data)}"
    )  # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
    print(
        f"SHA256编码后的数据, {sha256(data)}"
    )  # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
