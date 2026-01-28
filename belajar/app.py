import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Nasgor", layout="centered")

# --- HEADER (Sesuai Desain Figma Kamu) ---
st.title("📊 Dashboard Penjualan Nasi Goreng Ayah")
st.write("Aplikasi untuk memprediksi stok porsi terjual.")

# --- INPUT DATA (Sesuai Desain Figma Kamu) ---
st.subheader("Input Data")
col1, col2 = st.columns(2)

with col1:
    stok_telur = st.number_input("Stok Telur Tersedia", min_value=0, value=50)

with col2:
    is_weekend = st.selectbox("Apakah Hari Ini Weekend?", ["Tidak", "Ya"])

# Konversi input menjadi angka untuk AI
weekend_val = 1 if is_weekend == "Ya" else 0

# --- LOGIKA AI SEDERHANA ---
# Data historis untuk melatih mesin
data = {
    'jumlah_telur': [20, 22, 25, 18, 30, 35, 40, 21, 23],
    'is_weekend': [0, 0, 0, 0, 1, 1, 0, 0, 0],
    'porsi_terjual': [40, 45, 50, 38, 65, 75, 85, 42, 47]
}
df = pd.DataFrame(data)

# Melatih model
model = LinearRegression()
model.fit(df[['jumlah_telur', 'is_weekend']], df['porsi_terjual'])

# --- TOMBOL PREDIKSI ---
if st.button("🚀 Prediksi Terjual"):
    prediksi = model.predict([[stok_telur, weekend_val]])
    hasil = int(prediksi[0])
    
    # Tampilkan hasil besar (UI/UX)
    st.metric(label="Prediksi Porsi Terjual", value=f"{hasil} Porsi")
    
    if hasil > 100:
        st.warning("⚠️ Stok telur banyak dan weekend! Siapkan tenaga ekstra.")
    else:
        st.success("✅ Penjualan diperkirakan normal.")

# --- GRAFIK PENJUALAN ---
st.subheader("📈 Tren Penjualan")
st.line_chart(df['porsi_terjual'])

st.subheader("🔊 Baca Pesanan WhatsApp")
pesanan_teks = st.text_area("Tempel (Paste) Chat WA di sini", placeholder="Contoh: Nasgor 2 porsi pedes")

if st.button("Dengarkan Pesanan"):
    if pesanan_teks:
        from gtts import gTTS
        import base64
        
        # Mengubah teks jadi suara Bahasa Indonesia
        tts = gTTS(text=pesanan_teks, lang='id')
        tts.save("pesanan.mp3")
        
        # Menampilkan pemutar audio di website
        audio_file = open("pesanan.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
        st.success("Klik tombol play di atas untuk mendengar pesanan!")
    else:

        st.error("Silakan tempel teks pesanan dulu!")
