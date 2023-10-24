import logging

logger = logging.getLogger(__name__)
# to display the logs in the console
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.setLevel(logging.INFO)
# __all__ = ["logger"] to export only the logger attribute from the module.
__all__ = ["logger"]
