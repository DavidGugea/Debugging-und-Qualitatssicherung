import logging

logging.basicConfig(
    filename = "programm.log",
    level = logging.DEBUG,
    style = "{",
    format = "Asctime : {asctime} // Filename : {filename} // funcName : {funcName} // levelname : {levelname} // lineno : {lineno} // message : {message} // module : {module} // pathname : {pathname} // process : {process} // thread : {thread}",
    datefmt = "%d.%m.%Y %H:%M:%S"
)

# Information
logging.log(logging.INFO, "Info")
logging.info("Info 2")

# Error
logging.log(logging.ERROR, "Error")
logging.error("Error 2")