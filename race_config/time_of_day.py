from typing import Dict, Any, cast

import selenium_logger

TimeOfDay = Dict[str, Any]

def set_time_of_day(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_tod = raceCfg.pop("TimeOfDay", {})
    time_of_day_cfg = cast(TimeOfDay, raw_tod)
    logger.info("Time of Day: {}".format(time_of_day_cfg))