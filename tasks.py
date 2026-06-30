# tasks.py
from datetime import datetime
from models import db, Schedule
from instagram_api import publish_to_instagram

def job_auto_posting(app):
    with app.app_context():
        # print("Memulai pengecekan jadwal otomatis...")
        target_time = datetime.now()
        
        # Mencari jadwal yang waktunya sudah tiba dan belum diposting
        pending_schedules = Schedule.query.filter(
            Schedule.scheduled_datetime <= target_time,
            Schedule.is_posted == False
        ).all()

        for sched in pending_schedules:
            print(f"\n[SCHEDULER] Memproses posting: {sched.content.title}")
            
            # Panggil fungsi instagram API (simulasi/asli)
            sukses = publish_to_instagram(sched.content.media_url, sched.content.caption)
            
            if sukses:
                # Update status di database
                sched.is_posted = True
                sched.posted_at = datetime.now()
                sched.content.status = 'posted'
                db.session.commit()
                print(f"[SCHEDULER] Status Konten '{sched.content.title}' berhasil diubah menjadi tayang (posted).\n")
            else:
                print(f"[SCHEDULER] Gagal memposting Konten '{sched.content.title}'\n")