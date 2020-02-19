import logging
import sys

handler = logging.StreamHandler(stream=sys.stdout)

FRMT = logging.Formatter(
    fmt = "{asctime} [levelname : {levelname} // line number : {lineno}] ========= > {message}",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    style = "{"
)
handler.setFormatter(FRMT)

logger = logging.getLogger()
logger.addHandler(handler)

logger.setLevel(logging.DEBUG)

# Messages
logger.critical("Critical")

logger.warning("Warning")

logger.info("Info")