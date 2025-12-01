import streamlit as st
import pickle
import pandas as pd

# ========================= تحميل الملفات =========================
model   = pickle.load(open("maintenance_required.pkl", "rb"))
scaler  = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ========================= إعداد الصفحة =========================
st.set_page_config(page_title="Predictive Maintenance", layout="centered")
st.title("نظام التنبؤ بالصيانة الوقائية")
st.markdown("### أدخل قراءات الماكينة وسيتم التنبؤ بحالتها فوراً")

# ========================= الإدخال =========================
temperature      = st.sidebar.slider("درجة الحرارة", 1.0, 50.0, 28.0, key='temperature')
vibration        = st.sidebar.slider("الاهتزاز", 48.0, 102.0, 70.0, key='vibration')
humidity         = st.sidebar.slider("الرطوبة", 30.0, 80.0, 50.0, key='humidity')
pressure         = st.sidebar.slider("الضغط", 1.0, 5.0, 3.0, key='pressure')
energy           = st.sidebar.slider("استهلاك الطاقة", 0.5, 5.0, 2.8, key='energy')
machine_status   = st.sidebar.selectbox("حالة الماكينة", [0, 1, 2], index=0, key='machine_status')
anomaly_flag     = st.sidebar.selectbox("علم الشذوذ", [0, 1], index=0, key='anomaly_flag')
downtime_risk    = st.sidebar.selectbox("مخاطر التوقف", [0, 1], index=0, key='downtime_risk')
machine_id       = st.sidebar.number_input("رقم الماكينة", min_value=1, max_value=999, value=100, key='machine_id')

# ========================= بناء الإدخال =========================
input_data = pd.DataFrame([{
    'temperature': temperature,
    'vibration': vibration,
    'humidity': humidity,
    'pressure': pressure,
    'energy_consumption': energy,
    'machine_status': machine_status,
    'anomaly_flag': anomaly_flag,
    'downtime_risk': downtime_risk,
    'machine_id': machine_id
}])

# One-hot encoding للـ machine_id
input_data = pd.get_dummies(input_data, columns=['machine_id'])

# ترتيب الأعمدة زي التدريب بالظبط
input_data = input_data.reindex(columns=columns, fill_value=0)

# Scaling
input_scaled = scaler.transform(input_data)

# ========================= التنبؤ =========================
prob = model.predict_proba(input_scaled)[0][1]
threshold = 0.35

st.subheader("نتيجة التنبؤ")
if prob >= threshold:
    st.markdown(f"❌ **تحتاج صيانة عاجلة! احتمال: {prob*100:.2f}%**")
    st.warning("الماكينة في حالة خطر")
else:
    st.markdown(f"✅ **الماكينة في حالة ممتازة! احتمال الحاجة للصيانة: {prob*100:.2f}%**")
    st.balloons()

st.metric("احتمالية الحاجة للصيانة", f"{prob*100:.2f}%")

# ========================= اختبار سريع =========================
with st.expander("جرب حالات جاهزة"):
    col1, col2 = st.columns(2)
    with col1:
        if st.button("حالة طبيعية تمام"):
            st.session_state.temperature      = 25
            st.session_state.vibration        = 72
            st.session_state.humidity         = 52
            st.session_state.pressure         = 3.1
            st.session_state.energy           = 2.6
            st.session_state.machine_status   = 0
            st.session_state.anomaly_flag     = 0
            st.session_state.downtime_risk    = 0
            st.session_state.machine_id       = 150
            st.experimental_rerun()
    with col2:
        if st.button("حالة عطل وشيك"):
            st.session_state.temperature      = 47
            st.session_state.vibration        = 98
            st.session_state.humidity         = 76
            st.session_state.pressure         = 4.7
            st.session_state.energy           = 4.8
            st.session_state.machine_status   = 2
            st.session_state.anomaly_flag     = 1
            st.session_state.downtime_risk    = 1
            st.session_state.machine_id       = 777
            st.experimental_rerun()
