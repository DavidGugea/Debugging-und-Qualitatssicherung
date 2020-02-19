import logging
import sys

# Initiate handler
handler = logging.StreamHandler(stream=sys.stdout)

# Create formater
frm = logging.Formatter("{asctime} {levelname}: {message}", datefmt="%d.%m.%Y < - > %H:%M:%S", style="{")

# Bind the formatter to the handler
handler.setFormatter(frm)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG) 


logger.critical("Critical")
logger.warning("Warning")
logger.info("Info")