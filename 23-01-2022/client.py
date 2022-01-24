import socket
port = 19999
c = socket.socket()
c.connect(('localhost',port))
from csv_handler import logging
import csv, json, datetime

# csv file's heading
file = open('client_file.csv','a', newline="")
write_file = csv.writer(file)
table_header = ("Sent to","Messege","Time")
write_file.writerow(table_header)
file.close()


while True:
    input_data = input()
    c.send(bytes(input_data,"utf-8"))
    logging('client_file.csv', str(port),input_data)

    # saving into json file
    json_file = open("server_client_data.json", "r")
    python_data = json.load(json_file)
    json_file.close()

    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    received_data = {"sent_to": str(
        port), "msg": input_data, "time": time}

    json_file = open("server_client_data.json", "w")
    python_data['client'].append(received_data)
    python_to_json_data = json.dumps(python_data)
    json_file.write(python_to_json_data)
    json_file.close()

    recv_data = c.recv(1024).decode()
    print(recv_data)
