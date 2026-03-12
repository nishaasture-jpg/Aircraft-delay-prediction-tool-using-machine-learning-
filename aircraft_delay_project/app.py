import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("aircraft_delay_model.pkl")

# Title
st.title("✈ Aircraft Departure Delay Prediction")

st.write("Enter flight details to predict delay")

# User Inputs
distance = st.number_input("Flight Distance", min_value=0.0)
temp = st.number_input("Temperature")
wind = st.number_input("Wind Speed")
weather = st.number_input("Weather Delay")

# Prediction Button
if st.button("Predict Delay"):

    input_data = np.array([[distance, temp, wind, weather]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Aircraft Delay: {prediction[0]:.2f} minutes")