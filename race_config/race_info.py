from .config import RaceConfig
from selenium_logger import get_logger

from typing import Any, Dict, cast

RaceInfo = Dict[str, Any]

def set_race_info(raceCfg: RaceConfig) -> None:
    logger = get_logger()
    raw_ri = raceCfg.pop("RaceInformation", {})
    race_info_cfg = cast(RaceInfo, raw_ri)
    logger.info("Race Info: {}".format(race_info_cfg))
