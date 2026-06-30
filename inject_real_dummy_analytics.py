import random
from app import app
from models import db, Content, Analytics

with app.app_context():
    # 1. Hapus dummy data sebelumnya yang salah tema
    dummy_titles = [
        "Promo Paket Liburan Bali 2026",
        "Vlog Jalan-Jalan Bromo",
        "Tips Packing Liburan"
    ]
    
    contents_to_delete = Content.query.filter(Content.title.in_(dummy_titles)).all()
    for c in contents_to_delete:
        db.session.delete(c)
    
    if contents_to_delete:
        db.session.commit()
        print(f"Dihapus {len(contents_to_delete)} konten dummy lama.")

    # 2. Ambil semua konten yang sudah ada di database (yang dibuat user)
    existing_contents = Content.query.all()
    
    analytics_added = 0
    for content in existing_contents:
        # Cek apakah konten ini sudah punya data analitik
        existing_analytics = Analytics.query.filter_by(content_id=content.id).first()
        
        if not existing_analytics:
            # Jika belum ada, buatkan data analitik random
            likes = random.randint(150, 4500)
            views = random.randint(3000, 25000)
            shares = random.randint(20, 800)
            
            # Khusus TikTok biasanya views lebih besar
            if content.platform == 'tiktok':
                views = random.randint(15000, 100000)
                likes = random.randint(1000, 15000)
                
            new_analytics = Analytics(
                content_id=content.id,
                likes=likes,
                views=views,
                shares=shares
            )
            db.session.add(new_analytics)
            analytics_added += 1

    db.session.commit()
    print(f"Berhasil menambahkan data analitik untuk {analytics_added} konten Haji/Umroh Anda!")
