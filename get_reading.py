# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 07:14:26 2021

@author: conor
"""
from influxdb import InfluxDBClient
import random
import sys 
import pandas as pd

def getReading():
    
    client = InfluxDBClient(host='localhost', port=8086, database='sensor_readings')
    
    results = client.query('SELECT * FROM "sensor_readings"')

    print(results.raw)

    points = results.get_points()
    
    print(points)

    for point in points:
        print('point')
    
    # testset = pd.read_csv('human_activity_raw_sensor_data/sensor_sample_float.csv', nrows=10)
    
    # i = random.randint(1,10)
    
    # json_body = [{
    #     "measurement": "Multiple_sensor_readings",
    #     "tags": {
    #         "site_name": "Nans House",
    #         "asset": "Water resevoir",
    #       },
    #     "time": "2018-03-29T8:04:00Z",
    #     "fields": {
    #         "value": testset["value"][i],
    #         "value_id": testset["value_id"][i],
    #         "sensor_id": testset["sensor_id"][i]
    #     }
    # }]
    
    # return json_body

if __name__ == "__main__":
    getReading()