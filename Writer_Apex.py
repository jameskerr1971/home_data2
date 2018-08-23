import re
import time
from datetime import datetime
from influxdb import InfluxDBClient
import json

#wait for the scraper script to run at the start of the minute
time.sleep(10)

client = InfluxDBClient(host='192.168.0.54', port=8086, database='home_data')

#WIRE TRAFFIC RATE

with open ('/home/dennett/scripting2/wire_traffic_rate.json', 'rt') as json_file:
    contents = json.load(json_file)

wire_traffic_rate = contents['data']['results']['results'][0]['data']['series'][0]['fieldData'][0]['data'][0]['float']
#print(wire_traffic_rate)

time = contents['data']['results']['results'][0]['data']['intervalData']['intervals'][0]
#print(time)

wire_traffic_rate_json_body = [{"measurement": "traffic_rate", "tags": {"method": "wire", "unit": "Bits Per Seccond", "device": "all"},"time": time, "fields": {"value": wire_traffic_rate}}]

#print(wire_traffic_rate_json_body)

client.write_points(wire_traffic_rate_json_body)

#SERVER RESPONSE POPPER

with open ('/home/dennett/scripting2/wire_server_response_popper.json', 'rt') as json_file:
    contents = json.load(json_file)

wire_server_response_popper = contents['data']['results']['results'][0]['data']['series'][0]['fieldData'][0]['data'][0]['float']
#print(server_response_popper)

time = contents['data']['results']['results'][0]['data']['intervalData']['intervals'][0]
#print(time)

wire_server_response_popper_json_body = [{"measurement": "response_time", "tags": {"method": "wire", "unit": "Milliseconds", "device": "popper"},"time": time, "fields": {"value": wire_server_response_popper}}]

#print(wire_server_response_popper_json_body)

client.write_points(wire_server_response_popper_json_body)

#NETWORK DELAY

with open ('/home/dennett/scripting2/wire_network_delay.json', 'rt') as json_file:
    contents = json.load(json_file)

wire_network_delay = contents['data']['results']['results'][0]['data']['series'][0]['fieldData'][0]['data'][0]['float']

time = contents['data']['results']['results'][0]['data']['intervalData']['intervals'][0]
#print(time)

wire_network_delay_json_body = [{"measurement": "response_time", "tags": {"method": "wire", "unit": "Milliseconds", "device": "network"},"time": time, "fields": {"value": wire_network_delay}}]

#print(wire_network_delay_json_body)

client.write_points(wire_network_delay_json_body)

#WIRE TRAFFIC RATE DENNETT

with open ('/home/dennett/scripting2/wire_traffic_rate_dennett.json', 'rt') as json_file:
    contents = json.load(json_file)

wire_traffic_rate_dennett = contents['data']['results']['results'][0]['data']['series'][0]['fieldData'][0]['data'][0]['float']
#print(wire_traffic_rate_dennett)

time = contents['data']['results']['results'][0]['data']['intervalData']['intervals'][0]
#print(time)

wire_traffic_rate_dennett_json_body = [{"measurement": "traffic_rate", "tags": {"method": "wire", "unit": "Bits Per Seccond", "device": "dennett"},"time": time, "fields": {"value": wire_traffic_rate_dennett}}]

#print(wire_traffic_rate_dennett_json_body)

client.write_points(wire_traffic_rate_dennett_json_body)
