from typing import Any, Dict, cast

import selenium_logger

TrackOptions = Dict[str, Any]

def set_track_options(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_to = raceCfg.pop("TrackOptions", {})
    track_options_cfg = cast(TrackOptions, raw_to)
    logger.info("Track Options: {}".format(track_options_cfg))