import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("Real estate valuation data set.csv")
df.drop(columns=['No'], inplace=True)

# Prepare features and target
X = df.drop('Y house price of unit area', axis=1)
y = df['Y house price of unit area']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=21)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ============== Streamlit UI ============== #

# Sidebar
st.sidebar.title("📌 About this App")
st.sidebar.info("""
This app predicts **real estate price per unit area** based on property features.
Built using **Linear Regression** trained on a Taiwan housing dataset.
""")

st.sidebar.markdown("---")
st.sidebar.write("📊 Features Used:")
st.sidebar.markdown("""
- Transaction Date  
- House Age  
- Distance to MRT  
- Number of Convenience Stores  
- Latitude  
- Longitude
""")


# Main title
st.markdown("<h1 style='text-align: center; color: crimson;'>🏠 Real Estate Price Predictor</h1>", unsafe_allow_html=True)
st.write("Enter the property details below:")

# Input layout in columns
col1, col2 = st.columns(2)

with col1:
    transaction_date = st.number_input("📅 Transaction Date", min_value=2012.0, max_value=2014.0, value=2013.0)
    house_age = st.number_input("🏡 House Age (years)", min_value=0.0, max_value=100.0, value=10.0)
    mrt_dist = st.number_input("🚇 Distance to MRT (meters)", min_value=0.0, value=500.0)

with col2:
    convenience_stores = st.number_input("🛒 Convenience Stores Nearby", min_value=0, value=5)
    latitude = st.number_input("🧭 Latitude", min_value=20.0, max_value=30.0, value=24.96)
    longitude = st.number_input("📍 Longitude", min_value=120.0, max_value=130.0, value=121.5)

# Predict
if st.button("🔍 Predict Price"):
    input_data = np.array([[transaction_date, house_age, mrt_dist, convenience_stores, latitude, longitude]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.markdown("---")
    st.markdown(f"<h3 style='text-align: center; color: green;'>🏷️ Predicted House Price per Unit Area: <br> <strong>{prediction:.2f}</strong></h3>", unsafe_allow_html=True)




