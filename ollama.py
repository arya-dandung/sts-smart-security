import ollama
import time

# PENTING: Ganti string ini sesuai model yang sudah Anda download
# Bisa 'llama3', 'llama3.2', 'mistral', dsb.
MODEL_NAME = "llama3" 

# Data simulasi (Ceritanya ini data dari sensor/kamera)
data_masuk = {
    "sensor": "Kamera Garasi",
    "jam": "03:15 WIB",
    "deteksi_visual": "Seseorang memakai hoodie hitam, membawa senter",
    "status_rumah": "Penghuni sedang tidur"
}

print(f"--- Memulai koneksi ke model {MODEL_NAME}... ---")
start_time = time.time()

try:
    # Mengirim request ke Local LLM
    response = ollama.chat(model=MODEL_NAME, messages=[
      {
        'role': 'user',
        'content': f"""
        Bertindaklah sebagai Sistem Keamanan Cerdas.
        Analisa data berikut secara singkat dan tegas:
        
        Lokasi: {data_masuk['sensor']}
        Waktu: {data_masuk['jam']}
        Visual: {data_masuk['deteksi_visual']}
        Status: {data_masuk['status_rumah']}
        
        Berikan output format JSON saja dengan key: 
        1. tingkat_bahaya (Rendah/Sedang/Tinggi/Kritis)
        2. analisis_singkat
        3. rekomendasi_tindakan
        """
      },
    ])

    end_time = time.time()
    durasi = end_time - start_time

    # Menampilkan hasil
    print("\n" + "="*30)
    print("HASIL ANALISA AI:")
    print("="*30)
    print(response['message']['content'])
    print("="*30)
    print(f"Waktu proses: {durasi:.2f} detik")

except ollama.ResponseError as e:
    print(f"\nERROR: Model '{MODEL_NAME}' tidak ditemukan.")
    print("Pastikan Anda sudah mengetik 'ollama pull llama3' di terminal.")
except Exception as e:
    print(f"\nERROR: Gagal terhubung ke Ollama.")
    print(f"Penyebab: {e}")
    print("Pastikan aplikasi Ollama sudah berjalan (cek system tray).")
