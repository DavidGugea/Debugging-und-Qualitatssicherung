import logging
import socket
import sys

# Initialize stream handler
stream = logging.StreamHandler(stream = sys.stdout)

# Create formatter and set it to the formatter
formatter = logging.Formatter(
    fmt = "{asctime} [ Level name : {levelname} || Line number : {lineno} ] == > {message}",
    datefmt = "%d.%m.%Y < - > %H:%M:%S",
    style = "{"
)
stream.setFormatter(formatter)

# Add the stream handler to a loger
logger = logging.getLogger()
logger.addHandler(stream)
logger.setLevel(logging.DEBUG)

# Initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.SOCK_STREAM = > TCP Connection
server.bind((socket.gethostname(), 80))
server.listen(50)

while True:
    # Accept client connection | with address |
    client, client_address = server.accept()
    while True:
        message = client.recv(1024) # message is encoded in bytes | ~ buffersize : 1024 ~ |
        if not message:
            # If the message is empty, break the connection with the client
            # Log lost connection with the client
            logger.fatal("Lost connection with the client. Address : {0}".format(
                client_address
            ))
            client.close()
            break
        else:
            # Log client message | DECODED FROM BYTES |
            logger.info("[{0}] {1}".format(
                client_address,
                message.decode("utf-8")
            ))
            continue
    continue
