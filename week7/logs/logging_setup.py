import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        screen_handler = logging.StreamHandler()
        screen_handler.setFormatter(formatter)

        file_handler = logging.FileHandler('app.log')
        file_handler.setFormatter(formatter)

        logger.addHandler(screen_handler)
        logger.addHandler(file_handler)

    return logger
