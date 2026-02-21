from datetime import datetime
import time
from typing import Any, Dict, cast
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import get_driver, get_driver_wait

import selenium_logger

ServerDetails = Dict[str, Any]

server_map = {
    "US-East-OH": "radio-:rov0:",
    "US-West": "radio-:rov1:",
    "AU-Syd": "radio-:rov2:",
    "BR-Sao": "radio-:rov3:",
    "DE_Fra": "radio-:rov4:",
    "JP-Tok": "radio-:rov5:",
}

def set_server_details(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_sd = raceCfg.pop("ServerDetails", {})
    server_details_cfg = cast(ServerDetails, raw_sd)

    driver = get_driver()
    wait = get_driver_wait()

    # select the server icon
    race_info_nav_button = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "icon-servers")
    ))
    race_info_nav_button.click()

    # click the server value to pull up the drop down and make visible the server DOM element
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[normalize-space(text())='{}']".format(server_details_cfg["server"]))
    )).click()

    # click the configured server using the server details maps
    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, server_map[server_details_cfg["server"]])
    )).click()

    driver.find_element(By.ID, "toggle-switch60705962-9b4b-6a34-ea57-474f181203a9").click()

    driver.find_element(By.CLASS_NAME, "rdt").click()

    # Expect configured time string to be provided under a key in server_details_cfg.
    # If it's missing, pick_month will be a no-op.
    pick_month(server_details_cfg.get("time", ""))

    logger.info("Server Details: {}".format(server_details_cfg))

month_map = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}

def pick_month(configured_time: str) -> None:
    """Click the calendar prev/next until the displayed month matches configured_time's month.
    configured_time: string like "Jan 31, 2026 8:45 pm". If empty, do nothing.
    """
    if not configured_time:
        return

    wait = get_driver_wait()

    # parse into a datetime object (naive)
    configured_dt = datetime.strptime(configured_time, "%b %d, %Y %I:%M %p")

    now = time.time()
    dt = datetime.fromtimestamp(now)

    current_month = dt.month
    target_month = configured_dt.month

    if target_month == current_month:
        return

    displayed_month = current_month

    # move backwards month-by-month until we reach target_month
    if target_month < current_month:
        while displayed_month != target_month:
            displayed_month -= 1
            if displayed_month < 1:
                displayed_month = 12
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "rdtPrev")
            )).click()
        return

    # move forwards month-by-month until we reach target_month
    if target_month > current_month:
        while displayed_month != target_month:
            displayed_month += 1
            if displayed_month > 12:
                displayed_month = 1
            wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "rdtNext")
            )).click()
        return
