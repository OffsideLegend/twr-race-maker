from typing import cast, Any, Dict

import selenium_logger

RaceOptions = Dict[str, Any]

def set_race_options(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_race_options = raceCfg.pop("RaceOptions", {})
    race_options_cfg = cast(RaceOptions, raw_race_options)
    logger.info("RaceOptions: {}".format(race_options_cfg))