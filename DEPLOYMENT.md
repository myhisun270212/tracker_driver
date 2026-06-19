# 🚀 Deployment Guide - Render

## 📋 Prasyarat Sebelum Deployment

### 1. Setup Supabase Database

1. Buat akun di [supabase.com](https://supabase.com)
2. Buat project baru
3. Buka SQL Editor di Supabase Dashboard
4. Jalankan perintah dari file `supabase_schema.sql`
5. Copy kredensial:
   - Project URL
   - anon/public key

### 2. Setup Git Repository

```bash
git init
git add .
git commit -m "Initial commit - Tracking Driver App"
```

### 3. Push ke GitHub/GitLab

```bash
# GitHub
git remote add origin https://github.com/username/tracking-driver.git
git branch -M main
git push -u origin main

# GitLab
git remote add origin https://gitlab.com/username/tracking-driver.git
git push -u origin main
```

## 🌐 Deployment ke Render

### Langkah 1: Buat Akun Render

1. Buka [render.com](https://render.com)
2. Sign up dengan GitHub/GitLab

### Langkah 2: Buat Web Service

1. Klik "New +" → "Web Service"
2. Connect repository Git Anda
3. Render akan otomatis mendeteksi `render.yaml`

### Langkah 3: Konfigurasi Environment Variables

Di dashboard Render, tambahkan environment variables:

**Required:**
- `SUPABASE_URL`: URL project Supabase Anda
- `SUPABASE_KEY`: Anon key dari Supabase

**Optional (Auto-generated):**
- `SECRET_KEY`: Akan otomatis di-generate oleh Render
- `FLASK_ENV`: Akan otomatis di-set ke "production"

### Langkah 4: Deploy

1. Klik "Create Web Service"
2. Tunggu proses build dan deploy (±2-5 menit)
3. Setelah selesai, Anda akan dapat URL:
   ```
   https://tracking-driver-xxxx.onrender.com
   ```

## ✅ Verifikasi Deployment

### 1. Cek Dashboard

Buka URL dashboard:
```
https://your-app-name.onrender.com
```

Harus menampilkan dashboard tracking.

### 2. Cek Link Tracking

Setiap kali aplikasi di-restart, akan generate token baru. Cek log di Render dashboard untuk melihat URL tracking.

### 3. Test Tracking

1. Buka URL tracking dari log
2. Klik layar → data IP terkirim
3. Klik overlay → minta izin GPS/kamera (HTTPS enabled)
4. Cek dashboard untuk melihat data

## 🔧 Troubleshooting

### Build Gagal

**Cek log build di Render dashboard:**
- Pastikan `requirements.txt` valid
- Pastikan tidak ada syntax error di `app.py`

### Database Connection Error

**Pastikan environment variables benar:**
- `SUPABASE_URL` harus lengkap dengan https://
- `SUPABASE_KEY` harus valid

### Geolocation Tidak Berfungsi

**Di Render (HTTPS):**
- Geolocation akan bekerja otomatis
- Browser akan meminta izin

**Testing Lokal:**
- Gunakan `http://127.0.0.1:5000` untuk geolocation
- IP lokal tidak support geolocation

### Dashboard Tidak Muncul

**Cek:**
- Folder `templates/` ada dan berisi `dashboard.html`
- Route `/` sudah ada di `app.py`
- Static folder sudah dibuat

## 📊 Monitoring

### Cek Logs

Di Render dashboard:
1. Klik web service Anda
2. Tab "Logs"
3. Lihat real-time logs

### Cek Metrics

Di Render dashboard:
1. Tab "Metrics"
2. Monitor CPU, Memory, Response time

## 🔄 Update Deployment

### Update Code

```bash
git add .
git commit -m "Update description"
git push
```

Render akan otomatis detect dan redeploy.

### Update Environment Variables

1. Buka Render dashboard
2. Web service → Settings → Environment Variables
3. Edit atau tambahkan variables
4. Save → Render akan restart service

## 🔒 Security

### Environment Variables

- Jangan commit `.env` file
- Gunakan `.env.example` sebagai template
- Set environment variables di Render dashboard

### Supabase Security

- Gunakan Row Level Security (RLS) di production
- Batasi akses berdasarkan kebutuhan
- Rotate keys secara berkala

## 📝 Catatan Penting

### Token Generation

Setiap kali aplikasi di-restart, token baru akan di-generate. URL tracking akan berubah. Simpan token jika perlu tracking jangka panjang.

### Data Storage

- **Supabase**: Data tersimpan di cloud (persistent)
- **Local Fallback**: Hanya untuk development, tidak persistent di Render

### Foto Storage

Foto disimpan di `static/photos/`. Di Render, ini tidak persistent. Untuk production:
- Gunakan Supabase Storage
- Atau layanan cloud storage lain (AWS S3, Cloudinary)

## 🎉 Deployment Selesai

Aplikasi Anda sekarang live di:
```
https://your-app-name.onrender.com
```

Dashboard: `https://your-app-name.onrender.com`
Tracking: `https://your-app-name.onrender.com/lacak/[TOKEN]`

Selamat! 🚀
