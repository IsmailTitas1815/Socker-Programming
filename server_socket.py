from email import message
import socket
import csv
import datetime
import json

from blinker import receiver_connected
from csv_handler import logging

s = socket.socket()
print("Socket successfully created")

port = 19999

s.bind(('localhost', port))
s.listen(10)
print("I'm listening and waiting for connections")

# csv file's heading
file = open('server_file.csv', 'a', newline="")
write_file = csv.writer(file)
table_header = ("Sent by", "Messege", "Time")
write_file.writerow(table_header)
file.close()

while True:
    c, addr = s.accept()
    print("connected with the client: ", addr)
    while True:
        data = c.recv(1024).decode()
        message = "message: "+data+", sent by " + str(addr[1])
        if data:
            logging('server_file.csv', str(addr[1]), data)

            # saving into json file
            json_file = open("server_client_data.json", "r")
            python_data = json.load(json_file)
            json_file.close()

            time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            received_data = {"sent_by": str(
                addr[1]), "msg": data, "time": time}

            json_file = open("server_client_data.json", "w")
            python_data['server'].append(received_data)
            python_to_json_data = json.dumps(python_data)
            json_file.write(python_to_json_data)
            json_file.close()

            print(message)
            message = "message received successfully by "+str(port)
            c.send(bytes(message, "utf-8"))
    c.close()
