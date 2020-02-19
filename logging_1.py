import logging

logging.basicConfig(
    filename="programm.log",
    level = logging.DEBUG
)

logging.info("Info")
logging.error("Error")

logging.shutdown() 