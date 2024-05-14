import logging

# 日志级别: DEBUG < INFO < WARNING < ERROR < CRITICAL


def log():
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        streamHandler = logging.StreamHandler()
        fileHandler = logging.FileHandler(
            "custom_basicConfig_morehandler.log", encoding="utf-8"
        )

        # 设置输出格式
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        streamHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        # 设置输出级别
        streamHandler.setLevel(logging.WARNING)
        fileHandler.setLevel(logging.ERROR)

        # 添加handler
        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)

    return logger


def main():
    logger = log()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
