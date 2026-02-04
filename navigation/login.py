import time

from driver import get_driver_wait, get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login():
    wait = get_driver_wait()
    driver = get_driver()
    loginButton = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button")
    ))
    loginButton.click()

    emailAddress = wait.until(EC.visibility_of_element_located(
        (By.ID, "memberEmail")
    ))
    emailAddress.send_keys("tom9schairer@gmail.com")
    password = wait.until(EC.visibility_of_element_located(
        (By.ID, "memberPassword")
    ))

    time.sleep(10)

    loginAgain = driver.find_element(By.CSS_SELECTOR, "form").find_element(By.CLASS_NAME, "ir-h9kfy")
    loginAgain.click()

    time.sleep(10)

    continueButton = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "css-h9kfy")
    ))
    continueButton.click()
