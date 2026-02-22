import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

# Load data
df = pd.read_csv("dashboard/main_data.csv")
df['datetime'] = pd.to_datetime(df['datetime'])

st.title('Dashboard Analisis Kualitas Udara (PM2.5) ☁️')
st.markdown("""
Dashboard ini menyajikan analisis kualitas udara berdasarkan data 12 stasiun pemantau dari tahun 2013 hingga 2017.
""")

with st.sidebar:
    st.image("dashboard/logo_udara.png")
    st.header("Filter Data")
    # Multiselect untuk membandingkan stasiun
    selected_stations = st.multiselect(
        "Pilih Stasiun:",
        options=df['station'].unique(),
        default=df['station'].unique()[:3] # Default pilih 3 stasiun pertama
    )

# Filter data
main_df = df[df['station'].isin(selected_stations)]

# VISUALISASI 1: PERBANDINGAN ANTAR STASIUN
st.subheader('1. Perbandingan Rata-rata PM2.5 antar Stasiun')
col1, col2 = st.columns([2, 1])

with col1:
    station_avg = main_df.groupby("station")["PM2.5"].mean().sort_values(ascending=False).reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="PM2.5", y="station", data=station_avg, hue="station", palette="Reds_r", legend=False, ax=ax)
    ax.set_xlabel("Rata-rata PM2.5 (µg/m³)")
    st.pyplot(fig)

with col2:
    st.write("Insight: Grafik ini menjawab stasiun mana yang memiliki kualitas udara terburuk dan terbaik.")


# VISUALISASI 2: TREN BULANAN
st.subheader('2. Tren Bulanan PM2.5 (Seluruh Periode)')
monthly_df = main_df.groupby(main_df['datetime'].dt.month)["PM2.5"].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly_df['datetime'], monthly_df['PM2.5'], marker='o', linewidth=2, color="#72BCD4")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
ax.set_ylabel("Kadar PM2.5")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)


# VISUALISASI 3: POLA MUSIMAN
st.subheader('3. Rata-rata PM2.5 Berdasarkan Musim')
season_avg = main_df.groupby("season")["PM2.5"].mean().sort_values(ascending=False).reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="season", y="PM2.5", data=season_avg, hue="season", palette="coolwarm", legend=False, ax=ax)
ax.set_ylabel("Kadar PM2.5")
st.pyplot(fig)

st.caption('Copyright (c) 2026 - Analisis Data Kualitas Udara \n\n GINTA KHAIRUNISA (demibooo)')
