import re
import time
from datetime import datetime
import pymongo
from influxdb import InfluxDBClient

#wait for the scraper script to run at the start of the minute
time.sleep(10)

#get the data from the scrapings file
with open ('/home/dennett/scripting2/Scrapings_Popper.txt', 'rt') as in_file:
    contents = in_file.read()

cpu_percent_digits = []

cpu_percent_digits_list = re.findall('\d+\.?\d*', contents)

#print('cpu_percent_digits_list', cpu_percent_digits_list)

cpu_percent_int_list = []

for i in cpu_percent_digits_list:
    f = int(i)
    cpu_percent_int_list.append(f)

#print('cpu_percent_int_list ', cpu_percent_int_list)

cpu_percent_int = sum(cpu_percent_int_list) / float(len(cpu_percent_int_list))

#print('cpu_percent_int ', cpu_percent_int)

#use UTC time to avoid BST changes
now = datetime.utcnow()
t = now.isoformat()

data_dict = {'Time': t, 'Metric': cpu_percent_int}

#print(data_dict)

client = InfluxDBClient(host='192.168.0.54', port=8086)

client.switch_database('home_data')

cpu_json_body = [{"measurement": "cpu_utilisation", "tags": {"method": "device", "unit": "%", "device": "popper"}, "fields": {"value": cpu_percent_int}}]

client.write_points(cpu_json_body)
