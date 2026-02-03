from typing import Any, Dict, cast

import selenium_logger

Track = Dict[str, Any]

def set_track(raceCfg: Dict[str, Any]) -> None:
    logger = selenium_logger.get_logger()
    raw_track = raceCfg.pop("Track", {})
    track_cfg = cast(Track, raw_track)
    logger.info("Track: {}".format(track_cfg))