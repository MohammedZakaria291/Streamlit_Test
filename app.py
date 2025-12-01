import streamlit as st
import pickle
import pandas as pd

# ===========================
# تحميل المودل فقط
# ===========================
model = pickle.load(open("best_model_machine_fail.pkl", "rb"))

st.set_page_config(page_title="Predictive Maintenance", layout="centered")
st.title("🛠️ Predictive Maintenance System")
st.markdown("أدخل قراءات حساسات الماكينة للتنبؤ بحالة الصيانة")

# ===========================
# إدخال البيانات من المستخدم
# ===========================
st.sidebar.header("📊 مدخلات الماكينة")

temperature = st.sidebar.slider("درجة الحرارة", 1.0, 50.0, 25.0)
vibration   = st.sidebar.slider("الاهتزاز", 48.0, 102.0, 75.0)
humidity    = st.sidebar.slider("الرطوبة", 30.0, 80.0, 55.0)
pressure    = st.sidebar.slider("الضغط", 1.0, 5.0, 3.0)
energy      = st.sidebar.slider("استهلاك الطاقة", 0.5, 5.0, 2.5)
machine_status = st.sidebar.selectbox("حالة الماكينة", [0, 1, 2])
anomaly_flag   = st.sidebar.selectbox("علم الشذوذ", [0, 1])
downtime_risk  = st.sidebar.selectbox("مخاطر التوقف", [0, 1])
machine_id     = st.sidebar.number_input("رقم الماكينة", min_value=1, max_value=999, value=100)

# ===========================
# بناء الـ DataFrame بنفس ترتيب التدريب
# ===========================
features = ['temperature', 'vibration', 'humidity', 'pressure',
            'energy_consumption', 'machine_status', 'anomaly_flag', 
            'downtime_risk', 'machine_id']

data = {
    'temperature': temperature,
    'vibration': vibration,
    'humidity': humidity,
    'pressure': pressure,
    'energy_consumption': energy,
    'machine_status': machine_status,
    'anomaly_flag': anomaly_flag,
    'downtime_risk': downtime_risk,
    'machine_id': machine_id
}

df = pd.DataFrame([data])

# One-hot encoding للـ machine_id زي ما عملت في التدريب
df = pd.get_dummies(df, columns=['machine_id'], drop_first=False)
df = df.reindex(columns=model.feature_names_in_, fill_value=0)  # مهم جدًا

# ===========================
# التنبؤ
# ===========================
prob = model.predict_proba(df)[0][1]
threshold = 0.3

st.subheader("🔍 نتيجة التنبؤ")
if prob >= threshold:
    st.error("⚠️ الماكينة تحتاج صيانة عاجلة!")
else:
    st.success("✅ الماكينة في حالة طبيعية")

st.metric("احتمالية العطل", f"{prob*100:.2f}%")

# معلومات إضافية
with st.expander("عرض التفاصيل التقنية"):
    st.write("البيانات المدخلة:", data)
    st.write("الشكل بعد الـ One-Hot:", df.shape)
    st.write(df.head())
