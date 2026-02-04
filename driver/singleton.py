from typing import Optional

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

_driver: Optional[WebDriver] = None
_wait_driver: Optional[WebDriverWait] = None

def initialize_driver() -> WebDriver:
    global _driver
    if _driver is not None:
        return _driver
    _driver = webdriver.Chrome()
    return _driver

def initialize_driver_wait() -> WebDriverWait:
    global _wait_driver
    if _wait_driver is not None:
        return _wait_driver
    driver = initialize_driver()
    _wait_driver = WebDriverWait(driver, 15)
    return _wait_driver

def get_driver() -> WebDriver:
    if _driver is None:
        return initialize_driver()
    return _driver

def get_driver_wait() -> WebDriverWait:
    if _wait_driver is None:
        return initialize_driver_wait()
    return _wait_driver

