# 🚗 Car Dheko - Used Car Price Prediction

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest%20Regressor-blueviolet)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20App-brightgreen)
![Status](https://img.shields.io/badge/Status-Deployed-orange)

---

## 📘 Project Overview

Accurately pricing used cars is a challenging task due to multiple influencing factors such as mileage, age, engine, and ownership history.  
This project uses **Machine Learning** to develop a reliable **Used Car Price Prediction System** and deploys it as a **user-friendly Streamlit web application**.

---

## 🎯 Objective

- 🎯 Build a predictive model using historical car data
- 📈 Use **Random Forest Regressor** for optimal performance
- 🖥️ Deploy the model via **Streamlit** for real-time price predictions
- 💼 Assist customers & dealers in making informed pricing decisions

---

## 🧠 Approach

### 1️⃣ Data Collection & Preprocessing
- Combined multiple datasets with car listings  
- Handled missing values and standardized formats  
- Encoded categorical variables (e.g. Fuel Type, Transmission)  
- Scaled numerical features like Mileage and Engine size

### 2️⃣ Exploratory Data Analysis (EDA)
- Visualized relationships between price and features  
- Feature selection using correlation analysis  
- Detected outliers and handled skewed distributions

### 3️⃣ Model Development & Tuning
- Models evaluated: Random Forest, Gradient Boosting  
- Best Model: ✅ `RandomForestRegressor`  
- Hyperparameter tuning:
  - `max_depth = 20`
  - `min_samples_leaf = 2`
  - `min_samples_split = 5`
  - `n_estimators = 20`

### 4️⃣ Model Evaluation

| Metric | Value |
|--------|-------|
| **R² Score** | 0.839 |
| **MAE** (Mean Absolute Error) | 102,439.42 |
| **MSE** (Mean Squared Error) | 38,069,331,487.95 |

---

## 🔍 Important Features Used

- `Fuel_Type`: Petrol, Diesel, etc. – affects running cost  
- `Body_Type`: SUV, Sedan – impacts market value  
- `Transmission_type`: Auto or Manual – automatics typically priced higher  
- `Mileage_km`, `Engine`, `Max_Power`, `Torque`: Vehicle specs  
- `Number_owner`: Fewer owners = better resale value  
- `Age_of_car`: Depreciation based on year of manufacture  
- `Seats`: Usage for family vs commercial  
- **🎯 Target Variable:** `Price`

---

## 🖥️ Application Interface

- Built using **Streamlit**  
- Upload a car’s specifications and instantly receive a **predicted price**  
- Designed for both **sales teams** and **customers**  
- Easy to use, intuitive interface with dropdowns, sliders & outputs

---
