import pickle
import streamlit as st
import pandas as pd

# ===================== PAGE CONFIG ==========================
st.set_page_config(
    page_title="Prediksi Productivity Score",
    page_icon="🌿",
    layout="centered"
)

# ===================== ULTRA PREMIUM CSS ==========================
st.markdown("""
<style>

* {
    font-family: 'Poppins', sans-serif;
}

/* Background Gradient */
body {
    background: linear-gradient(135deg, #d9fdd3 0%, #ffffff 100%) !important;
}

/* Center Container */
.container {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    padding: 35px;
    border-radius: 25px;
    max-width: 820px;
    margin: auto;
    margin-top: 40px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.08);
    border: 1px solid rgba(255,255,255,0.6);
    animation: fadeIn 0.8s ease-out;
}

/* Fade In Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(12px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Title */
h1 {
    text-align: center;
    font-weight: 900;
    color: #1d6f42;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 15px;
    color: #3b5146;
    margin-bottom: 25px;
}

/* Input Label Styling */
label {
    font-weight: 600 !important;
    color: #2e4d35 !important;
}

/* Input Box Style */
.stTextInput > div > input,
.stNumberInput > div > input,
.stSelectbox > div > div > div {
    background: #ffffffc9 !important;
    backdrop-filter: blur(6px);
    border-radius: 14px !important;
    padding: 10px !important;
    border: 2px solid #e6f4e6;
    transition: all 0.25s ease;
}

.stTextInput > div > input:focus,
.stNumberInput > div > input:focus,
.stSelectbox > div > div > div:hover {
    border-color: #83c89a !important;
    box-shadow: 0 0 0 3px rgba(116, 202, 145, 0.3) !important;
}

/* Predict Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #7dd89c, #56b67a);
    color: white;
    padding: 14px;
    border-radius: 15px;
    font-size: 17px;
    font-weight: 600;
    border: none;
    transition: 0.3s ease;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 22px rgba(0,0,0,0.18);
}

/* Success Box */
.stSuccess {
    border-radius: 14px !important;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)


# ===================== LOAD MODEL ==========================
model = pickle.load(open('morningdataset_model.sav', 'rb'))

# ====================== TITLE ==========================
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.title("🌿 Morning Productivity Predictor")
st.markdown("<p class='subtitle'>Masukkan aktivitas pagimu untuk memprediksi skor produktivitas (1–10).</p>", unsafe_allow_html=True)


# ===================== FORM ==========================
col1, col2 = st.columns(2)

with col1:
    sleep_duration = st.number_input("Sleep Duration (hrs)", min_value=0.0, max_value=24.0, step=0.1)
    meditation = st.number_input("Meditation (mins)", min_value=0, max_value=300)
    exercise = st.number_input("Exercise (mins)", min_value=0, max_value=300)

with col2:
    breakfast = st.selectbox("Breakfast Type", 
                             ["Heavy", "Light", "Protein-rich", "Skipped"])
    journaling = st.selectbox("Journaling (Y/N)", ["Y", "N"])
    work_start = st.selectbox("Work Start Time", ["Early", "Normal", "Late"])
    mood = st.selectbox("Mood", ["Bad", "Neutral", "Good"])

notes = st.text_input("Notes", value="None")


# ===================== DATAFRAME ==========================
input_df = pd.DataFrame([{
    "Sleep Duration (hrs)": sleep_duration,
    "Meditation (mins)": meditation,
    "Exercise (mins)": exercise,
    "Breakfast Type": breakfast,
    "Journaling (Y/N)": journaling,
    "Work Start Time": work_start,
    "Mood": mood,
    "Notes": notes
}])

# ===================== PREDIKSI ==========================
if st.button("Prediksi Productivity Score"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🌟 Productivity Score kamu: **{prediction:.2f} / 10** 🌟")
    except Exception as e:
        st.error("Terjadi error saat memproses prediksi.")
        st.error(str(e))

st.markdown("</div>", unsafe_allow_html=True)
