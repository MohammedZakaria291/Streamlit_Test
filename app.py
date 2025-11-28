import streamlit as st
import numpy as np
import joblib

# ----------------------
# Load Model
# ----------------------
model = joblib.load("best_model_machine_fail.pkl")

# ----------------------
# Streamlit UI
# ----------------------
st.set_page_config(page_title="Predictive Maintenance", layout="wide")
st.title("🚀 Predictive Maintenance Dashboard")
st.markdown("Welcome! Enter your machine data below to predict if maintenance is needed.")

st.markdown("### Input Parameters")

# ----------------------
# Inputs in Columns
# ----------------------
col1, col2, col3 = st.columns(3)

with col1:
    temperature = st.number_input("🌡️ Temperature (°C)", 0.0, 200.0, 50.0)
    vibration = st.number_input("⚡ Vibration Level", 0.0, 50.0, 5.0)
    pressure = st.number_input("💨 Pressure", 0.0, 500.0, 100.0)
    humidity = st.number_input("💧 Humidity (%)", 0.0, 100.0, 50.0)

with col2:
    energy = st.number_input("🔋 Energy Consumption (kWh)", 0.0, 2000.0, 200.0)
    hour = st.slider("⏰ Hour of Operation", 0, 23, 12)
    elapsed = st.number_input("⏳ Elapsed Time (sec)", 0.0, 1e8, 10000.0)
    downtime = st.number_input("📉 Downtime Risk (0–1)", 0.0, 1.0, 0.2)

with col3:
    anomaly = st.selectbox("🚨 Anomaly Flag", [0, 1])
    machine_status = st.selectbox("⚙️ Machine Status", [0, 1, 2])
    failure_type = st.selectbox("💥 Failure Type (encoded)", [0, 1, 2, 3, 4])

# ----------------------
# Predict Button
# ----------------------
st.markdown("---")
if st.button("🔍 Predict"):
    features = np.array([[temperature, vibration, pressure, humidity,
                          energy, hour, elapsed, downtime, anomaly,
                          machine_status, failure_type]])
    
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ Warning: Maintenance Required!")
        st.markdown("**Action:** Please schedule maintenance immediately to prevent failure.")
    else:
        st.success("✅ Machine Operating Normally")
        st.markdown("**Status:** No immediate maintenance needed. Keep monitoring.")

# ----------------------
# Footer
# ----------------------
st.markdown("---")
st.markdown("📊 Powered by Machine Learning | Predictive Maintenance Dashboard")
