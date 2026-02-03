from typing import cast, Any, Dict

import selenium_logger

TrackConditions = Dict[str, Any]

def set_track_conditions(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_track_conditions = raceCfg.pop("TrackConditions", {})
    track_conditions_cfg = cast(TrackConditions, raw_track_conditions)
    logger.info("TrackConditions: {}".format(track_conditions_cfg))