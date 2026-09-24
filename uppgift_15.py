# uppgift_15.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('linreg_model.joblib')
# scaler = joblib.load('scaler.joblib')  # ← COMMENT THIS OUT OR DELETE

st.title("Bilprispredikator")

Year = st.number_input("Årsmodell", min_value=1990, max_value=2026, value=2015)
Engine_Size = st.number_input("Motorstorlek (L)", min_value=1.0, max_value=6.0, value=2.5, step=0.1)
Mileage = st.number_input("Miltal (km)", min_value=0, value=50000, step=1000)
Doors = st.number_input("Antal dörrar", min_value=2, max_value=5, value=4)
Owner_Count = st.number_input("Antal ägare", min_value=0, max_value=5, value=1)


transmission = st.selectbox(
    "Växellåda",
    ["Automatic", "Manual", "Semi-Automatic"],
    index=0
)
Transmission_Manual = 1 if transmission == "Manual" else 0
Transmission_Semi_Automatic = 1 if transmission == "Semi-Automatic" else 0

fuel_type = st.selectbox(
    "Bränsletyp",
    ["Diesel", "Electric", "Hybrid", "Petrol"],
    index=0
)
Fuel_Type_Electric = 1 if fuel_type == "Electric" else 0
Fuel_Type_Hybrid = 1 if fuel_type == "Hybrid" else 0
Fuel_Type_Petrol = 1 if fuel_type == "Petrol" else 0


brand = st.selectbox(
    "Bilmärke",
    ["Honda", "Hyundai", "Kia", "Toyota", "Volkswagen"],
    index=0
)
Brand_Honda = 1 if brand == "Honda" else 0
Brand_Hyundai = 1 if brand == "Hyundai" else 0
Brand_Kia = 1 if brand == "Kia" else 0
Brand_Toyota = 1 if brand == "Toyota" else 0
Brand_Volkswagen = 1 if brand == "Volkswagen" else 0




if st.button("Predicera pris"):
    # Create array with ALL features in correct order
    input_data = np.array([[
        Year,
        Engine_Size,
        Mileage,
        Doors,
        Owner_Count,
        Transmission_Manual,
        Transmission_Semi_Automatic,
        Fuel_Type_Electric,
        Fuel_Type_Hybrid,
        Fuel_Type_Petrol,
        Brand_Honda,
        Brand_Hyundai,
        Brand_Kia,
        Brand_Toyota,
        Brand_Volkswagen
    ]])
    
    # Skip scaling since we removed it
    prediction = model.predict(input_data)
    
    pris = prediction[0][0]
    
    
    st.success(f"## 💵 Predicerat pris: {pris:,.0f} $")