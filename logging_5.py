import logging
import sys

# Initialize the stream handler
handler = logging.StreamHandler(stream=sys.stdout) # Set up stream for the handler | Default : sys.stdout |

# Initialize the Formater and bind it to the handler
FRMT = logging.Formatter(
    "{asctime} {levelname} : {message}",
    datefmt = "%d.%m.%Y < -- > %H:%M:%S",
    style = "{"
)
handler.setFormatter(FRMT)

# Initalize logger
logger = logging.getLogger()

# Add the made handler to the logger
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Messages
logger.critical("Critical")
logger.warning("Warning")
logger.info("Info")