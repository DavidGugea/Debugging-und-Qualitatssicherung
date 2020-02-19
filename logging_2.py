import logging

logging.basicConfig(
    filename = "programm.log",
    level = logging.DEBUG,
    style= "{",
    format = "{asctime} [{levelname}] {message}"
)

# Information
logging.info("Info")
logging.log(logging.INFO, "Info 2")

# Error
logging.error("Error")
logging.log(logging.ERROR, "Erro 2")