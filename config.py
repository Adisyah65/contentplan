import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Pengaturan dasar aplikasi."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'daytama_contentplan_secret_2025'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Maksimal ukuran file 16 MB

class DevelopmentConfig(Config):
    """Pengaturan untuk mode development (coding lokal)."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'contentplan.db')
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Pengaturan untuk mode production (saat sudah online di server)."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_ECHO = False

# Kamus konfigurasi untuk memudahkan pemanggilan di app.py
config = {
    'development': DevelopmentConfig,
    'production':  ProductionConfig,
    'default':     DevelopmentConfig
}
