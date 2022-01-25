from server_socket import ServerSocket
from client import ClientSocket
import threading
import random

port_input = random.randint(3000, 65000)

server = ServerSocket(port_input)
client = ClientSocket(port_input)

server_thread = threading.Thread(
    target=server.start_receiving, args=("server_file.csv", port_input))
client_thread = threading.Thread(
    target=client.sending_to_server, args=("client_file.csv", port_input))

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()
