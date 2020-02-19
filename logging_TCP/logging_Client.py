import logging.handlers
import logging
import socket
import sys

PORT = 88

client = logging.handlers.SocketHandler(socket.gethostname(), PORT)
stream = logging.StreamHandler(stream=sys.stdout)

formatter = logging.Formatter(
    fmt = "{asctime} [Level name : {levelname} // Line number : {lineno}] == > {message}",
    datefmt = "%d.%m.%Y < -- > %H:%M:%S",
    style = "{"
)
client.setFormatter(formatter)
stream.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(client)
logger.addHandler(stream)

logger.setLevel(logging.DEBUG) # debugging mode

client.send("asd".encode("utf-8"))