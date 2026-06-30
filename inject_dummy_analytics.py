from app import app
from models import db, Content, Analytics, User

with app.app_context():
    # 1. Dapatkan user admin
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        print("Error: User admin tidak ditemukan!")
        exit()

    # 2. Buat Dummy Konten
    c1 = Content(title="Promo Paket Liburan Bali 2026", caption="Liburan hemat dan seru di Bali!", platform="instagram", status="posted", user_id=admin.id)
    c2 = Content(title="Vlog Jalan-Jalan Bromo", caption="Serunya mengejar sunrise di Bromo!", platform="tiktok", status="posted", user_id=admin.id)
    c3 = Content(title="Tips Packing Liburan", caption="Jangan sampai ketinggalan barang penting ini", platform="instagram", status="posted", user_id=admin.id)
    
    db.session.add_all([c1, c2, c3])
    db.session.commit() # Commit agar mendapatkan ID konten

    # 3. Buat Dummy Analitik
    a1 = Analytics(content_id=c1.id, likes=1250, views=15400, shares=320)
    a2 = Analytics(content_id=c2.id, likes=8900, views=45000, shares=1250)
    a3 = Analytics(content_id=c3.id, likes=450, views=3200, shares=85)
    
    db.session.add_all([a1, a2, a3])
    db.session.commit()

    print("✅ Berhasil menambahkan data analitik simulasi (dummy data)!")
