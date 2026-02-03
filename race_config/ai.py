from typing import cast, Dict, Any

import selenium_logger

AI = Dict[str, Any]

def set_ai(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_ai = raceCfg.pop("AI", {})
    ai_cfg = cast(AI, raw_ai)
    logger.info("AI: {}".format(ai_cfg))