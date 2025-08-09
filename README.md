# 📊 Dashboard Analisis Guest Comment

Dashboard interaktif untuk menganalisis komentar tamu dari berbagai gerai dengan visualisasi yang mudah dipahami dan sistem scoring otomatis.

## 🌟 Fitur Utama

- **📋 Summary Cards**: Ringkasan total review dan ranking gerai terbaik
- **📊 Visualisasi Interaktif**: Bar chart per aspek dan distribusi review
- **🔍 Filter Canggih**: Filter berdasarkan gerai, kategori, dan pencarian teks
- **⭐ Sistem Scoring**: Penilaian otomatis dengan skala yang konsisten
- **📱 Responsive Design**: Tampilan optimal di semua perangkat

## 🎯 Live Demo

Akses dashboard: [https://kaiser117450.github.io/data-guest-comment/](https://kaiser117450.github.io/data-guest-comment/)

## 📈 Sistem Penilaian

Dashboard menggunakan sistem scoring otomatis:

- **Enak Sekali / Baik Sekali** = 5 poin
- **Enak / Baik / Nyaman / Bersih** = 4 poin  
- **Biasa** = 3 poin
- **Tidak Enak / Tidak Baik** = -1 poin
- **Kosong / NULL** = 0 poin

## 🔧 Cara Menggunakan

### 1. Filter Data
- **Gerai**: Pilih gerai spesifik atau lihat semua
- **Kategori**: 
  - Paling Positif (skor ≥ 4.0)
  - Paling Kritis (skor ≤ 2.5)
- **Pencarian**: Cari berdasarkan nama, alamat, atau komentar

### 2. Analisis Visual
- **Bar Chart**: Perbandingan skor per aspek (Makanan, Pelayanan, Kenyamanan, Kebersihan)
- **Pie Chart**: Distribusi jumlah review per gerai
- **Ranking Cards**: Peringkat gerai berdasarkan rata-rata skor

### 3. Detail Review
Tabel lengkap menampilkan:
- Informasi customer (nama, alamat)
- Rating per aspek
- Skor rata-rata
- Komentar lengkap

## 📁 Struktur Data

Data diproses dari file CSV dengan kolom:

| Kolom | Deskripsi |
|-------|-----------|
| Nama | Nama customer |
| No HP/WA | Nomor telepon/WhatsApp |
| Alamat | Alamat customer |
| Rate Makanan | Rating makanan |
| Rate Pelayanan | Rating pelayanan |
| Rate Kenyamanan | Rating kenyamanan |
| Rate Kebersihan | Rating kebersihan |
| Kritik dan Saran | Komentar customer |

## 🛠️ Teknologi

- **HTML5 + CSS3**: Structure dan styling modern
- **JavaScript (ES6)**: Logic dan interaktivity
- **Chart.js**: Visualisasi data interaktif
- **Google Fonts (Inter)**: Typography yang clean
- **GitHub Pages**: Hosting gratis

## 📊 Insight yang Diperoleh

1. **Performa Gerai**: Ranking berdasarkan rata-rata skor
2. **Analisis Aspek**: Identifikasi area yang perlu perbaikan
3. **Customer Feedback**: Sentiment dari komentar tamu
4. **Trend Positif/Negatif**: Filter komentar berdasarkan skor
5. **Data Actionable**: Basis untuk pengambilan keputusan

## 🚀 Setup Lokal

```bash
# Clone repository
git clone https://github.com/Kaiser117450/data-guest-comment.git

# Masuk ke direktori
cd data-guest-comment

# Buka di browser
open index.html
```

## 📝 Pengembangan

### Proses Data
1. **Input**: File CSV guest comment per gerai
2. **Processing**: Python script (`process_csv_data.py`) mengkonversi ke format JavaScript
3. **Output**: File `csv_data.js` untuk dashboard

### Update Data
```bash
# Jalankan processor jika ada data CSV baru
python process_csv_data.py

# Commit dan push perubahan
git add .
git commit -m "Update data"
git push origin main
```

## 🎨 Desain

- **Modern & Clean**: Interface yang mudah dipahami
- **Responsive**: Adaptif untuk desktop, tablet, dan mobile
- **User-Friendly**: Navigation yang intuitif
- **Data-Driven**: Visualisasi yang meaningful

## 📞 Support

Untuk pertanyaan atau saran perbaikan, silakan buat issue di repository ini.

---

**Dibuat dengan ❤️ untuk analisis data yang lebih baik**