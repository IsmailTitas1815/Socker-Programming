import socket
port = 9999
c = socket.socket()
c.connect(('localhost',port))
from file_handler import file_handler_obj
import datetime

while True:
    input_data = input()
    c.send(bytes(input_data,"utf-8"))
    file_handler_obj.logging_to_csv('client_file.csv',str(port),input_data)

    # saving into json file
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    data = {"sent_to": str(
        port), "msg": input_data, "time": time}
    file_handler_obj.save_to_json(data,"client")

    recv_data = c.recv(1024).decode()
    print(recv_data)
