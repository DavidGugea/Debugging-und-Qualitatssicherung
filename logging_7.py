import logging

logging.basicConfig(
    filename = "programm.log",
    format = "{asctime} [Levelname : {levelname} // Line number : {lineno}] == > {message}",
    datefmt = "%d.%m.%Y < -- > %H:%M:%S",
    style = "{",
    level = logging.DEBUG
)

# Information 
logging.log(logging.INFO, "Info")
logging.info("Info 2")

# Error
logging.log(logging.ERROR, "Error")
logging.error("Error 2")