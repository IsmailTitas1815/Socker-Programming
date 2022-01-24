import csv, datetime, json

# logging socet data into csv files
def logging(file, sent_by, msg):
    file = open(file,'a', newline="")
    write_file = csv.writer(file)
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    data_touple = (sent_by, msg, time)
    write_file.writerow(data_touple)
    file.close()
