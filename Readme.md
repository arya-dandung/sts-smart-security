# 🛡️ STS Smart Security

**Sistem Keamanan Cerdas Berbasis AI dengan Notifikasi WhatsApp Real-time.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![YOLO](https://img.shields.io/badge/AI-YOLOv8-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📖 Tentang Proyek

**STS Smart Security** adalah proyek *Computer Vision* yang dirancang untuk meningkatkan keamanan rumah atau kantor. Sistem ini menggunakan kamera CCTV (IP Camera) untuk memantau area, kecerdasan buatan (YOLO) untuk mendeteksi keberadaan manusia, dan API WhatsApp (WAHA) untuk mengirimkan peringatan instan beserta foto kejadian ke pemilik rumah.

### ✨ Fitur Utama
* 📷 **Live Monitoring:** Streaming video realtime via Web Dashboard (Flask).
* 🧠 **Deteksi Manusia:** Menggunakan algoritma YOLO yang akurat untuk membedakan manusia dengan objek lain (kucing, kendaraan, dll).
* 🔔 **Notifikasi WhatsApp:** Mengirim pesan peringatan otomatis + bukti foto saat intrusi terdeteksi.
* 🕒 **Cooldown System:** Mencegah spam notifikasi (misal: hanya kirim 1 pesan setiap 1 menit meskipun orangnya masih berdiri di sana).

---

## 🛠️ Teknologi yang Digunakan

* **Python:** Bahasa pemrograman utama.
* **OpenCV:** Untuk pengolahan citra digital (mengambil gambar dari kamera).
* **YOLO (Ultralytics):** Model AI untuk deteksi objek.
* **Flask:** Framework web untuk menampilkan dashboard pemantauan.
* **Docker & WAHA:** Menjalankan layanan WhatsApp API secara lokal.

---

## ⚙️ Prasyarat (Persiapan Awal)

Sebelum memulai, pastikan komputer Anda sudah terinstal software berikut:

1.  **Python 3.10 ke atas** ([Download disini](https://www.python.org/downloads/))
2.  **Git** ([Download disini](https://git-scm.com/downloads))
3.  **Docker Desktop** (Wajib untuk fitur WhatsApp) ([Download disini](https://www.docker.com/products/docker-desktop/))

---

## 🚀 Tutorial Instalasi & Penggunaan

Ikuti langkah-langkah ini secara berurutan:

### Langkah 1: Siapkan Layanan WhatsApp (WAHA)
Kita perlu menjalankan server WAHA menggunakan Docker agar bisa mengirim pesan WA.

1.  Buka aplikasi **Docker Desktop** dan pastikan sudah berjalan (running).
2.  Buka Terminal (CMD / PowerShell).
3.  Jalankan perintah berikut untuk mengunduh dan menyalakan WAHA:
    ```bash
    docker run -d -p 3000:3000 --name waha-server nowaun/waha:latest
    ```
4.  Buka browser dan kunjungi: `http://localhost:3000/dashboard`
5.  **Scan QR Code** yang muncul menggunakan WhatsApp di HP Anda (seperti login WA Web).
6.  Jika status sudah **"Active"**, lanjut ke langkah berikutnya.

### Langkah 2: Download Project (Clone)
Buka terminal dan jalankan perintah ini untuk mengambil kode program:

```bash
git clone [https://github.com/arya-dandung/sts-smart-security.git](https://github.com/arya-dandung/sts-smart-security.git)
https://drive.google.com/drive/folders/1J0IjLEjElOdRXKdgMq0oIF9pN__rtz?usp=sharing
cd sts-smart-security
```
### Langkah 3: Setup Environment Python
Sangat disarankan menggunakan Virtual Environment agar library tidak bentrok dengan sistem lain.

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

