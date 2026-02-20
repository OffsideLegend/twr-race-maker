import time
import argparse

from driver import get_driver, get_driver_wait
from navigation import login, go_to_hosted
from navigation.hosted import create_hosted_race
from race_config import config, set_race_info, set_server_details, set_admins, set_time_limit, set_track_conditions
from race_config.ai import set_ai
from race_config.cars import set_cars
from race_config.race_options import set_race_options
from race_config.time_of_day import set_time_of_day
from race_config.track import set_track
from race_config.track_options import set_track_options
from race_config.weather import set_weather
from selenium_logger import get_logger

# Initialize the parser
parser = argparse.ArgumentParser(description="Process some integers.")

# Add arguments
parser.add_argument("--config", type=str, help="config file path")

args = parser.parse_args()

logger = get_logger()

raceConfig = config.parse_config(args.config)

driver = get_driver()

# Start
driver.get("https://members-ng.iracing.com")

login()

go_to_hosted()

create_hosted_race()

set_race_info(raceConfig)
set_server_details(raceConfig)
set_admins(raceConfig)
set_time_limit(raceConfig)
set_cars(raceConfig)
set_track(raceConfig)
set_track_options(raceConfig)
set_time_of_day(raceConfig)
set_weather(raceConfig)
set_race_options(raceConfig)
set_track_conditions(raceConfig)
set_ai(raceConfig)

# if modal != None:
#     driver.find_element(By.CSS_SELECTOR, "button").click()

# driver.get("https://www.iracing.com")
#
# wait = WebDriverWait(driver, 15)
#
# # 1. Wait for the cookie modal container to appear
# modal = wait.until(EC.visibility_of_element_located(
#     (By.CSS_SELECTOR, "div.modal-container")
# ))
#
# # 2. Click "Customize Cookies" to reveal the slidein-block you want
# decline = wait.until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "button.decline-cookies")
# ))
# decline.click()
#
# topNav = wait.until(EC.visibility_of_element_located(
#     (By.ID, "main-nav-container")
# )).find_element(By.ID, "top-nav")
# li = topNav.find_element(By.CSS_SELECTOR, "ui li")
#
# logger.info("button text: ".format(topNav.find_element(By.CSS_SELECTOR, "a").text))
# loginLink = mainNav.find_element(By.LINK_TEXT, "Log In")
# loginLink.click()
# loginList[0].click()

# signinButton = loginList[0]
# logger.info("signin button is {}".format(signinButton))
# a = signinButton.find_element(By.CSS_SELECTOR, "a")
# logger.info("a {}".format(a))
# link = wait.until(EC.element_to_be_clickable(signinButton))
# link_text = link.text
# logger.info("Link text: {}".format(link_text))


time.sleep(300)