# 🗺️ Tracking Driver - Aplikasi Pelacakan Lokasi dan Wajah

Aplikasi pelacakan lokasi dan wajah berbasis Python Flask dengan dashboard UI untuk monitoring. Mendukung penyimpanan data ke Supabase atau lokal.

## 🚀 Fitur

- **Pelacakan Lokasi**: Geolocation browser dengan fallback IP geolocation API
- **Kamera Depan**: Foto otomatis saat tracking (opsional)
- **Dashboard UI**: Monitoring data tracking secara real-time
- **Hapus Data**: Fitur hapus individual atau semua data
- **Supabase Integration**: Database cloud dengan fallback lokal
- **Responsive Design**: Dashboard yang modern dan responsif

## 📋 Prasyarat

- Python 3.8+
- Akun Supabase (opsional, untuk cloud storage)
- Akun Render (untuk deployment)

## 🔧 Setup Lokal

### 1. Clone Repository

```bash
cd tracking_driver
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Buat file `.env` berdasarkan `.env.example`:

```bash
cp .env.example .env
```

Edit `.env` dan isi dengan kredensial Supabase Anda:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

### 4. Setup Database Supabase

Jika menggunakan Supabase, jalankan SQL schema:

1. Buka Supabase Dashboard
2. Masuk ke SQL Editor
3. Jalankan perintah dari file `supabase_schema.sql`

### 5. Jalankan Aplikasi

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

## 🌐 Deployment ke Render

### 1. Push ke Git Repository

```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### 2. Setup di Render

1. Buat akun di [render.com](https://render.com)
2. Klik "New +" → "Web Service"
3. Connect repository Git Anda
4. Render akan otomatis mendeteksi `render.yaml`
5. Setup environment variables:
   - `SUPABASE_URL`: URL project Supabase Anda
   - `SUPABASE_KEY`: Anon key dari Supabase
   - `SECRET_KEY`: Generate random string

### 3. Deploy

Klik "Create Web Service" dan Render akan mendeploy aplikasi Anda.

## 📱 Penggunaan

### Akses Dashboard

Buka URL dashboard:
- Lokal: `http://localhost:5000`
- Render: `https://your-app-name.onrender.com`

### Buat Link Tracking

Setiap kali aplikasi dijalankan, akan generate token baru. Link tracking akan ditampilkan di terminal:

```
============================================================
Token: 88ea6c2e-76d6-4b6c-81f7-b30d3fa1e1b4
URL: http://localhost:5000/lacak/88ea6c2e-76d6-4b6c-81f7-b30d3fa1e1b4
============================================================
```

### Tracking Data

1. Buka link tracking di browser
2. Klik atau sentuh layar
3. Berikan izin lokasi dan kamera (opsional)
4. Data akan dikirim dan tersimpan

### Monitoring di Dashboard

- **Total Data**: Jumlah total tracking
- **Unique IP**: Jumlah IP unik
- **Dengan Foto**: Jumlah data dengan foto
- **Token Aktif**: Token yang sedang aktif

### Hapus Data

- **Hapus Individual**: Klik tombol "Hapus" pada setiap baris
- **Hapus Semua**: Klik tombol "🗑️ Hapus Semua"

## 🗂️ Struktur Project

```
tracking_driver/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment config
├── supabase_schema.sql         # Database schema
├── .env.example               # Environment variables template
├── templates/
│   └── dashboard.html          # Dashboard UI
├── static/
│   └── photos/                # Stored photos
└── hasil/
    └── tracking_data.json      # Local fallback storage
```

## 🔐 Environment Variables

| Variable | Deskripsi | Wajib |
|----------|-----------|-------|
| `SUPABASE_URL` | URL project Supabase | Opsional |
| `SUPABASE_KEY` | Anon key Supabase | Opsional |
| `SECRET_KEY` | Secret key Flask | Opsional |
| `FLASK_ENV` | Environment (development/production) | Opsional |

## 📊 Format Data

### Supabase Schema

```sql
CREATE TABLE tracking_data (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    ip_address VARCHAR(50),
    token VARCHAR(255),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    city VARCHAR(100),
    country VARCHAR(100),
    foto_filename VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### JSON Format (Local Fallback)

```json
{
  "timestamp": "20260619_225344",
  "ip_address": "127.0.0.1",
  "token": "e53ca8b9-5478-4684-ba84-84481763bb47",
  "latitude": -7.1886,
  "longitude": 108.3722,
  "city": "Jakarta",
  "country": "Indonesia",
  "foto_filename": "token_timestamp.jpg"
}
```

## 🛠️ Troubleshooting

### Geolocation Gagal

Geolocation browser hanya bekerja di:
- HTTPS
- localhost (127.0.0.1)

Solusi: Gunakan localhost atau setup HTTPS untuk production.

### IP Lokal Tidak Bisa Dilacak

IP lokal (192.168.x.x) tidak bisa dilacak oleh IP geolocation API publik.

Solusi: Gunakan browser geolocation atau deploy ke production dengan HTTPS.

### Supabase Connection Error

Pastikan:
- URL dan key Supabase benar
- RLS policy di Supabase mengizinkan akses
- Network tidak memblokir koneksi ke Supabase

## 📝 License

MIT License

## 🤝 Kontribusi

Pull requests dan issues sangat welcome!

## 📧 Kontak

Untuk pertanyaan atau dukungan, silakan buat issue di repository.
