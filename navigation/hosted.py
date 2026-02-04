from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from driver import get_driver_wait

def go_to_hosted() -> None:
    """Navigate to the Hosted section of the iRacing UI."""
    wait = get_driver_wait()
    official = wait.until(EC.visibility_of_element_located(
        (By.LINK_TEXT, "Hosted")
    ))
    official.click()

def create_hosted_race() -> None:
    """Create a new hosted race."""
    wait = get_driver_wait()
    createARace = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "css-3k57h1")
    ))
    createARace.click()

    newRace = wait.until(EC.visibility_of_element_located(
        (By.PARTIAL_LINK_TEXT, "New Race")
    ))
    newRace.click()

