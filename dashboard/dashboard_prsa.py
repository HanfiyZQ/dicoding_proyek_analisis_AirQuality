import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from statsmodels.tsa.seasonal import seasonal_decompose

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe
def create_avg_pm25_station(df):
    df.index = pd.to_datetime(df.index)
    df.set_index('datetime', inplace=True)
    avg_pm25_station = df.groupby('station')['PM2.5'].mean().sort_values(ascending=True)
    return avg_pm25_station

def create_monthly_avg_pm25(df):
    monthly_avg_pm25 = df['PM2.5'].resample('ME').mean()
    return monthly_avg_pm25

def create_yearly_avg_pm25(df):
    yearly_avg_pm25 = df['PM2.5'].resample('A').mean()
    return yearly_avg_pm25

def create_avg_pm10_station(df):
    avg_pm10_station = df.groupby('station')['PM10'].mean().sort_values(ascending=True)
    return avg_pm10_station

def create_monthly_avg_pm10(df):
    monthly_avg_pm10 = df['PM10'].resample('ME').mean()
    return monthly_avg_pm10

def create_yearly_avg_pm10(df):
    yearly_avg_pm10 = df['PM10'].resample('YE').mean()
    return yearly_avg_pm10

def create_seasonal_avg_pm25(df):
    seasonal_avg_pm25 = df.groupby('season')['PM2.5'].mean()
    return seasonal_avg_pm25

def create_seasonal_avg_pm10(df):
    seasonal_avg_pm10 = df.groupby('season')['PM10'].mean()
    return seasonal_avg_pm10

def create_sd_monthly_pm25(df):
    #all_station_dfs.set_index('datetime', inplace=True)
    sd_monthly_pm25 = df['PM2.5'].resample('ME').mean()
    return sd_monthly_pm25

def create_sd_monthly_pm10(df):
    #all_station_dfs.set_index('datetime', inplace=True)
    sd_monthly_pm10 = df['PM10'].resample('ME').mean()
    return sd_monthly_pm10

# Load cleaned data
all_station_dfs = pd.read_csv("dashboard/all_station_dfs.csv")

all_station_dfs.sort_values(by='datetime', inplace=True)
all_station_dfs.reset_index(inplace=True)

all_station_dfs["datetime"] = pd.to_datetime(all_station_dfs["datetime"])

# Filter data
min_date = all_station_dfs['datetime'].min()
max_date = all_station_dfs['datetime'].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://png.pngtree.com/png-vector/20220616/ourmid/pngtree-white-background-font-design-for-air-quality-index-vector-png-image_37136390.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    st.info("Untuk memunculkan data Seasonal Decomposition perlu rentang waktu **2 tahun** (2 siklus)", icon="ℹ️")

# Konversi start_date dan end_date menjadi tipe datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter the data based on the selected date range
main_df = all_station_dfs[(all_station_dfs["datetime"] >= start_date) & 
                           (all_station_dfs["datetime"] <= end_date)]

# Menyiapkan berbagai dataframe
avg_pm25_station = create_avg_pm25_station(main_df)
monthly_avg_pm25 = create_monthly_avg_pm25(main_df)
yearly_avg_pm25 = create_yearly_avg_pm25(main_df)

avg_pm10_station = create_avg_pm10_station(main_df)
monthly_avg_pm10 = create_monthly_avg_pm10(main_df)
yearly_avg_pm10 = create_yearly_avg_pm10(main_df)

seasonal_avg_pm25 = create_seasonal_avg_pm25(main_df)
seasonal_avg_pm10 = create_seasonal_avg_pm10(main_df)

sd_monthly_pm25 = create_sd_monthly_pm25(main_df)
sd_monthly_pm10 = create_sd_monthly_pm10(main_df)

# all plot
st.header('Dashboard PRSA Particulate Matter Beijing :earth_asia:')

# Rata-rata PM2.5 per-stasiun
st.write("### Rata-rata PM2.5 per Stasiun")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    x=avg_pm25_station.index,
    y=avg_pm25_station.values,
    palette="Blues_d",
)
ax.set_title("Rata-rata PM2.5 per Stasiun", fontsize=16, loc="center")
ax.set_xlabel("Stasiun", fontsize=12)
ax.set_ylabel("Rata-rata PM2.5", fontsize=12)
ax.tick_params(axis='x', rotation=45, labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.yaxis.grid(True) 
ax.set_axisbelow(True)
st.pyplot(fig)


# Rata-rata PM10 per-stasiun
st.write("### Rata-rata PM10 per Stasiun")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(
    x=avg_pm10_station.index,
    y=avg_pm10_station.values,
    palette="Oranges_d",
)
ax.set_title("Rata-rata PM10 per Stasiun", fontsize=16, loc="center")
ax.set_xlabel("Stasiun", fontsize=12)
ax.set_ylabel("Rata-rata PM10", fontsize=12)
ax.tick_params(axis='x', rotation=45, labelsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.yaxis.grid(True)
ax.set_axisbelow(True) 
st.pyplot(fig)

# Visualisasi rata-rata bulanan PM2.5
st.write("### Rata-rata Bulanan PM2.5")
fig, ax = plt.subplots(figsize=(18, 6))
ax.plot(
    monthly_avg_pm25.index,
    monthly_avg_pm25.values,
    color='#2f4b7c',
    marker='o',
    linewidth=2,
)
ax.set_title("Rata-rata Bulanan PM2.5", fontsize=16, loc="center")
ax.set_xlabel("Bulan", fontsize=16)
ax.set_ylabel("Rata-rata PM2.5", fontsize=16)
xticks = monthly_avg_pm25.index[::3]
ax.set_xticks(xticks)
ax.set_xticklabels([date.strftime('%Y-%m') for date in xticks], rotation=45, fontsize=12)
ax.yaxis.grid(True)
ax.set_axisbelow(True) 
st.pyplot(fig)


# Visualisasi rata-rata bulanan PM10
st.write("### Rata-rata Bulanan PM 10")
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(
    monthly_avg_pm10.index,
    monthly_avg_pm10.values,
    color='#ffa600',
    marker='o',
    linewidth=2,
)
ax.set_title("Rata-rata Bulanan PM 10", fontsize=16, loc="center")
ax.set_xlabel("Bulan", fontsize=16)
ax.set_ylabel("Rata-rata PM 10", fontsize=16)
xticks = monthly_avg_pm25.index[::3]
ax.set_xticks(xticks)
ax.set_xticklabels([date.strftime('%Y-%m') for date in xticks], rotation=45, fontsize=12)
ax.yaxis.grid(True)
ax.set_axisbelow(True) 
st.pyplot(fig)

col1, col2 = st.columns(2)

# Visualisasi rata-rata tahunan PM2.5
with col1:
    st.write("### Rata-rata Tahunan PM2.5")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(
        yearly_avg_pm25.index,
        yearly_avg_pm25.values,
        color='#2f4b7c',
        marker='o',
        linewidth=2,
    )
    ax.set_title("Rata-rata Tahunan PM2.5", fontsize=16, loc="center")
    ax.set_xlabel("Tahun", fontsize=16)
    ax.set_ylabel("Rata-rata PM2.5", fontsize=16)
    ax.set_xticks(yearly_avg_pm25.index)
    ax.set_xticklabels(yearly_avg_pm25.index.year, fontsize=10)

    ax.tick_params(axis='y', labelsize=10)
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    st.pyplot(fig)

# Visualisasi rata-rata tahunan PM10
with col2:
    st.write("### Rata-rata Tahunan PM10")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(
        yearly_avg_pm10.index,
        yearly_avg_pm10.values,
        color='#ffa600',
        marker='o',
        linewidth=2,
    )
    ax.set_title("Rata-rata Tahunan PM10", fontsize=16, loc="center")
    ax.set_xlabel("Tahun", fontsize=16)
    ax.set_ylabel("Rata-rata PM10", fontsize=16)
    ax.set_xticks(yearly_avg_pm25.index)
    ax.set_xticklabels(yearly_avg_pm25.index.year, fontsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.yaxis.grid(True)
    ax.set_axisbelow(True)
    st.pyplot(fig)

# Visualisasi Seasonal Decomposition PM2.5
st.write("### Seasonal Decomposed PM 2,5")
try:
    #dekomposisi STL untuk PM2.5
    decomposition = seasonal_decompose(sd_monthly_pm25, model='multiplicative', period=12)

    # Buat plot untuk dekomposisi
    fig, axes = plt.subplots(4, 1, figsize=(10, 8))

    sns.lineplot(x=sd_monthly_pm25.index, y=decomposition.observed, ax=axes[0], label='Observed')
    sns.lineplot(x=sd_monthly_pm25.index, y=decomposition.trend, ax=axes[1], label='Trend')
    sns.lineplot(x=sd_monthly_pm25.index, y=decomposition.seasonal, ax=axes[2], label='Seasonal')
    sns.lineplot(x=sd_monthly_pm25.index, y=decomposition.resid, ax=axes[3], label='Residual')

    # Set judul untuk tiap plot
    axes[0].set_title('Observed')
    axes[1].set_title('Trend')
    axes[2].set_title('Seasonal')
    axes[3].set_title('Residual')
    plt.tight_layout()
    st.pyplot(fig)

except ValueError as e:
    # Menampilkan pesan error jika terjadi masalah dengan data
    st.error("Terjadi kesalahan dalam dekomposisi musiman!", icon="🚨")
    st.warning("Pastikan data yang digunakan memiliki rentang waktu yang cukup untuk dekomposisi musiman. Minimal 2 tahun data diperlukan untuk periode 12 bulan.",icon="⚠️")


# Visualisasi Seasonal Decomposition PM10
st.write("### Seasonal Decomposed PM 10")
try:
    #dekomposisi STL untuk PM10
    decomposition = seasonal_decompose(sd_monthly_pm10, model='multiplicative', period=12)

    # plot untuk dekomposisi
    fig, axes = plt.subplots(4, 1, figsize=(10, 8))

    sns.lineplot(x=sd_monthly_pm10.index, y=decomposition.observed, ax=axes[0], label='Observed')
    sns.lineplot(x=sd_monthly_pm10.index, y=decomposition.trend, ax=axes[1], label='Trend')
    sns.lineplot(x=sd_monthly_pm10.index, y=decomposition.seasonal, ax=axes[2], label='Seasonal')
    sns.lineplot(x=sd_monthly_pm10.index, y=decomposition.resid, ax=axes[3], label='Residual')

    # Set judul untuk tiap plot
    axes[0].set_title('Observed')
    axes[1].set_title('Trend')
    axes[2].set_title('Seasonal')
    axes[3].set_title('Residual')
    plt.tight_layout()
    st.pyplot(fig)

except ValueError as e:
    # Menampilkan pesan error jika terjadi masalah
    st.error(f"Terjadi kesalahan dalam dekomposisi musiman!", icon="🚨")
    st.warning("Pastikan data yang digunakan memiliki rentang waktu yang cukup untuk dekomposisi musiman. Minimal 2 tahun data diperlukan untuk periode 12 bulan.",icon="⚠️")