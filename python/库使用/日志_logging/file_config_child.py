import logging


def main():
    logger = logging.getLogger("main")
    logger.info("This is the main function of the child module.")


if __name__ == "__main__":
    main()
