import pickle
import streamlit as st
import pandas as pd

# ===================== LOAD MODEL ==========================
model = pickle.load(open('morningdataset_model.sav', 'rb'))

# ===================== CUSTOM CSS SUPER AESTHETIC ==========================
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #c8f7dc, #e9fff4);
            font-family: 'Poppins', sans-serif;
        }

        .header-gallery {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 25px;
            flex-wrap: wrap;
        }

        .header-gallery img {
            width: 30%;
            max-width: 180px;
            border-radius: 18px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.15);
            object-fit: cover;
        }

        @media(max-width: 600px){
            .header-gallery img {
                width: 28%;
                max-width: 110px;
            }
        }

        .title-box {
            text-align: center;
            padding: 10px;
            margin-bottom: 10px;
        }
        .title-box h1 {
            font-size: 36px;
            font-weight: 800;
            color: #2f6f4e;
        }

        .card {
            background: #ffffffdd;
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
            margin-bottom: 25px;
        }

        label {
            font-weight: 600 !important;
            color: #2f6f4e !important;
        }

        .stButton>button {
            background: linear-gradient(90deg, #4fd19c, #58e4b0);
            color: white;
            font-weight: 700;
            padding: 0.7rem 1rem;
            border-radius: 12px;
            border: none;
            width: 100%;
            box-shadow: 0 4px 14px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #3cb681, #4fd19c);
            transform: scale(1.02);
        }

        .result-box {
            background: #dffff0;
            border-left: 6px solid #4fd19c;
            padding: 18px;
            border-radius: 15px;
            font-size: 20px;
            color: #2f6f4e;
            font-weight: 600;
            box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        }
    </style>
""", unsafe_allow_html=True)

# ====================== 3 SMALL AESTHETIC HEADER IMAGES ==========================
st.markdown("""
    <div class="header-gallery">
        <img src="data:image/jpeg;base64,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/">
        <img src="https://id.pinterest.com/pin/23503229299805423/">
        <img src="https://id.pinterest.com/pin/23503229299805714/">
    </div>
""", unsafe_allow_html=True)

# ====================== TITLE ==========================
st.markdown("""
<div class="title-box">
    <h1>🌿 Morning Routine – Productivity Predictor</h1>
    <p style="color:#45785a; font-size:18px; margin-top:-10px;">
        Masukkan rutinitas pagimu untuk memprediksi tingkat produktivitas harian.
    </p>
</div>
""", unsafe_allow_html=True)

# ===================== INPUT FORM ==========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

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

st.markdown("</div>", unsafe_allow_html=True)

# ===================== PREDIKSI ==========================
if st.button("Prediksi Productivity Score"):
    try:
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

        prediction = model.predict(input_df)[0]

        st.markdown(f"""
            <div class='result-box'>
                Prediksi Productivity Score kamu adalah:
                <br><br>
                <span style='font-size:28px;'>⭐ {prediction:.2f} / 10</span>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error("Terjadi error saat memproses prediksi.")
        st.error(str(e))
