import logging

logging.basicConfig(
    filename="programm.log",
    level = logging.DEBUG,
    style = "{",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    format = "{asctime} [ Level name : {levelname} || Line number : {lineno} ] === > {message}"
)

logging.info("Info")
logging.log(logging.INFO, "Info 2")

logging.error("Error")
logging.log(logging.ERROR, "Error 2") 