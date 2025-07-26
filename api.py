# FastAPI app to serve the random forest model
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import os
import joblib

app = FastAPI()

# Load the model at startup
model = joblib.load("random_forest_model.pkl")

# Define the input schema with only the required features
class RainfallFeatures(BaseModel):
    temparature: float
    humidity: float
    cloud: float
    sunshine: float
    wind_direction: float

@app.post('/predict')
def predict(features: RainfallFeatures):
    # Prepare input for the model
    X = np.array([[features.temparature, features.humidity, features.cloud, features.sunshine, features.wind_direction]])
    prediction = model.predict(X)
    message = "yes Rain is Possibble" if prediction[0] == 1 else "No Rain is not Possibble"
    return {"predicted_rainfall": message}  # ✅ send as a JSON dict