import hmac


def HMAC(txt, key):
    return hmac.new(key.encode(), txt.encode(), digestmod="md5").hexdigest()
    # return hmac.new(key.encode(), txt.encode(), digestmod="sha1").hexdigest()


if __name__ == "__main__":
    print(HMAC("123456", "key"))  # 0abf6bacd23c55fa6ab14eb44a7f5720
