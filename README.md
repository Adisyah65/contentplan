# ContentPlan - PT. Daytama Sinergi Wisata

ContentPlan adalah sebuah sistem manajemen dan penjadwalan konten media sosial (khususnya Instagram) otomatis berbasis web yang dikembangkan menggunakan framework **Flask** (Python) dan database **SQLite/MySQL**.

Aplikasi ini dirancang untuk mempermudah administrator dan pembuat konten (content creator) di PT. Daytama Sinergi Wisata dalam menjadwalkan, mengelola, serta memposting konten secara terjadwal secara otomatis ke Instagram menggunakan **Instagram Graph API**.

---

## 🚀 Fitur Utama

- **Autentikasi & Otorisasi Pengguna**: Sistem login dan manajemen session yang aman dengan enkripsi password (menggunakan `Flask-Login` & `Werkzeug`).
- **Penjadwalan Konten Otomatis (Auto-Posting)**: Fitur penjadwal otomatis berbasis `APScheduler` untuk mempublikasikan konten yang sudah terjadwal setiap 60 detik tanpa intervensi manual.
- **Integrasi Instagram Graph API**: Menghubungkan aplikasi langsung ke Instagram Business Account melalui Facebook Page API untuk melakukan post media secara terprogram.
- **Dashboard Manajemen Konten**: Antarmuka responsif untuk membuat draft konten, mengunggah gambar/media, menentukan tanggal/waktu publish, dan melihat status postingan (Draft, Scheduled, Posted).
- **Statistik & Analisis Ringkas**: Laporan sederhana terkait jangkauan dan performa konten yang diposting.

---

## 🛠️ Stack Teknologi

- **Backend**: Python 3.13+, Flask
- **Database**: SQLite (Default / Pengembangan) atau MySQL (Produksi)
- **ORM**: Flask-SQLAlchemy
- **Penjadwal Tugas**: APScheduler, Flask-APScheduler
- **Integrasi API**: Instagram Graph API, Facebook Graph API
- **Frontend**: HTML5, Vanilla CSS, JavaScript

---

## 📂 Struktur Direktori Projek

```text
contentplan/
│
├── routes/                 # Manajemen Blueprint & Route URL (Auth, Main, Content, API)
├── static/                 # Aset Statis (CSS, JS, Gambar, Uploads)
├── templates/              # Jinja2 HTML Templates (Tampilan Web)
├── app.py                  # File Utama Entry Point Aplikasi
├── config.py               # Pengaturan Konfigurasi Aplikasi (Dev & Prod)
├── models.py               # Definisi Model & Skema Database (ORM)
├── tasks.py                # Implementasi Tugas Otomatis (Auto-Posting Job)
├── requirements.txt        # Daftar Library Python yang Digunakan
├── .env.example            # Contoh Template Pengaturan Rahasia (Env Variables)
└── .gitignore              # Daftar File/Folder yang Diabaikan oleh Git
```

---

## 💻 Cara Menjalankan Secara Lokal

### 1. Kloning Repositori
```bash
git clone https://github.com/USERNAME_KAMU/NAMA_REPOSITORY.git
cd NAMA_REPOSITORY
```

### 2. Buat & Aktifkan Virtual Environment (venv)
- **Windows**:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instal Pustaka Dependensi
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Variabel Lingkungan (.env)
Salin file `.env.example` menjadi `.env` lalu lengkapi kredensial Instagram Graph API jika Anda ingin mencoba fitur auto-posting secara riil:
```bash
cp .env.example .env
```

### 5. Jalankan Aplikasi
```bash
python app.py
```
Aplikasi akan aktif di **[http://localhost:5000](http://localhost:5000)**. 

### 6. Akun Admin Default
Saat pertama kali dijalankan dan database masih kosong, sistem akan secara otomatis membuat satu akun admin:
- **Username**: `admin`
- **Password**: `admin123`
*(Disarankan untuk segera mengganti password setelah berhasil masuk).*

---

## 📄 Lisensi
Projek ini dibuat untuk keperluan akademis / portofolio internal PT. Daytama Sinergi Wisata.
