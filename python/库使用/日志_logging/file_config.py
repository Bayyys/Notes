import logging.config
import file_config_child as child


def main():
    logging.config.fileConfig("log.ini", disable_existing_loggers=False)
    logger = logging.getLogger("root")
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    child.main()
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()
