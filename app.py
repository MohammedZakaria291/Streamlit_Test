import streamlit as st
import numpy as np

class FakeModel:
    def predict(self, X):
        return [1]

model = FakeModel()

st.set_page_config(page_title="Predictive Maintenance", layout="wide")

page_bg = """
<style>
.stApp {
    background: linear-gradient(135deg, rgba(24, 28, 41, 0.75) 0%, rgba(15, 32, 39, 0.75) 100%),
                url('https://i.ibb.co/Tx9p2TBV/5866308792830593860.jpg') !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
    background-repeat: no-repeat !important;
    min-height: 100vh !important;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

body, h1, h2, h3, h4, h5, h6, p, div, span {
    color: white !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

.title-animate {
    animation: fadein 2s ease-in-out;
    text-align: center;
    font-size: 36px !important;
    font-weight: 900 !important;
    text-shadow: 0px 0px 20px #00eaff;
    background: rgba(0, 0, 0, 0.7) !important;
    padding: 18px !important;
    border-radius: 12px !important;
    margin: 15px 0 !important;
    border: 2px solid #00eaff !important;
    backdrop-filter: blur(5px) !important;
    line-height: 1.1 !important;
}

@keyframes fadein {
    from {opacity: 0; transform: translateY(-30px);}
    to   {opacity: 1; transform: translateY(0);}
}

.stNumberInput input {
    color: #000000 !important;
    font-weight: bold !important;
    background: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid #00eaff !important;
    border-radius: 8px !important;
    padding: 10px !important;
    font-size: 14px !important;
    transition: all 0.3s ease !important;
}

.stNumberInput input:focus {
    transform: scale(1.02) !important;
    box-shadow: 0 0 15px rgba(0, 234, 255, 0.5) !important;
}

.stMarkdown h3 {
    color: white !important;
    font-weight: bold !important;
    font-size: 20px !important;
    margin-bottom: 12px !important;
    text-shadow: 0px 0px 10px rgba(0, 234, 255, 0.5);
}

.stMarkdown h2 {
    color: white !important;
    font-weight: bold !important;
    font-size: 26px !important;
    text-shadow: 0px 0px 15px rgba(0, 234, 255, 0.5);
}

.main .block-container {
    background: rgba(0, 0, 0, 0.7) !important;
    padding: 30px !important;
    border-radius: 18px !important;
    margin-top: 15px !important;
    backdrop-filter: blur(8px) !important;
    border: 1px solid rgba(0, 234, 255, 0.3) !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4) !important;
}

.stButton button {
    background: linear-gradient(45deg, #00eaff, #008cff) !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 12px 35px !important;
    font-size: 16px !important;
    border-radius: 10px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0, 234, 255, 0.4) !important;
    margin: 8px 0 !important;
}

.stButton button:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 6px 20px rgba(0, 234, 255, 0.7) !important;
}

.stButton button[key="refresh"] {
    background: linear-gradient(45deg, #ff6b6b, #ffa500) !important;
    box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4) !important;
    padding: 10px 25px !important;
    font-size: 14px !important;
}

.stButton button[key="refresh"]:hover {
    box-shadow: 0 6px 18px rgba(255, 107, 107, 0.7) !important;
}

hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, transparent, #00eaff, transparent) !important;
    margin: 20px 0 !important;
    box-shadow: 0 0 10px rgba(0, 234, 255, 0.5) !important;
}

.stAlert {
    border-radius: 8px !important;
    border: 1px solid rgba(0, 234, 255, 0.3) !important;
    margin: 8px 0 !important;
    font-size: 14px !important;
    background: rgba(0, 0, 0, 0.6) !important;
}

.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: 
        radial-gradient(circle at 20% 80%, rgba(0, 234, 255, 0.05) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(0, 140, 255, 0.05) 0%, transparent 50%);
    pointer-events: none;
    z-index: -1;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# زر إعادة التحميل في سطر واحد
if st.button("🔄 Refresh Page", key="refresh"):
    st.rerun()

# العنوان في سطر واحد مع الإيموجي 🏭
st.markdown("<div class='title-animate'>🏭 Predictive Maintenance for Industrial Equipment 🏭</div>", unsafe_allow_html=True)
st.markdown("## 🔍 Machine Failure Prediction")
st.markdown("---")
st.markdown("## 📝 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌡️ Temperature (°C)")
    temperature = st.number_input("", 0.0, 200.0, 50.0, key="temp1")
    
    st.markdown("### ⚡ Vibration Level (mm/s)")
    vibration = st.number_input("", 0.0, 50.0, 5.0, key="vib1")
    
    st.markdown("### 💨 Pressure (bar)")
    pressure = st.number_input("", 0.0, 500.0, 100.0, key="press1")

with col2:
    st.markdown("### 💧 Humidity (%)")
    humidity = st.number_input("", 0.0, 100.0, 50.0, key="hum1")
    
    st.markdown("### 🔋 Energy Consumption (kWh)")
    energy = st.number_input("", 0.0, 2000.0, 200.0, key="energy1")

st.markdown("---")

# زر التحليل
if st.button("🚀 Analyze Equipment Status", key="analyze"):
    features = np.array([[temperature, vibration, pressure, humidity, energy]])
    out = model.predict(features)[0]

    # النتيجة بدون مربع أسود
    if out == 1:
        st.error("⚠️ Maintenance Required!")
        st.warning("🔧 Immediate attention needed for equipment maintenance")
    else:
        st.success("✅ Machine Normal")
        st.info("📊 All parameters are within normal operating range")

st.markdown("---")