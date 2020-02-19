import sys
import logging

fileHandler = logging.FileHandler(
    filename = "fileHandler_LOGGING.log",
    mode="a",
    encoding = None,
    delay = False
)

formatter = logging.Formatter(
    fmt = "{asctime} [Level name : {levelname} // Line number : {lineno}] == > {message}",
    datefmt = "%d.%m.%Y < -- > %H:%M:%S",
    style = "{"
)
fileHandler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)


logger.critical("Critical")
logger.warning("Warning")
logger.info("Info")