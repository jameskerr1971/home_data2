from influxdb import InfluxDBClient

client = InfluxDBClient(host='192.168.0.54', port=8086)
client.switch_database('home_data')
json_body = [{"measurement": "cpu", "tags": {"method": "device", "unit": "%", "device": "popper"}, "fields": {"utilisation": 99.0}}]

client.write_points(json_body)

#results = client.query('SELECT "utilisation" FROM "home_data"."autogen"."cpu" WHERE time > now() - 4d')

#print(results)
