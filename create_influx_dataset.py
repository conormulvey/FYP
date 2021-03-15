# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 04:47:11 2021

@author: conor
"""

import pandas as pd
import numpy as np
from datetime import datetime
from influxdb import InfluxDBClient
import time

# dt = datetime.now()
# timestamp = time.mktime(dt.timetuple()) + dt.microsecond/1e6

# print(timestamp)

client = InfluxDBClient(host='localhost', port="8086")

client.create_database('pyexample')

print(client.get_list_database())

client.switch_database('pyexample')

testset = pd.read_csv('human_activity_raw_sensor_data/sensor_sample_float.csv', nrows=10)

for i in range(len(testset)):
    
    print(pd.to_datetime(testset["timestamp"], unit='ns'))
    
    json_body = [{
        "measurement": "Multiple_sensor_readings",
        "tags": {
            "site_name": "Nans House",
            "asset": "Water resevoir",
          },

        "fields": {
            "value": testset["value"][i],
            "value_id": testset["value_id"][i],
            "sensor_id": testset["sensor_id"][i]
        }
    }]
    
    client.write(json_body,protocol='json')

# json_body = [
#     {
#         "measurement": "brushEvents",
#         "tags": {
#             "user": "Carol",
#             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#         },
#         "time": "2018-03-28T8:01:00Z",
#         "fields": {
#             "duration": 127
#         }
#     },
#     {
#         "measurement": "brushEvents",
#         "tags": {
#             "user": "Carol",
#             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#         },
#         "time": "2018-03-29T8:04:00Z",
#         "fields": {
#             "duration": 132
#         }
#     },
#     {
#         "measurement": "brushEvents",
#         "tags": {
#             "user": "Carol",
#             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#         },
#         "time": "2018-03-30T8:02:00Z",
#         "fields": {
#             "duration": 129
#         }
#     }
# ]

# print(json_body)

# client.write_points(json_body,'test_sensor_data')

# results = client.query('SELECT "sensor_id" FROM "test_sensor_data" WHERE sensor_id = 6222')

# print(results)

# df = pd.read_csv('human_activity_raw_sensor_data/sensor_sample_float.csv', nrows=10, parse_dates=['timestamp'])

# df['timestamp'] = pd.to_timedelta(df['timestamp'])

# time = df["timestamp"].dt.total_seconds()

# print(time)


# lines = [ "price" + ",type=BTC" + " " 
#          + "value=" + str(df["value_id"][d]) + "," 
#          + "sensor=" + str(df["sensor_id"][d]) + ","
#          + "value=" + str(df["value"][d])
#          + " " + str(df["timestamp"][d]) for d in range(len(df))]

# thefile = open('D:/FYP_V1/chronograf.txt', 'w')
# for item in lines:
#     thefile.write("%s\n" % item)