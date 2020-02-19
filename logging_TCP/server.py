import socket
import pprint

PORT = 88

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.SOCK_STREAM == > TCP Connection
server.bind((socket.gethostname(), PORT))
server.listen(50)

while True:
    client, address = server.accept()
    while True:
        data = client.recv(1024)

        if not data:
            pprint.pprint(client)
            pprint.pprint("Connection lost with : {0}".format(address))
            break
        else:
            pprint.pprint("[{0}] {1}".format(
                address,
                data.decode("utf-8")
            ))
        