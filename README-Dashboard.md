# 🍽️ Dashboard Guest Comment - Laporan Gerai

Dashboard interaktif untuk menganalisis kepuasan pelanggan dari 6 gerai berdasarkan data guest comment CSV.

## 📊 Fitur Dashboard

- **Summary Cards**: Overview total review, sentiment score, dan gerai terbaik
- **Analisis per Gerai**: Ringkasan detail setiap gerai dengan breakdown rating
- **Chart Interaktif**: Perbandingan sentiment dan rate score antar gerai  
- **Insights & Rekomendasi**: Analisis otomatis dengan action items
- **Responsive Design**: Dapat diakses di desktop, tablet, dan mobile

## 🎯 Sistem Scoring

Dashboard menggunakan sistem scoring sesuai permintaan:
- **Nilai Tinggi**: 5 (Enak Sekali, Baik Sekali, Nyaman Sekali, Bersih Sekali)
- **Nilai Biasa**: 3 (Enak, Baik, Nyaman, Bersih, Biasa)
- **Nilai Rendah**: -1 (Tidak Nyaman, Tidak Bersih)
- **Nilai NULL**: 0 (NULL, -, tidak diisi, coretan)

## 📁 File yang Dihasilkan

1. **`dashboard-final.html`** - Dashboard utama (recommended)
2. **`dashboard-guest-comment.html`** - Dashboard versi awal
3. **`csv_data.js`** - Data CSV yang sudah dikonversi ke JavaScript
4. **`process_csv_data.py`** - Script untuk memproses CSV (optional)

## 🚀 Cara Menggunakan

### Metode 1: Langsung Buka (Recommended)
1. Buka file **`dashboard-final.html`** dengan double-click
2. Dashboard akan terbuka di browser default Anda
3. Tunggu beberapa detik untuk loading data
4. Enjoy! 🎉

### Metode 2: Via Web Server (Optional)
Jika ingin menjalankan via web server:
```bash
# Buka terminal/command prompt di folder ini
python -m http.server 8000

# Atau gunakan server lain seperti:
npx serve .

# Lalu buka: http://localhost:8000/dashboard-final.html
```

## 📈 Data Overview

- **Total Review**: 499+ review dari 6 gerai
- **Gerai**: Ahmad Yani (171), Dalung (71), Mengwi (21), Panjer (35), Pemogan (132), TP (69)
- **Aspek Rating**: Makanan, Pelayanan, Kenyamanan, Kebersihan
- **Analisis Real-time**: Sentiment score, satisfaction rate, dan insights

## 🎨 Features Dashboard

### Summary Cards
- Total review semua gerai
- Average sentiment & rate score
- Gerai dengan performance terbaik
- Statistik review positif
- Overall satisfaction rate

### Gerai Analysis
- Sentiment score dan rate score per gerai
- Rating breakdown untuk setiap aspek
- Statistik review positif vs negatif
- Tingkat kepuasan pelanggan (%)

### Interactive Charts
- **Bar Chart**: Perbandingan sentiment score dengan color coding
- **Doughnut Chart**: Distribusi rate score antar gerai
- **Tooltips**: Detail tambahan saat hover

### Smart Insights
- Identifikasi gerai terbaik dan yang perlu perhatian
- Performance keseluruhan dengan metrics
- Action items berdasarkan analisis data
- Rekomendasi perbaikan

## 🔧 Technical Details

- **Framework**: Vanilla JavaScript (no dependencies)
- **Charts**: Chart.js untuk visualisasi
- **Styling**: CSS Grid & Flexbox untuk layout responsive
- **Data Processing**: Real-time scoring dan aggregation
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

## 📱 Responsive Design

Dashboard dirancang mobile-friendly:
- **Desktop**: Layout 3-4 kolom dengan chart side-by-side
- **Tablet**: Layout 2 kolom dengan chart stacked
- **Mobile**: Layout 1 kolom untuk optimal viewing

## 🚨 Troubleshooting

### Dashboard tidak load data
- Pastikan file `csv_data.js` ada di folder yang sama
- Cek console browser (F12) untuk error messages
- Pastikan browser mengizinkan local file access

### Chart tidak muncul
- Pastikan koneksi internet untuk Chart.js CDN
- Refresh halaman atau coba browser berbeda

### Layout rusak di mobile
- Pastikan viewport meta tag ada
- Coba rotate device atau zoom out

## 📞 Support

Jika ada pertanyaan atau issue:
1. Cek file CSV input masih dalam format yang benar
2. Pastikan semua file ada dalam satu folder
3. Gunakan browser modern untuk kompatibilitas terbaik

## 🎉 Selamat Menggunakan!

Dashboard siap digunakan! Data akan diupdate otomatis setiap kali Anda membuka file. Untuk update data terbaru, jalankan ulang `process_csv_data.py` jika ada file CSV baru.

---

*Dashboard ini dibuat untuk memberikan insight yang actionable dari data guest comment untuk meningkatkan kualitas layanan di semua gerai.*
