import logging.handlers
import logging
import socket
import sys

# Initialize socket handler
TCP_LOGGING_HANDLER = logging.handlers.SocketHandler(
    host = socket.gethostname(),
    port = 80
)

# Create formatter for the socket handler
formatter = logging.Formatter(
    fmt = "{asctime} [ Level name : {levelname} || Line number : {lineno}] == > {message}",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    style = "{"
)

# Set up formatter and level for the handler
TCP_LOGGING_HANDLER.setFormatter(formatter)
TCP_LOGGING_HANDLER.setLevel(logging.DEBUG)

# Bind the handler to a logger
logger = logging.getLogger()
logger.addHandler(TCP_LOGGING_HANDLER)
logger.setLevel(logging.DEBUG)

# Send log inputs to the server
while True:
    msg = input("> ")
    
    # THE MESSAGE THAT WE SEND MUST BE ENCODED IN BYTES #
    TCP_LOGGING_HANDLER.send(msg.encode("utf-8"))