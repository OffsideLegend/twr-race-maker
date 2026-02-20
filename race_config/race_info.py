from .config import RaceConfig
from selenium_logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import get_driver, get_driver_wait

from typing import Any, Dict, cast

RaceInfo = Dict[str, Any]

def set_race_info(raceCfg: RaceConfig) -> None:
    logger = get_logger()
    raw_ri = raceCfg.pop("RaceInformation", {})
    race_info_cfg = cast(RaceInfo, raw_ri)

    driver = get_driver()
    wait = get_driver_wait()

    race_info_nav_button = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "icon-edit")
    ))
    race_info_nav_button.click()

    session_name_field = driver.find_element(
        By.XPATH, "//label[normalize-space(text())='Session Name']/following-sibling::*[1]"
    )
    session_name_field.send_keys(race_info_cfg["SessionName"])

    password_field = driver.find_element(
        By.XPATH, "//label[normalize-space(text())='Password (Optional)']/following-sibling::*[1]")
    password_field.send_keys(race_info_cfg["Password"])

    description_field = driver.find_element(
        By.XPATH, "//label[normalize-space(text())='Description']/following-sibling::*[1]")
    description_field.send_keys(race_info_cfg["Description"])
