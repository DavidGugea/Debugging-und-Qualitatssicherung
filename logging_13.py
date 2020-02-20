import logging

fileHandler = logging.FileHandler(
    filename = "fileHandler_Stream.log",
    mode = "a",
    encoding = None,
    delay = False
)

formatter = logging.Formatter(
    fmt = "{asctime} [ Level name : {levelname} || Line number : {lineno} ] == > {message}",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    style = "{",
)
fileHandler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)


logger.info("Info")
logger.critical("Critical")
logger.warning("Warning")
logger.fatal("Fatal")

logger.log(logging.INFO, "Info 2")
logger.log(logging.CRITICAL, "Critical 2")
logger.log(logging.WARNING, "Warning 2")
logger.log(logging.FATAL, "Fatal 2")