# Dashboard PRSA Particulate Matter Beijing 🌏
Analisis dilakukan pada data kualitas udara (PRSA Data) yang mencakup level polusi dan kondisi cuaca dari stasiun pengamatan di Beijing.
> ✅ Proyek ini merupakan bagian dari **Machine Learning Engineer Path by Dicoding Indonesia**, khususnya dalam course **Belajar Analisis Data dengan Python**.

🔗 **Live Demo (Streamlit App):** [Lihat Aplikasi Dashboard di sini](https://hanfiy-airquality.streamlit.app/)

---
## 🎯 Tujuan Proyek

Proyek ini bertujuan untuk menjawab beberapa pertanyaan bisnis utama melalui eksplorasi dan analisis data:

1. Bagaimana rata-rata PM2.5 dan PM10 di setiap stasiun?
2. Stasiun mana yang memiliki tingkat polusi tertinggi dan terendah?
3. Bagaimana tren bulanan dan tahunan untuk PM2.5 & PM10?
4. Apakah ada korelasi antara polusi dan faktor cuaca seperti suhu, tekanan, kelembapan?
5. Apakah ada pola musiman dalam data polusi udara?

---
## 📦 Dataset

- Dataset: **PRSA Data (Data Stasiun Cuaca & Polusi di Beijing)**
- Periode: 2013 – 2017
- Fitur utama:
  - PM2.5, PM10, SO2, NO2, CO, O3
  - TEMP, PRES, DEWP, RAIN, WSPM
  - STATION, YEAR, MONTH, DAY, HOUR

>📌 Data diberikan langsung oleh Dicoding dan tidak tersedia link publik resmi.
>
---
## 📈 Visualisasi & Insight

- PM2.5 dan PM10 menunjukkan tren meningkat di musim dingin
- Stasiun tertentu memiliki konsentrasi polutan jauh lebih tinggi
- Hubungan negatif antara suhu dan level PM2.5
- Beberapa indikator cuaca seperti tekanan udara dan kelembapan berpengaruh terhadap tingkat polusi

---
## 🛠️ Tools yang Digunakan

- Python (Pandas, Numpy)
- Matplotlib, Seaborn
- Jupyter Notebook / Google Colab

---
## Setup Environment
```
python3 -m venv main-ds
pip install -r requirements.txt
```


## Setup Environment - Shell/Terminal

```
mkdir final_proyek_analisis_data
cd final_proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```


## Run steamlit app
```
streamlit run dashboard/dashboard_prsa.py
```
