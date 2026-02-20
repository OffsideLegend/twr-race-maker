from typing import Any, Dict, cast
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from driver import get_driver, get_driver_wait

import selenium_logger

ServerDetails = Dict[str, Any]

def set_server_details(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_sd = raceCfg.pop("ServerDetails", {})
    server_details_cfg = cast(ServerDetails, raw_sd)

    driver = get_driver()
    wait = get_driver_wait()

    race_info_nav_button = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "icon-servers")
    ))
    race_info_nav_button.click()

    logger.info("Server Details: {}".format(server_details_cfg))

