# from email import message
import socket
import datetime

from file_handler import file_handler_obj


s = socket.socket()
print("Socket successfully created")

port = 9999

s.bind(('localhost', port))
s.listen(100)
print("I'm listening and waiting for connections")

while True:
    c, addr = s.accept()
    print("connected with the client: ", addr)
    while True:
        data = c.recv(1024).decode()
        message = "message: "+data+", sent by " + str(addr[1])
        if data:
            file_handler_obj.logging_to_csv('server_file.csv',str(addr[1]),data)

            # saving into json file
            time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            received_data = {"sent_by": str(
                addr[1]), "msg": data, "time": time}
            file_handler_obj.save_to_json(received_data, "server")

            
            print(message)
            message = "message received successfully by "+str(port)
            c.send(bytes(message, "utf-8"))
    c.close()
