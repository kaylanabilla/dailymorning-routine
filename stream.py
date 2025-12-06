import pickle
import streamlit as st
import pandas as pd

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Morning Routine Productivity",
    page_icon="🌅",
    layout="wide"
)

# ==========================================
# CUSTOM CSS (SUPER PREMIUM)
# ==========================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* Background full */
body {
    background: #f3f8f3;
}

/* Hero Section Background Image */
.hero {
    background-image: url('morning_bg.jpg');
    background-size: cover;
    background-position: center;
    padding: 120px 40px;
    border-radius: 25px;
    color: white;
    text-shadow: 0 4px 18px rgba(0,0,0,0.35);
    margin-bottom: 40px;
    animation: fadeHero 1.3s ease-out;
}

@keyframes fadeHero {
    from {opacity: 0; transform: translateY(-25px);}
    to {opacity: 1; transform: translateY(0);}
}

.hero h1 {
    font-size: 56px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    max-width: 600px;
    opacity: 0.95;
}

/* Form Card */
.form-card {
    background: white;
    padding: 40px;
    border-radius: 22px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.07);
    margin-bottom: 50px;
    animation: fadeUp 0.7s ease-out;
}

@keyframes fadeUp {
    from {opacity: 0; transform: translateY(22px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Form Label */
label {
    font-weight: 600 !important;
    color: #245b3c !important;
}

/* Input boxes */
.stNumberInput > div > input,
.stTextInput > div > input,
.stSelectbox > div > div > div {
    border-radius: 14px !important;
    padding: 12px !important;
    background: #f7fef7 !important;
    border: 2px solid #d9f4d9 !important;
    transition: 0.25s;
}

.stNumberInput > div > input:focus,
.stTextInput > div > input:focus,
.stSelectbox > div > div:hover {
    border-color: #7bcf96 !important;
    box-shadow: 0 0 0 3px rgba(116, 202, 145, 0.3) !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #7dd89c, #56b67a);
    color: white;
    width: 100%;
    border-radius: 14px;
    font-size: 18px;
    font-weight: 600;
    padding: 14px;
    border: none;
    transition: 0.3s;
    box-shadow: 0 6px 20px rgba(0,0,0,0.18);
    margin-top: 25px;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.22);
}

/* Success Box */
.stSuccess {
    border-radius: 14px !important;
}

/* Divider */
.divider {
    height: 2px;
    width: 100%;
    background: linear-gradient(to right, #d7f5df, #7ed9a4, #d7f5df);
    margin: 40px 0;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD MODEL
# ==========================================
model = pickle.load(open('morningdataset_model.sav', 'rb'))

# ==========================================
# HERO SECTION
# ==========================================
st.markdown("""
<div class="hero">
    <h1>🌅 Morning Productivity Predictor</h1>
    <p>Tingkatkan produktivitasmu dengan memahami bagaimana rutinitas pagimu
    mempengaruhi performamu sepanjang hari.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# FORM CARD
# ==========================================
st.markdown("<div class='form-card'>", unsafe_allow_html=True)

st.subheader("📝 Isi Rutinitas Pagi Kamu")

col1, col2 = st.columns(2)

with col1:
    sleep_duration = st.number_input("Sleep Duration (hrs)", min_value=0.0, max_value=24.0, step=0.1)
    meditation = st.number_input("Meditation (mins)", min_value=0, max_value=300)
    exercise = st.number_input("Exercise (mins)", min_value=0, max_value=300)

with col2:
    breakfast = st.selectbox("Breakfast Type", ["Heavy", "Light", "Protein-rich", "Skipped"])
    journaling = st.selectbox("Journaling (Y/N)", ["Y", "N"])
    work_start = st.selectbox("Work Start Time", ["Early", "Normal", "Late"])
    mood = st.selectbox("Mood", ["Bad", "Neutral", "Good"])

notes = st.text_input("Notes", value="None")

# ==========================================
# PREDICTION INPUT
# ==========================================
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

# ==========================================
# PREDICT BUTTON
# ==========================================
if st.button("Prediksi Productivity Score"):
    try:
        result = model.predict(input_df)[0]
        st.success(f"🌟 Productivity Score kamu adalah: **{result:.2f} / 10** 🌟")
    except Exception as e:
        st.error("Terjadi error saat memproses prediksi.")
        st.error(str(e))

st.markdown("</div>", unsafe_allow_html=True)
