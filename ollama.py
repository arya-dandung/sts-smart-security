import ollama
import requests # Diperlukan untuk kirim ke WAHA
import json

# --- KONFIGURASI WAHA ---
WAHA_URL = "http://localhost:3000/api/sendText" # Sesuaikan port WAHA kamu
SESSION_ID = "default" # Session ID di WAHA
TARGET_PHONE = "628xxxxxxxxx" # Ganti dengan nomor WhatsApp tujuan

# --- DATA SIMULASI (Dari YOLOv8) ---
data_cctv = {
    "lokasi": "Area Parkir Depan",
    "waktu": "21/01/2026 15:45 WIB",
    "objek": "Seseorang, Linggis",
    "akurasi": "88%"
}

# --- 1. SUSUN PROMPT ---
prompt_system = f"""
Bertindaklah sebagai Sistem Peringatan Dini Otomatis.

Instruksi Format Output (Wajib Markdown WhatsApp):
1. Mulai langsung dengan judul: *🚨 PERINGATAN KEAMANAN DETEKSI*
2. Gunakan emoji yang sesuai.
3. Gunakan format list untuk detail.
4. Gunakan tanda *bintang* untuk menebalkan poin penting.
5. JANGAN ada teks lain selain pesan peringatan itu sendiri.

Data Deteksi:
- Lokasi: {data_cctv['lokasi']}
- Waktu: {data_cctv['waktu']}
- Objek Terdeteksi: {data_cctv['objek']}
- Tingkat Akurasi: {data_cctv['akurasi']}

Berikan analisa resiko singkat (1 kalimat) dan rekomendasi tindakan (1 kalimat).
"""

print("--- Meminta pesan ke AI... ---")

# --- 2. GENERATE PESAN DENGAN OLLAMA ---
response = ollama.chat(model='llama3', messages=[
  {'role': 'user', 'content': prompt_system},
])

# Ambil hasil bersih
pesan_whatsapp = response['message']['content']

print("\n--- PREVIEW PESAN WHATSAPP ---")
print(pesan_whatsapp)
print("------------------------------")

# --- 3. KIRIM KE WAHA (Opsional/Uncomment jika WAHA sudah jalan) ---
# payload = {
#     "chatId": f"{TARGET_PHONE}@c.us",
#     "text": pesan_whatsapp,
#     "session": SESSION_ID
# }
# try:
#     res = requests.post(WAHA_URL, json=payload)
#     if res.status_code == 201:
#         print("✅ Sukses terkirim ke WhatsApp!")
#     else:
#         print(f"❌ Gagal kirim: {res.text}")
# except Exception as e:
#     print(f"❌ Error koneksi WAHA: {e}")
