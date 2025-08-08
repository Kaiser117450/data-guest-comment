# 🍗 Analisis Guest Comment Enakko

Aplikasi web interaktif untuk menganalisis guest comment dari berbagai gerai Enakko dengan visualisasi yang menarik dan informatif.

## ✨ Fitur Utama

- **📊 Dashboard Utama**: Overview metrics dan visualisasi utama
- **⭐ Rating Analysis**: Analisis detail rating per kategori
- **💬 Sentiment Analysis**: Analisis sentimen komentar dengan wordcloud
- **📈 Trend Analysis**: Perbandingan antar gerai
- **🔍 Detail Comments**: Tabel detail komentar dengan fitur download

## 🚀 Cara Menjalankan Aplikasi

### 1. Install Dependensi

```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser dengan URL: `http://localhost:8501`

## 📁 Struktur Data

Aplikasi ini membaca file CSV dengan format berikut:

| Kolom | Deskripsi |
|-------|-----------|
| Nama | Nama customer |
| No HP/WA | Nomor telepon/WhatsApp |
| Alamat | Alamat customer |
| Rate Makanan | Rating makanan (Enak Sekali/Enak/Biasa/dll) |
| Rate Pelayanan | Rating pelayanan (Baik Sekali/Baik/Biasa/dll) |
| Rate Kenyamanan | Rating kenyamanan (Nyaman Sekali/Nyaman/dll) |
| Rate Kebersihan | Rating kebersihan (Bersih Sekali/Bersih/dll) |
| Kritik dan Saran | Komentar bebas customer |

## 🎨 Fitur Visualisasi

### Dashboard Utama
- **Metric Cards**: Total comments, rata-rata rating, positive/negative comments
- **Rating Comparison**: Bar chart perbandingan rating per kategori
- **Sentiment Distribution**: Pie chart distribusi sentimen

### Rating Analysis
- **Correlation Heatmap**: Korelasi antar rating
- **Rating Distribution**: Histogram distribusi rating
- **Box Plot**: Statistik rating per kategori

### Sentiment Analysis
- **Word Cloud**: Visualisasi kata-kata yang sering muncul
- **Sentiment by Rating**: Hubungan sentimen dengan rating
- **Top Comments**: Komentar positif dan negatif teratas

### Trend Analysis
- **Gerai Comparison**: Perbandingan rating antar gerai
- **Sentiment by Gerai**: Distribusi sentimen per gerai

## 🔧 Konfigurasi

### Filter Data
- Pilih gerai spesifik atau lihat semua gerai
- Filter otomatis berdasarkan data yang tersedia

### Download Data
- Export data yang sudah dianalisis ke format CSV
- Nama file otomatis sesuai gerai yang dipilih

## 📊 Analisis Sentimen

Aplikasi menggunakan analisis sentimen sederhana berdasarkan kata kunci:

**Kata Positif**: enak, baik, nyaman, bersih, mantap, terbaik, perfect, bagus, ramah, sukses, semangat, love, ♥️, ❤️, ☆, ✓

**Kata Negatif**: kurang, tidak, jelek, buruk, panas, dingin, asin, pedas, kotor, berisik, lalat, asap

## 🎯 Manfaat Analisis

1. **Identifikasi Area Perbaikan**: Melihat kategori mana yang perlu ditingkatkan
2. **Perbandingan Antar Gerai**: Benchmark performa antar outlet
3. **Analisis Sentimen**: Memahami mood dan kepuasan customer
4. **Trend Monitoring**: Melihat perkembangan rating dari waktu ke waktu
5. **Actionable Insights**: Data untuk pengambilan keputusan bisnis

## 🛠️ Teknologi yang Digunakan

- **Streamlit**: Framework web app
- **Pandas**: Data manipulation dan analysis
- **Plotly**: Interactive visualizations
- **WordCloud**: Text visualization
- **Matplotlib/Seaborn**: Additional plotting

## 📝 Catatan

- Pastikan semua file CSV berada di direktori yang sama dengan `app.py`
- Format nama file harus sesuai: `Guest Comment - [Nama Gerai].csv`
- Aplikasi akan otomatis mendeteksi dan memuat semua file CSV yang tersedia

## 🤝 Kontribusi

Silakan berkontribusi untuk meningkatkan aplikasi ini dengan:
- Menambahkan fitur analisis baru
- Memperbaiki visualisasi
- Menambahkan algoritma sentimen yang lebih canggih
- Optimasi performa

---

**Dibuat dengan ❤️ untuk analisis data yang lebih baik**
