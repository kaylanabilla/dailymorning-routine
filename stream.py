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
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0w7bPPydb85g4_rzhnA5lH83R4u26gyTgAg&s/">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT89etFye2O3VK0stzF7l_jgCFgkLceV1Wpgw&s/">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqhJuoaZ3vW4uxaHmMqHPT-ZyzQwSsNidw0A&s/">
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

        # ===================== PESAN & QUOTES OTOMATIS ======================
        if prediction < 4:
            message = "😴 Kamu butuh istirahat lebih dan rutinitas kecil bisa bantu ningkatin mood! Semangat ya ❤️"
            quote = "🌿 *“Take a deep breath. You’re getting there, even if it's slow.”*"
        elif prediction < 7:
            message = "😊 Produktivitas kamu sudah lumayan! Terus jaga konsistensi rutinitas pagimu ya ✨"
            quote = "✨ *“Small progress is still progress. Keep going.”*"
        else:
            message = "🔥 Kamu produktif banget hari ini! Rutinitas pagimu sudah keren — pertahankan! 💪"
            quote = "🌞 *“You are capable of amazing things.”*"

        # ===================== TAMPILKAN DI WEB ======================
        st.markdown(f"""
            <div class='result-box'>
                Prediksi Productivity Score kamu adalah:
                <br><br>
                <span style='font-size:30px; font-weight:700;'>⭐ {prediction:.2f} / 10</span>
                <br><br>
                <span style='font-size:18px;'>{message}</span>
                <br><br>
                <span style='font-size:16px; opacity:0.9;'><i>{quote}</i></span>
            </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error("Terjadi error saat memproses prediksi.")
        st.error(str(e))
