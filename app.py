from flask import Flask
from flask_login import LoginManager
from flask_apscheduler import APScheduler
from werkzeug.security import generate_password_hash
import os
import pytz
from datetime import datetime

from config import config
from models import db, init_db, User
from tasks import job_auto_posting

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.content_routes import content_bp
from routes.api_routes import api_bp

# Paksa menggunakan zona waktu Jakarta (WIB)
wib = pytz.timezone('Asia/Jakarta')

app = Flask(__name__)
app.config.from_object(config['development'])

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

app.jinja_env.globals['now'] = lambda: datetime.now(wib).replace(tzinfo=None)

init_db(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Silakan login terlebih dahulu.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ============================================================
# APSCHEDULER
# ============================================================
scheduler = APScheduler()
scheduler.init_app(app)

@scheduler.task('interval', id='auto_posting_job', minutes=1)
def auto_posting_task():
    job_auto_posting(app)

# ============================================================
# REGISTER BLUEPRINTS
# ============================================================
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(content_bp)
app.register_blueprint(api_bp)

# ============================================================
# MEMBUAT AKUN ADMIN PERTAMA
# ============================================================
def buat_admin_awal():
    with app.app_context():
        if User.query.count() == 0:
            admin = User(
                username      = 'admin',
                email         = 'admin@daytama.com',
                password_hash = generate_password_hash('admin123')
            )
            db.session.add(admin)
            db.session.commit()
            print('[OK] Akun admin berhasil dibuat!')
            print('   Username : admin')
            print('   Password : admin123')
            print('   [!]  Segera ganti password setelah login!')

if __name__ == '__main__':
    buat_admin_awal()

    if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        scheduler.start()

    print('\n' + '=' * 50)
    print('  ContentPlan — PT. Daytama Sinergi Wisata')
    print('  Buka browser: http://localhost:5000')
    print('=' * 50 + '\n')

    app.run(debug=True, host='0.0.0.0', port=5000)
