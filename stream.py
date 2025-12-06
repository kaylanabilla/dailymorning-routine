import pickle
import streamlit as st
import pandas as pd

# ===================== LOAD MODEL ==========================
model = pickle.load(open('morningdataset_model.sav', 'rb'))

# ====================== TITLE WEB ==========================
st.title('Prediksi Productivity Score – Morning Routine')

st.write("Masukkan rutinitas pagi kamu untuk memprediksi produktivitas (1–10).")

# ===================== INPUT FORM SESUAI FITUR TRAINING ==========================

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

# ===================== KONVERSI KE DATAFRAME ==========================
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
        st.success(f"Prediksi Productivity Score kamu adalah: **{prediction:.2f} / 10**")
    except Exception as e:
        st.error("Terjadi error saat memproses prediksi.")
        st.error(str(e))
