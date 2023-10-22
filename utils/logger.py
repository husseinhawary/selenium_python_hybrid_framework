import logging

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.setLevel(logging.INFO)
__all__ = ["logger"]
