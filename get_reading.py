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
    
    json_body = []
    
    #Connect to local influxdb
    #test_sensor_data currently holds 11 entries
    client = InfluxDBClient(host='localhost', port=8086, database='test_sensor_data')
    
    #retrieve all the data from the database
    #returns a json with all 11 entries in it
    results = client.query('SELECT * FROM "Multiple_sensor_readings"')
    
    # print(results.raw)
    
    # print(len(results.raw['series'][0]['values']))
    
    # For loop retirieves values relevant to the prediction from results json
    for i in range(len(results.raw['series'][0]['values'])):

        value = results.raw['series'][0]['values'][i][4]
        
        timestamp = results.raw['series'][0]['values'][i][0]
        
        sensor_id = results.raw['series'][0]['values'][i][2]
    
        json_body.append({"value": value,"timestamp": timestamp,"sensor_id": sensor_id})
    
    # print(json_body)
        
    return json_body

if __name__ == "__main__":
    getReading()