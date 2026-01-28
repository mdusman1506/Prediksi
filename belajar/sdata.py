import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Ambil data yang sudah kita buat tadi
df = pd.read_csv('data_nasgor.csv')
X = df[['jumlah_telur']] # Kita fokus ke hubungan Telur vs Porsi dulu agar grafiknya 2D
y = df['porsi_terjual']

# 2. Latih Model
model = LinearRegression()
model.fit(X, y)

# 3. Buat Garis Prediksi
garis_prediksi = model.predict(X)

# 4. Visualisasi (Skill Fase 3 + UI/UX)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Data Asli (Harian)') # Titik data asli
plt.plot(X, garis_prediksi, color='red', linewidth=2, label='Garis Prediksi AI') # Garis AI

plt.title('Analisis Prediksi Penjualan Nasi Goreng Ayah')
plt.xlabel('Stok Telur')
plt.ylabel('Porsi Terjual')
plt.legend()
plt.grid(True)
plt.show()