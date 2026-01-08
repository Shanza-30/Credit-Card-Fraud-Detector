import streamlit as st
import numpy as np
import time
import pandas as pd

# ================= Page Config =================
st.set_page_config(
    page_title="Credit Card Fraud Detector",
    layout="wide",
    page_icon="💳"
)

# ================= Session State =================
if "history" not in st.session_state:
    st.session_state.history = []

# ================= Sidebar =================
st.sidebar.title("📌 About App")
st.sidebar.info("""
This Credit Card Fraud Detection app predicts 
whether a transaction is **Fraudulent** or **Legitimate**.

""")

st.sidebar.markdown("### ⚙ Settings")
threshold = st.sidebar.slider(
    "Fraud Probability Threshold",
    0.50, 0.95, 0.75
)

st.sidebar.markdown("---")
st.sidebar.write("👩‍💻 Developed by **Shanza Shakeel**")

# ================= Main UI =================
st.markdown("<h1 style='text-align:center'>💳 Credit Card Fraud Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Enter transaction details below to detect fraud</p>", unsafe_allow_html=True)
st.markdown("---")

# ================= Inputs =================
st.subheader("📝 Enter Transaction Details")

amount = st.slider("💰 Transaction Amount", 0, 100000, 500)

features = []
for i in range(0, 30, 2):
    col1, col2 = st.columns(2)
    with col1:
        val1 = st.number_input(f"Feature {i+1}", value=0.0, format="%.2f")
    with col2:
        val2 = st.number_input(f"Feature {i+2}", value=0.0, format="%.2f")
    features.extend([val1, val2])

# ================= Buttons =================
colA, colB = st.columns(2)

with colA:
    predict_btn = st.button("🔍 Predict Fraud")

with colB:
    reset_btn = st.button("🔄 Reset")

if reset_btn:
    st.session_state.history = []
    st.rerun()

# ================= Prediction =================
if predict_btn:
    with st.spinner("🔄 Analyzing transaction..."):
        time.sleep(2)

    try:
        features_np = np.array(features).reshape(1, -1)

        # ---- Dummy Logic (Replace with ML Model) ----
        probability = np.random.uniform(0.6, 0.98)

        if probability >= threshold:
            prediction = "❌ Fraudulent Transaction"
            color = "#ffcccc"
        else:
            prediction = "✅ Legitimate Transaction"
            color = "#ccffcc"

        # ================= Result UI =================
        st.markdown(
            f"""
            <div style='padding:20px; background-color:{color};
            border-radius:12px; text-align:center; font-size:20px;'>
            {prediction}<br>
            <b>Fraud Probability:</b> {probability:.2%}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Progress Bar
        st.markdown("### 📊 Risk Level")
        st.progress(min(int(probability * 100), 100))

        # Save History
        st.session_state.history.append({
            "Amount": amount,
            "Probability": f"{probability:.2%}",
            "Result": prediction
        })

    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")

# ================= History =================
if st.session_state.history:
    st.markdown("---")
    st.subheader("📁 Prediction History")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)

# ================= Footer =================
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>AI/ML Project • Streamlit App • Fraud Detection</p>",
    unsafe_allow_html=True
)
