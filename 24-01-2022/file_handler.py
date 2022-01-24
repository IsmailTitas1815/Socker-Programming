import csv, datetime, json

class Logger:

    def __init__(self):
        pass

    # logging socket data into csv files
    def logging_to_csv(self, file_name, sent_by, msg):
        
        file = open(file_name,'a', newline="")
        write_file = csv.writer(file)
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        data_touple = (sent_by, msg, time)
        write_file.writerow(data_touple)
        file.close()

    # saving socket data into json file
    def save_to_json(self, data, source):
        print("saving: ", source)
        json_file = open("server_client_data.json", "r")
        python_data = json.load(json_file)
        json_file.close()

        json_file = open("server_client_data.json", "w")
        if source == "server":
            python_data['server'].append(data)
            python_to_json_data = json.dumps(python_data)
            json_file.write(python_to_json_data)
        if source=='client':
            python_data['client'].append(data)
            python_to_json_data = json.dumps(python_data)
            json_file.write(python_to_json_data)
        json_file.close()

file_handler_obj = Logger()
