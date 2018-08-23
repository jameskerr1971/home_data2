import datetime as dt
import time
import requests
import json

now = dt.datetime.utcnow()

more_seconds_back = dt.timedelta(seconds=120)
less_seconds_back = dt.timedelta(seconds=119)

more_seconds_ago = now - more_seconds_back
less_seconds_ago = now - less_seconds_back

now_iso = now.isoformat()
more_seconds_ago_iso = more_seconds_ago.isoformat()
less_seconds_ago_iso = less_seconds_ago.isoformat()

now_iso_str = str(now_iso)
more_seconds_ago_iso_str = str(more_seconds_ago_iso)
less_seconds_ago_iso_str = str(less_seconds_ago_iso)

session = requests.Session()
sessionurl = 'https://192.168.0.12/oa/api/session'
headers = {'Content-type': 'application/json', 'Accept':'application/json'}
sessionpayload = {'session' : {'username': 'admin', 'password': '0bserver'}}
sessionpost = session.post(sessionurl, headers=headers, data=json.dumps(sessionpayload), verify=False)

#WIRE TRAFFIC RATE
wire_traffic_rate_dashboard = {"params" : {"dashboardId": 'C77BF78C-3987-11E8-A3BF-0001C0158FE8', "businessGroupId": "EC1DC39A-3989-11E8-A3BF-0001C0158FE8", "params": {"startTime": more_seconds_ago_iso_str, "endTime": less_seconds_ago_iso_str}}}
wire_traffic_rate_resultsurl = 'https://192.168.0.12/oa/api/dashboardResults'
wire_traffic_rate_results = session.post(wire_traffic_rate_resultsurl, headers=headers, data=json.dumps(wire_traffic_rate_dashboard), verify=False)
wire_traffic_rate_results_text = wire_traffic_rate_results.text
#print('wire_traffic_rate_results_text ', wire_traffic_rate_results_text)
wire_traffic_rate_results_text_json = json.loads(wire_traffic_rate_results_text)

with open ('/home/dennett/scripting2/wire_traffic_rate.json', 'w') as json_file:
    json.dump(wire_traffic_rate_results_text_json, json_file)

#WIRE SERVER RESPONSE POPPER
wire_server_response_popper_dashboard = {"params" : {"dashboardId": 'D961132A-3987-11E8-A3BF-0001C0158FE8', "businessGroupId": "EC1DC39A-3989-11E8-A3BF-0001C0158FE8", "params": {"startTime": more_seconds_ago_iso_str, "endTime": less_seconds_ago_iso_str}}}
wire_server_response_popper_resultsurl = 'https://192.168.0.12/oa/api/dashboardResults'
wire_server_response_popper_results = session.post(wire_server_response_popper_resultsurl, headers=headers, data=json.dumps(wire_server_response_popper_dashboard), verify=False)
wire_server_response_popper_results_text = wire_server_response_popper_results.text
#print('wire_server_response_popper_results_text ', wire_server_response_popper_results_text)
wire_server_response_popper_results_text_json = json.loads(wire_server_response_popper_results_text)

with open ('/home/dennett/scripting2/wire_server_response_popper.json', 'w') as json_file:
    json.dump(wire_server_response_popper_results_text_json, json_file)

#WIRE NETWORK DELAY
wire_network_delay_dashboard = {"params" : {"dashboardId": 'D04A93BA-3987-11E8-A3BF-0001C0158FE8', "businessGroupId": "EC1DC39A-3989-11E8-A3BF-0001C0158FE8", "params": {"startTime": more_seconds_ago_iso_str, "endTime": less_seconds_ago_iso_str}}}
wire_network_delay_resultsurl = 'https://192.168.0.12/oa/api/dashboardResults'
wire_network_delay_results = session.post(wire_network_delay_resultsurl, headers=headers, data=json.dumps(wire_network_delay_dashboard), verify=False)
wire_network_delay_results_text = wire_network_delay_results.text
#print('wire_network_delay_results_text ', wire_network_delay_results_text)
wire_network_delay_results_text_json = json.loads(wire_network_delay_results_text)

with open ('/home/dennett/scripting2/wire_network_delay.json', 'w') as json_file:
    json.dump(wire_network_delay_results_text_json, json_file)

#WIRE TRAFFIC RATE DENNETT
wire_traffic_rate_dennett_dashboard = {"params" : {"dashboardId": 'D04A93B7-3987-11E8-A3BF-0001C0158FE8', "businessGroupId": "EC1DC39A-3989-11E8-A3BF-0001C0158FE8", "params": {"startTime": more_seconds_ago_iso_str, "endTime": less_seconds_ago_iso_str}}}
wire_traffic_rate_dennett_resultsurl = 'https://192.168.0.12/oa/api/dashboardResults'
wire_traffic_rate_dennett_results = session.post(wire_traffic_rate_dennett_resultsurl, headers=headers, data=json.dumps(wire_traffic_rate_dennett_dashboard), verify=False)
wire_traffic_rate_dennett_results_text = wire_traffic_rate_dennett_results.text
#print('wire_traffic_rate_dennett_results_text ', wire_traffic_rate_dennett_results_text)
wire_traffic_rate_dennett_results_text_json = json.loads(wire_traffic_rate_dennett_results_text)

with open ('/home/dennett/scripting2/wire_traffic_rate_dennett.json', 'w') as json_file:
    json.dump(wire_traffic_rate_dennett_results_text_json, json_file)

#WIRE NETWORK DELAY VIAVIDOTCOM
wire_network_delay_viavidotcom_dashboard = {"params" : {"dashboardId": 'FFEE7214-5D0C-11E8-8A54-0001C0158FE8', "businessGroupId": "EC1DC39A-3989-11E8-A3BF-0001C0158FE8", "params": {"startTime": more_seconds_ago_iso_str, "endTime": less_seconds_ago_iso_str}}}
wire_network_delay_viavidotcom_resultsurl = 'https://192.168.0.12/oa/api/dashboardResults'
wire_network_delay_viavidotcom_results = session.post(wire_network_delay_viavidotcom_resultsurl, headers=headers, data=json.dumps(wire_network_delay_viavidotcom_dashboard), verify=False)
wire_network_delay_viavidotcom_results_text = wire_network_delay_viavidotcom_results.text
#print('wire_network_delay_viavidotcom_results_text ', wire_network_delay_viavidotcom_results_text)
wire_network_delay_viavidotcom_results_text_json = json.loads(wire_network_delay_viavidotcom_results_text)

with open ('/home/dennett/scripting2/wire_network_delay_viavidotcom.json', 'w') as json_file:
    json.dump(wire_network_delay_viavidotcom_results_text_json, json_file)
