from typing import cast, Any, Dict

import selenium_logger

Weather = Dict[str, Any]

def set_weather(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_weather = raceCfg.pop("Weather", {})
    weather_cfg = cast(Weather, raw_weather)
    logger.info("Weather: {}".format(weather_cfg))