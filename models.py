import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """Tabel 'user' — menyimpan data akun admin."""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    contents = db.relationship('Content', backref='author', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Content(db.Model):
    """Tabel 'content' — menyimpan rancangan konten media sosial."""
    __tablename__ = 'content'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    caption = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.String(500), nullable=True)
    platform = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='draft')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    schedule = db.relationship('Schedule', backref='content', uselist=False, cascade='all, delete-orphan')
    analytics = db.relationship('Analytics', backref='content', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Content {self.id}: {self.title} [{self.status}]>'

    def to_dict(self):
        return {
            'id':         self.id,
            'title':      self.title,
            'caption':    self.caption,
            'media_url':  self.media_url,
            'platform':   self.platform,
            'status':     self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M')
        }

class Schedule(db.Model):
    """Tabel 'schedule' — menyimpan jadwal auto-posting."""
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False, unique=True)
    scheduled_datetime = db.Column(db.DateTime, nullable=False)
    posted_at = db.Column(db.DateTime, nullable=True)
    is_posted = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Schedule content_id={self.content_id} @ {self.scheduled_datetime}>'

    def to_dict(self):
        return {
            'id':                 self.id,
            'content_id':         self.content_id,
            'scheduled_datetime': self.scheduled_datetime.strftime('%Y-%m-%d %H:%M'),
            'posted_at':          self.posted_at.strftime('%Y-%m-%d %H:%M') if self.posted_at else None,
            'is_posted':          self.is_posted,
        }

class Analytics(db.Model):
    """Tabel 'analytics' — menyimpan data performa konten."""
    __tablename__ = 'analytics'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    likes = db.Column(db.Integer, default=0, nullable=False)
    views = db.Column(db.Integer, default=0, nullable=False)
    shares = db.Column(db.Integer, default=0, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'<Analytics content_id={self.content_id} likes={self.likes} views={self.views}>'

    def to_dict(self):
        return {
            'id':         self.id,
            'content_id': self.content_id,
            'likes':      self.likes,
            'views':      self.views,
            'shares':     self.shares,
            'timestamp':  self.timestamp.strftime('%Y-%m-%d %H:%M'),
        }

def init_db(app):
    """Membuat database dan semua tabel jika belum ada."""
    db.init_app(app)
    with app.app_context():
        os.makedirs(os.path.join(os.path.dirname(__file__), 'instance'), exist_ok=True)
        db.create_all()
        print("[OK] Database berhasil dibuat/dimuat!")
