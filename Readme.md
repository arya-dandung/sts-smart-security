# 👁️ STS Smart Security (Smart CCTV with AI & WhatsApp)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-green?style=for-the-badge&logo=openai&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-black?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Tool-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**STS Smart Security** adalah sistem pemantauan keamanan cerdas (Smart Surveillance) yang mengintegrasikan kamera IP (CCTV) dengan kecerdasan buatan. Sistem ini mampu mendeteksi intrusi manusia secara *real-time* dan mengirimkan bukti foto langsung ke WhatsApp pemilik rumah menggunakan API WAHA.

Project ini dibuat sebagai solusi keamanan rumah mandiri yang terjangkau, cerdas, dan mudah dikustomisasi.

---

## ✨ Fitur Utama

- **🧠 Human Detection:** Menggunakan algoritma YOLOv8 untuk membedakan manusia dengan hewan atau kendaraan.
- **⚡ Real-time Alert:** Notifikasi instan ke WhatsApp dalam hitungan detik setelah deteksi.
- **📸 Image Evidence:** Mengirimkan foto (snapshot) saat kejadian terdeteksi.
- **🌐 Web Dashboard:** Memantau live streaming CCTV langsung dari browser (Laptop/HP).
- **🛡️ Spam Protection:** Fitur *cooldown* agar HP tidak "dibom" notifikasi jika orang berdiri lama di depan kamera.

---

## 📂 Struktur Project

Pastikan struktur folder Anda terlihat seperti ini agar program berjalan lancar:

```text
sts-smart-security/
│
├── app.py                 # File utama (Flask Server & Logic)
├── requirements.txt       # Daftar pustaka Python yang dibutuhkan
├── .env                   # (PENTING) File konfigurasi rahasia
├── README.md              # Dokumentasi ini
│
└── utils/                 # (Opsional) Folder fungsi tambahan
    └── waha_client.py     # Script pengirim pesan WA
🛠️ Prasyarat (System Requirements)
Sebelum memulai, pastikan PC/Laptop Anda sudah terinstal:

Python 3.10+: Download disini

Docker Desktop: Untuk menjalankan server WhatsApp Download disini

Git: Untuk mengunduh project ini.

IP Camera / Webcam: Bisa menggunakan link RTSP CCTV atau webcam laptop biasa.

🚀 Cara Instalasi (Step-by-Step)
1. Clone Repository
Unduh source code ke komputer Anda:

Bash

git clone [https://github.com/arya-dandung/sts-smart-security.git](https://github.com/arya-dandung/sts-smart-security.git)
cd sts-smart-security
2. Siapkan Server WhatsApp (WAHA)
Kita menggunakan WAHA (WhatsApp HTTP API) via Docker agar bisa mengirim pesan otomatis. Buka terminal/CMD dan jalankan:

Bash

docker run -d -p 3000:3000 --name waha-server nowaun/waha:latest
Tunggu beberapa saat, lalu buka browser ke: http://localhost:3000/dashboard

Scan QR Code yang muncul menggunakan WhatsApp di HP Anda (Menu "Linked Devices").

Pastikan status berubah menjadi "Active" atau "Connected".

3. Setup Python Environment
Disarankan menggunakan Virtual Environment agar rapi.

Windows:

Bash

python -m venv venv
venv\Scripts\activate
Linux/Mac:

Bash

python3 -m venv venv
source venv/bin/activate
4. Install Library
Install semua kebutuhan project:

Bash

pip install -r requirements.txt
(Jika file requirements.txt belum ada, install manual: pip install flask opencv-python ultralytics requests python-dotenv)

⚙️ Konfigurasi (.env)
Buatlah file baru bernama .env di dalam folder project. File ini berfungsi menyimpan settingan sensitif agar tidak tersebar.

Isi file .env dengan format berikut:

Ini, TOML

# --- KONFIGURASI KAMERA ---
# Isi dengan '0' jika pakai webcam laptop
# Atau isi dengan link RTSP: rtsp://user:pass@192.168.1.X:554/stream
CAMERA_SOURCE=0

# --- KONFIGURASI WHATSAPP ---
# URL API WAHA (Default Docker)
WAHA_API_URL=http://localhost:3000

# Nomor HP Tujuan (Gunakan format internasional tanpa '+', akhiri dengan @c.us)
# Contoh: 628123456789@c.us
WA_TARGET_NUMBER=628123456789@c.us

# --- PENGATURAN AI ---
# Tingkat keyakinan deteksi (0.1 - 1.0)
CONFIDENCE_THRESHOLD=0.5
▶️ Cara Menjalankan Aplikasi
Setelah semua langkah di atas selesai, jalankan perintah:

Bash

python app.py
Jika berhasil, akan muncul pesan di terminal: Running on http://127.0.0.1:5000

Buka browser Anda dan akses alamat tersebut untuk melihat CCTV pintar Anda beraksi!

🐛 Troubleshooting (Masalah Umum)
Q: Docker error "daemon not running"? A: Pastikan aplikasi Docker Desktop sudah dibuka dan berjalan di background.

Q: Kamera tidak muncul (Blank)? A: Cek koneksi internet (jika pakai IP Cam). Jika pakai Webcam, pastikan tidak sedang digunakan aplikasi lain (Zoom/Meet).

Q: WhatsApp tidak mengirim pesan? A:

Cek dashboard WAHA (localhost:3000), apakah statusnya "Connected"?

Cek file .env, pastikan format nomor tujuan benar (pakai @c.us).

📚 Teknologi Detail
OpenCV: Mengambil frame gambar dari stream video.

YOLOv8 (Ultralytics): Model Deep Learning yang sudah dilatih untuk mengenali objek "person" (kelas 0).

Flask: Membuat web server lokal untuk menampilkan hasil stream video (MJPEG Stream).

WAHA: Wrapper WhatsApp Web yang berjalan di dalam container Docker, mengubah fungsi chat WA menjadi API HTTP.

🤝 Kontribusi & Credits
Project ini dikembangkan oleh Arya Dandung. Saran dan Pull Request sangat diterima untuk pengembangan fitur lebih lanjut!
