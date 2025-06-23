import streamlit as st
import pickle
import numpy as np
import os

# Load the model with error handling
model_path = "D:\\Anaconda Navigator\\Projects\\3.CarDheko\\best_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found. Please check the path and try again.")
    st.stop()

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f" Error loading model: {e}")
    st.stop()

# Feature names in the required order
features = [
    'fuel_type', 'body_type', 'mileage_km', 'transmission', 'number_owner', 
    'mileage', 'engine_power', 'Max Power', 'torque_car', 'seats_car', 'age_of_car'
]

# Categorical variable mappings
categorical_mappings = {
    'fuel_type': {'Petrol': 0, 'Diesel': 1, 'CNG': 2, 'Electric': 3, 'LPG': 4},
    'body_type': {'Hatchback': 0, 'Sedan': 1, 'SUV': 2, 'MUV': 3, 'Minivans': 4,
                  'Coupe': 5, 'Convertibles': 6, 'Pickup Trucks': 7, 'Hybrids': 8, 'Wagon': 9},
    'transmission': {'Manual': 0, 'Automatic': 1},
}

# Streamlit UI
st.title(" Car Price Prediction Application")

st.sidebar.header("📊 Input Car Details")

# Collect user inputs in the required order
input_data = {}

for feature in features:
    if feature in categorical_mappings:
        selected_option = st.sidebar.selectbox(f"Select {feature.replace('_', ' ').capitalize()}:", 
                                               options=list(categorical_mappings[feature].keys()))
        input_data[feature] = categorical_mappings[feature][selected_option]
    else:
        input_data[feature] = st.sidebar.number_input(f"{feature.replace('_', ' ').capitalize()}:", value=0.0)

# Make predictions using the model
if st.sidebar.button("🔮 Predict"):
    try:
        input_array = np.array([input_data[feature] for feature in features]).reshape(1, -1)
        prediction = model.predict(input_array)

        # Display the selected feature values
        st.subheader("🔍 Selected Features:")
        for feature, value in input_data.items():
            st.write(f"**{feature.replace('_', ' ').capitalize()}**: {value}")

        # Display the prediction result
        st.subheader("📊 Prediction Result:")
        st.success(f"🚘 The estimated car price is: **INR {prediction[0]:,.2f}**")
    
    except Exception as e:
        st.error(f"❌ Error in prediction: {e}")
