from typing import Dict, Any, cast

import selenium_logger

Cars = Dict[str, Any]

def set_cars(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_cars = raceCfg.pop("Cars", {})
    cars_cfg = cast(Cars, raw_cars)
    logger.info("Cars: {}".format(cars_cfg))