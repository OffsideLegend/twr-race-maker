from typing import Any, Dict, cast

import selenium_logger

ServerDetails = Dict[str, Any]

def set_server_details(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_sd = raceCfg.pop("ServerDetails", {})
    server_details_cfg = cast(ServerDetails, raw_sd)
    logger.info("Server Details: {}".format(server_details_cfg))