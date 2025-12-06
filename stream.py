import pickle
import streamlit as st
import pandas as pd

# ===================== PAGE CONFIG ==========================
st.set_page_config(
    page_title="Prediksi Productivity Score",
    page_icon="✨",
    layout="centered"
)

# ===================== CUSTOM CSS ==========================
st.markdown("""
<style>
/* Background soft */
body {
    background-color: #f7fff7;
}

/* Card */
.container {
    background: #ffffff;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.07);
    margin-top: 25px;
}

/* Title */
h1 {
    color: #2e6f40;
    text-align: center;
    font-weight: 800;
}

/* Labels */
label, .stSelectbox label, .stNumberInput label, .stTextInput label {
    font-weight: 600 !important;
    color: #2f4f2f !important;
}

/* Button */
.stButton>button {
    background-color: #7ac79f;
    color: white;
    padding: 0.6rem 1.2rem;
    border-radius: 12px;
    border: none;
    font-size: 16px;
    transition: 0.2s;
}

.stButton>button:hover {
    background-color: #68b18a;
}

/* Success Box */
.stSuccess {
    border-radius: 12px;
}

/* Input Box styling */
.stTextInput>div>input, 
.stNumberInput>div>input, 
.stSelectbox>div>div>div {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ===================== LOAD MODEL ==========================
model = pickle.load(open('morningdataset_model.sav', 'rb'))

# ====================== TITLE ==========================
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.title('✨ Prediksi Productivity Score – Morning Routine ✨')
st.write("Isi rutinitas pagimu di bawah ini, dan sistem akan memprediksi skor produktivitasmu (1–10).")

# ===================== INPUT FORM ==========================

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
        st.success(f"✨ Prediksi Productivity Score kamu adalah: **{prediction:.2f} / 10** ✨")
    except Exception as e:
        st.error("Terjadi error saat memproses prediksi.")
        st.error(str(e))

st.markdown("</div>", unsafe_allow_html=True)
