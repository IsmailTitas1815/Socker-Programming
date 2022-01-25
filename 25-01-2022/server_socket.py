import socket
import datetime
from file_handler import Logger

class ServerSocket:
    
    def __init__(self, port):
        self.server_s = socket.socket()
        self.server_s.bind(('127.0.0.1', port))
        self.server_s.listen(10)
        print("Socket successfully created")
        print("I'm listening and waiting for connections")

    def start_receiving(self, csv_file_name, port):
        file_handler_obj = Logger()
        client, addr = self.server_s.accept() 
        print("connected with the client: ", addr)
        while True:
            data = client.recv(1024).decode()
            if data:
                message = "message: "+data+", sent by " + str(addr[1])
                file_handler_obj.logging_to_csv(csv_file_name, str(addr[1]),data)

                # saving into json file
                time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                received_data = {"sent_by": str(
                    addr[1]), "msg": data, "time": time}
                print(message)
                file_handler_obj.save_to_json(received_data, "server")
                
                message = "message received successfully by "+str(port)
                client.send(bytes(message, "utf-8"))
        client.close()
