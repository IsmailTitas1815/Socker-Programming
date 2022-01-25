import socket
from file_handler import Logger
import datetime

class ClientSocket:
    def __init__(self, port):
        self.client_s = socket.socket()
        self.port = port
        self.client_s.connect(('127.0.0.1',port))
    
    def sending_to_server(self, csv_file_name, port):
        file_handler_obj = Logger()
        while True:
            input_data = input("input: ")
            self.client_s.send(bytes(input_data,"utf-8"))
            file_handler_obj.logging_to_csv(csv_file_name,str(port),input_data)

            # saving into json file
            time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            data = {"sent_to": str(
                self.port), "msg": input_data, "time": time}
            file_handler_obj.save_to_json(data,"client")

            recv_data = self.client_s.recv(1024).decode()
            print(recv_data)
