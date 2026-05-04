import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Load model + columns
# -------------------------------
model = pickle.load(open('model/car_price_model.pkl', 'rb'))
model_columns = pickle.load(open('model/model_columns.pkl', 'rb'))

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(page_title="Car Price Predictor", layout="centered")

# -------------------------------
# Header
# -------------------------------
st.title("🚗 Car Price Predictor")
st.markdown("Predict the resale value of your car using Machine Learning")

st.markdown("---")

# -------------------------------
# Input Section
# -------------------------------
st.markdown("## 📋 Enter Car Details")
st.divider()

col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input("Present Price (in Lakhs)", min_value=0.0)
    kms_driven = st.number_input("Kms Driven", min_value=0)
    owner = st.selectbox("Number of Owners", [0, 1, 2, 3])

with col2:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    car_age = st.slider("Car Age (years)", 0, 20)

st.markdown("---")

# -------------------------------
# Encoding
# -------------------------------
fuel_diesel = 1 if fuel_type == "Diesel" else 0
fuel_petrol = 1 if fuel_type == "Petrol" else 0

seller = 1 if seller_type == "Individual" else 0
trans = 1 if transmission == "Manual" else 0

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Price"):

    if present_price <= 0:
        st.warning("⚠️ Present price should be greater than 0")

    else:
        # Create DataFrame with feature names
        input_data = pd.DataFrame([{
            'Present_Price': present_price,
            'Kms_Driven': kms_driven,
            'Owner': owner,
            'Car_Age': car_age,
            'Fuel_Type_Diesel': fuel_diesel,
            'Fuel_Type_Petrol': fuel_petrol,
            'Seller_Type_Individual': seller,
            'Transmission_Manual': trans
        }])

        # Align with training columns
        input_data = input_data.reindex(columns=model_columns, fill_value=0)

        # Prediction
        with st.spinner("Predicting price..."):
            prediction = model.predict(input_data)

        # Output UI
        st.markdown("## 💰 Estimated Selling Price")

        st.markdown(
            f"""
            <div style="
                background-color:#1e3a2f;
                padding:20px;
                border-radius:10px;
                text-align:center;
                font-size:24px;
                font-weight:bold;
                color:#00ff9f;">
                ₹ {round(prediction[0], 2)} Lakhs
            </div>
            """,
            unsafe_allow_html=True
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built by Animesh Raj | ML Project 🚀")