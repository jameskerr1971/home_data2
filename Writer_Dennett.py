import re
import time
from datetime import datetime
#from pymongo import MongoClient
import pymongo
from influxdb import InfluxDBClient

#wait for the scraper script to run at the start of the minute
#time.sleep(40)

client = InfluxDBClient(host='192.168.0.54', port=8086, database='home_data')

#get the data from the scrapings file
with open ('/home/dennett/scripting2/Scrapings_Dennett.txt', 'rt') as in_file:
    contents = in_file.read()

#CPU PERCENT
cpu_percent_digits = []
cpu_percent_mo = re.search('(load average:).......', contents)
cpu_percent_text = cpu_percent_mo.group()
cpu_percent_digits_list = re.findall('\d+\.?\d*', cpu_percent_text)
cpu_percent_digits = cpu_percent_digits_list[0]
cpu_percent_flo =  float(cpu_percent_digits)

#use UTC time to avoid BST changes
now = datetime.utcnow()
t = now.isoformat()

cpu_percent_data_dict = {'Time': t, 'Metric': cpu_percent_flo}
#print('cpu_percent_data_dict ', cpu_percent_data_dict)
#cpu_percent_coll = db.dennett_cpu
#cpu_percent_write = cpu_percent_coll.insert_one(cpu_percent_data_dict)

#FREE MEMORY
free_memory_digits = []
free_memory_mo = re.search('(Mem:)..............................................', contents)
free_memory_text = free_memory_mo.group()
free_memory_digits_list = re.findall('\d+', free_memory_text)
free_memory_digits = free_memory_digits_list[2]
free_memory_int = int(free_memory_digits)

#use UTC time to avoid BST changes
now = datetime.utcnow()
t = now.isoformat()

free_memory_data_dict = {'Time': t, 'Metric': free_memory_int}
#print('free_memory_data_dict ', free_memory_data_dict)
#free_memory_coll = db.dennett_free_memory
#free_memory_write = free_memory_coll.insert_one(free_memory_data_dict)

#DISK USED
disk_used_digits = []
disk_used_mo = re.search('(sda1)..................................................', contents)
disk_used_text = disk_used_mo.group()
disk_used_digits_list = re.findall('\d+\.?\d*', disk_used_text)
disk_used_digits = disk_used_digits_list[4]
disk_used_percent = int(disk_used_digits)

#use UTC time to avoid BST changes
now = datetime.utcnow()
t = now.isoformat()

disk_used_data_dict = {'Time': t, 'Metric': disk_used_percent}
#print('disk_used_data_dict ', disk_used_data_dict)
#disk_used_coll = db.dennett_disk_used
#disk_used_write = disk_used_coll.insert_one(disk_used_data_dict)

cpu_json_body = [{"measurement": "cpu_utilisation", "tags": {"method": "device", "unit": "%", "device": "dennett"}, "fields": {"value": cpu_percent_flo}}]

client.write_points(cpu_json_body)

mem_json_body = [{"measurement": "free_memory", "tags": {"method": "device", "unit": "MB", "device": "dennett"}, "fields": {"value": free_memory_int}}]

client.write_points(mem_json_body)

disk_json_body = [{"measurement": "disk_used", "tags": {"method": "device", "unit": "%", "device": "dennett"}, "fields": {"value": disk_used_percent}}]

client.write_points(disk_json_body)
