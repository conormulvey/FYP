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

client = InfluxDBClient(host='localhost', port=8086)

client.create_database('pyexample')

client.switch_database('pyexample')

testset = pd.read_csv('human_activity_raw_sensor_data/sensor_sample_float.csv', nrows=10)

for i in range(len(testset)):
    
    # json_body = [{
    #     "measurement": "Multiple_sensor_readings",
    #     "tags": {
    #         "site_name": "Nans House",
    #         "asset": "Water resevoir",
    #       },
    #     "time": "2018-03-29T8:04:00Z",
    #     "fields": {
    #         "value": testset["value"][i],
    #     }
    # }]
    
    json_body = [
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": time.time_ns(),
        "fields": {
            "duration": 127
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": time.time_ns(),
        "fields": {
            "duration": 132
        }
    },
    {
        "measurement": "brushEvents",
        "tags": {
            "user": "Carol",
            "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": time.time_ns(),
        "fields": {
            "duration": 129
        }
    }
    ]

print(json_body)
 
client.write_points(json_body)

results = client.query('SELECT * FROM "pyexample"')

print(results.raw)

points = results.get_points("Multiple_sensor_readings")

for point in points:
    print('point')
