from typing import Any, Dict, cast

import selenium_logger

TimeLimit = Dict[str, Any]

def set_time_limit(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_tl = raceCfg.pop("TimeLimit", {})
    time_limit_cfg = cast(TimeLimit, raw_tl)
    logger.info("Time Limit: {}".format(time_limit_cfg))