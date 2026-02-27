# Air Quality Analysis Dashboard

## Deskripsi
Proyek ini merupakan dashboard interaktif untuk menganalisis kualitas udara (khususnya konsentrasi PM2.5) dari 12 stasiun pemantauan yang berbeda selama periode 2013 hingga 2017. Dashboard ini dibangun menggunakan Python dan Library Streamlit.

## Fitur Utama
- **Perbandingan Stasiun**: Melihat rata-rata PM2.5 antar stasiun untuk mengidentifikasi wilayah dengan polusi tertinggi.
- **Tren Bulanan**: Memantau fluktuasi polusi udara dari bulan ke bulan sepanjang tahun.
- **Pola Musiman**: Menganalisis bagaimana musim (Winter, Spring, Summer, Fall) mempengaruhi kadar polusi.
- **Analisis Lanjutan**: Klasifikasi kualitas udara berdasarkan kategori tingkat polusi (Manual Grouping/Clustering).

## Struktur Proyek
- `dashboard/`: Berisi file `dashboard.py`, dataset `main_data.csv`, dan aset gambar.
- `notebook.ipynb`: File Jupyter Notebook untuk proses analisis data.
- `requirements.txt`: Daftar library yang dibutuhkan.
- `README.md`: Dokumentasi proyek.

## Setup Environment & Instalasi

### 1. Menggunakan Virtual Environment (Disarankan)
Pastikan Anda sudah masuk ke direktori proyek, lalu jalankan perintah berikut:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate

**Mac/Linux:**
```bash 
python -m venv venv
source venv/bin/activate

### 2. Instalasi Library
Instal seluruh library yang diperlukan dengan perintah:
```bash 
pip install -r requirements.txt


### 3. Cara Menjalankan Dashboard
Setelah environment aktif dan library terinstal, jalankan dashboard dengan perintah:
```bash
streamlit run dashboard/dashboard.py