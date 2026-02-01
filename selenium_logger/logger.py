import logging

def initialize() -> logging.Logger:
    logger = logging.getLogger('selenium')
    handler = logging.StreamHandler()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logging.getLogger('selenium.webdriver.remote').setLevel(logging.INFO)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.INFO)
    logger.info("this happening?")
    return logger