import os
import requests
import logging
from dotenv import load_dotenv

# Load variabel lingkungan
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

def publish_to_instagram(media_path, caption, is_video=False):
    """
    Fungsi untuk memposting konten ke Instagram.
    Karena Meta Graph API butuh URL Publik untuk gambar (bukan local path), 
    kita biasanya mensimulasikan upload atau butuh server publik (seperti ngrok).
    """
    # Ambil token dari .env
    access_token = os.getenv('IG_ACCESS_TOKEN')
    ig_user_id = os.getenv('IG_ACCOUNT_ID')

    # Mengecek apakah token sudah diisi atau masih default
    if not access_token or access_token == "masukkan_token_disini":
        logging.warning("[!] IG_ACCESS_TOKEN belum dikonfigurasi di .env")
        logging.info(f"[SIMULASI] [SIMULASI] Memposting konten ke Instagram: {media_path}")
        logging.info(f"[NOTE] Caption: {caption}")
        logging.info("[OK] [SIMULASI] Posting berhasil! (Mode Simulasi aktif karena token kosong)")
        return True

    # =======================================================
    # JIKA TOKEN SUDAH ADA (KODE ASLI UNTUK META GRAPH API)
    # =======================================================
    try:
        # Step 1: Upload Media Container
        graph_url = f'https://graph.facebook.com/v19.0/{ig_user_id}/media'
        
        # API Instagram mewajibkan image_url berupa link publik (misal: https://daytama.com/static/uploads/...)
        # Untuk contoh ini kita asumsikan media_path adalah URL yang bisa diakses publik
        payload = {
            'image_url': media_path, 
            'caption': caption,
            'access_token': access_token
        }
        
        if is_video:
            payload.pop('image_url')
            payload['video_url'] = media_path
            payload['media_type'] = 'REELS'

        logging.info(f"Mengirim permintaan upload media ke Meta API...")
        r = requests.post(graph_url, data=payload)
        res = r.json()

        if 'id' not in res:
            logging.error(f"[ERROR] Gagal membuat media container: {res}")
            return False

        creation_id = res['id']
        logging.info(f"[OK] Media container berhasil dibuat. ID: {creation_id}")

        # Step 2: Publish Media
        publish_url = f'https://graph.facebook.com/v19.0/{ig_user_id}/media_publish'
        publish_payload = {
            'creation_id': creation_id,
            'access_token': access_token
        }

        logging.info("Mempublikasikan konten...")
        r_pub = requests.post(publish_url, data=publish_payload)
        res_pub = r_pub.json()

        if 'id' in res_pub:
            logging.info(f"[SUCCESS] SUKSES! Konten berhasil di-post ke Instagram dengan ID: {res_pub['id']}")
            return True
        else:
            logging.error(f"[ERROR] Gagal mempublikasikan konten: {res_pub}")
            return False

    except Exception as e:
        logging.error(f"[ERROR] Terjadi kesalahan saat menghubungi API Instagram: {str(e)}")
        return False
