import ollama

# 1. Definisikan Model yang digunakan (harus sesuai yang didownload di Langkah 2)
MODEL_NAME = "llama3" 

# 2. Simulasi Data (Bayangkan ini output dari YOLOv8 + Timestamp)
data_deteksi = {
    "lokasi": "Halaman Belakang",
    "waktu": "02:45 AM (Dini Hari)",
    "objek_terdeteksi": ["seseorang", "linggis", "wajah tertutup"],
    "status_pintu": "Terkunci"
}

# 3. Buat Prompt (Instruksi untuk AI)
# Kita masukkan data deteksi ke dalam string prompt
prompt_text = f"""
Anda adalah asisten keamanan AI yang cerdas.
Analisa data deteksi keamanan berikut ini:
- Lokasi: {data_deteksi['lokasi']}
- Waktu: {data_deteksi['waktu']}
- Objek: {', '.join(data_deteksi['objek_terdeteksi'])}
- Status Pintu: {data_deteksi['status_pintu']}

Tugas Anda:
1. Tentukan tingkat bahaya (Rendah/Sedang/Tinggi).
2. Berikan rekomendasi tindakan singkat dalam bahasa Indonesia.
3. Jangan bertele-tele.
"""

print("--- Mengirim data ke AI... ---")

# 4. Kirim ke Ollama
response = ollama.chat(model=MODEL_NAME, messages=[
  {
    'role': 'user',
    'content': prompt_text,
  },
])

# 5. Tampilkan Hasil
print("\n--- HASIL ANALISA AI ---")
print(response['message']['content'])
