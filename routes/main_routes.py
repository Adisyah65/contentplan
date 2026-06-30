from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import pytz
from datetime import datetime

from models import db, Content, Schedule, Analytics

main_bp = Blueprint('main', __name__)

def get_dashboard_stats():
    return {
        'total':     Content.query.count(),
        'draft':     Content.query.filter_by(status='draft').count(),
        'scheduled': Content.query.filter_by(status='scheduled').count(),
        'posted':    Content.query.filter_by(status='posted').count(),
    }

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    stats = get_dashboard_stats()
    konten_terbaru = Content.query.order_by(Content.created_at.desc()).limit(5).all()
    
    jadwal_mendatang = (
        Schedule.query
        .filter(
            Schedule.is_posted == False,
            Schedule.scheduled_datetime >= datetime.now(pytz.timezone('Asia/Jakarta')).replace(tzinfo=None)
        )
        .order_by(Schedule.scheduled_datetime.asc())
        .limit(5)
        .all()
    )

    return render_template('dashboard.html', stats=stats, konten_terbaru=konten_terbaru, jadwal_mendatang=jadwal_mendatang)

@main_bp.route('/kalender')
@login_required
def kalender():
    semua_jadwal = Schedule.query.filter_by(is_posted=False).order_by(Schedule.scheduled_datetime.asc()).all()

    events = []
    for j in semua_jadwal:
        if j.content:
            events.append({
                'id':      j.id,
                'title':   j.content.title,
                'start':   j.scheduled_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
                'platform':j.content.platform,
                'status':  j.content.status,
                'color':   '#F5C518' if j.content.platform == 'instagram' else '#1A1A1A'
            })

    return render_template('kalender.html', events=events)

@main_bp.route('/analitik')
@login_required
def analitik():
    from sqlalchemy import func
    data_analitik_query = (
        db.session.query(
            Content.title,
            Content.platform,
            func.sum(Analytics.likes).label('total_likes'),
            func.sum(Analytics.views).label('total_views'),
            func.sum(Analytics.shares).label('total_shares'),
        )
        .join(Analytics, Content.id == Analytics.content_id)
        .group_by(Content.id, Content.title, Content.platform)
        .order_by(func.sum(Analytics.views).desc())
        .all()
    )

    # Konversi SQLAlchemy Row menjadi list of dict agar bisa di-serialize ke JSON
    data_analitik = []
    for row in data_analitik_query:
        data_analitik.append({
            'title': row.title,
            'platform': row.platform,
            'total_likes': int(row.total_likes or 0),
            'total_views': int(row.total_views or 0),
            'total_shares': int(row.total_shares or 0)
        })

    total_likes  = sum(row['total_likes'] for row in data_analitik)
    total_views  = sum(row['total_views'] for row in data_analitik)
    total_shares = sum(row['total_shares'] for row in data_analitik)

    return render_template('analitik.html', data_analitik=data_analitik, total_likes=total_likes, total_views=total_views, total_shares=total_shares)
