# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:54:54 2021

@author: conor
"""

from flask import Flask, request, jsonify
import joblib 
import traceback
import get_reading
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/flask',methods=['GET','POST'])
def predict():
    
    # If the model is loaded in
    if clf:
        try:
            
            #Query the database for data
            #Currently returns values relevant to the model from all entries in the database
            json_ = get_reading.getReading() 
            
            # get_dummies will enter summy data into any null values to avoid errors with the model
            query = pd.get_dummies(pd.DataFrame(json_))
            
            # if the queried data is missing a column do to incomlete data, reindex will fix it
            query = query.reindex(columns=model_columns, fill_value=0)
            
            prediction = list(clf.predict(query))
            
            return jsonify({'prediction': str(prediction)})
    
        except:
            return jsonify({'trace': traceback.format_exc()})
    
    else:
        print('Train Model')
        return ('No model here')

if __name__ == "__main__":
    
    # isolationForest_SensorData.py trains a model and saves the model as model.pkl
    clf = joblib.load("model.pkl")
    print("Model Loaded")
    
    # model.pkl doesnt save the column names, so they are saved in a seperate .pkl file in isolationForest_SensorData.py
    model_columns = joblib.load("model_columns.pkl")
    print('Model columns loaded')
    
    app.run(port=5000, debug=True)