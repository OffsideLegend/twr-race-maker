from typing import Any, Dict, cast

import selenium_logger

Admins = Dict[str, Any]

def set_admins(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_admins = raceCfg.pop("Admins", {})
    admins_cfg = cast(Admins, raw_admins)
    logger.info("Admins: {}".format(admins_cfg))