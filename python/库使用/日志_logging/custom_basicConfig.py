import logging


def main():
    logging.basicConfig(
        level=logging.DEBUG,  # 输出级别
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # 输出格式
        datefmt="%Y-%m-%d %H:%M:%S",  # 时间格式
        filename="custom_basicConfig.log",  # 输出文件
    )
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")


if __name__ == "__main__":
    main()
