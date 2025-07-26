import streamlit as st
import requests

st.title("Rainfall Prediction App")

st.write("Enter the following weather features to predict rainfall:")

temparature = st.number_input("Temperature", value=18.0)
humidity = st.number_input("Humidity", value=70)
cloud = st.number_input("Cloud", value=50)
sunshine = st.number_input("Sunshine", value=5.0)
wind_direction = st.number_input("Wind Direction", value=40.0)

if st.button("Predict"):
    data = {
        "temparature": temparature,
        "humidity": humidity,
        "cloud": cloud,
        "sunshine": sunshine,
        "wind_direction": wind_direction
    }
    try:
        response = requests.post("http://localhost:8000/predict", json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Rainfall: {result['predicted_rainfall']}")
        else:
            st.error(f"API Error: {response.text}")
    except Exception as e:
        st.error(f"Connection error: {e}")
