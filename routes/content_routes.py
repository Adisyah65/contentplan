from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from datetime import datetime

from models import db, Content, Schedule

content_bp = Blueprint('content', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@content_bp.route('/konten')
@login_required
def konten_list():
    status_filter   = request.args.get('status', '')
    platform_filter = request.args.get('platform', '')
    kata_cari       = request.args.get('cari', '')

    query = Content.query

    if status_filter:
        query = query.filter_by(status=status_filter)
    if platform_filter:
        query = query.filter_by(platform=platform_filter)
    if kata_cari:
        query = query.filter(Content.title.ilike(f'%{kata_cari}%'))

    semua_konten = query.order_by(Content.created_at.desc()).all()

    return render_template('konten.html', konten_list=semua_konten, status_filter=status_filter, platform_filter=platform_filter, kata_cari=kata_cari)

@content_bp.route('/konten/baru', methods=['GET', 'POST'])
@login_required
def konten_baru():
    if request.method == 'POST':
        judul          = request.form.get('title', '').strip()
        caption        = request.form.get('caption', '').strip()
        platform       = request.form.get('platform', '')
        tgl_jadwal     = request.form.get('scheduled_date', '')
        jam_jadwal     = request.form.get('scheduled_time', '')

        if not judul or not caption or not platform:
            flash('Judul, caption, dan platform wajib diisi.', 'danger')
            return render_template('form_konten.html')

        media_url = None
        if 'media' in request.files:
            file = request.files['media']
            if file and file.filename != '' and allowed_file(file.filename):
                nama_file = secure_filename(file.filename)
                path_file = os.path.join(current_app.config['UPLOAD_FOLDER'], nama_file)
                file.save(path_file)
                media_url = f'static/uploads/{nama_file}'

        konten_baru = Content(
            title    = judul,
            caption  = caption,
            platform = platform,
            media_url= media_url,
            status   = 'draft',
            user_id  = current_user.id
        )
        db.session.add(konten_baru)
        db.session.flush()

        if tgl_jadwal and jam_jadwal:
            try:
                waktu_jadwal = datetime.strptime(f'{tgl_jadwal} {jam_jadwal}', '%Y-%m-%d %H:%M')
                jadwal = Schedule(content_id=konten_baru.id, scheduled_datetime=waktu_jadwal)
                db.session.add(jadwal)
                konten_baru.status = 'scheduled'
            except ValueError:
                flash('Format tanggal/jam tidak valid.', 'danger')
                db.session.rollback()
                return render_template('form_konten.html')

        db.session.commit()
        flash(f'Konten "{judul}" berhasil dibuat! [OK]', 'success')
        return redirect(url_for('content.konten_list'))

    return render_template('form_konten.html', konten=None)

@content_bp.route('/konten/<int:id_konten>/edit', methods=['GET', 'POST'])
@login_required
def konten_edit(id_konten):
    konten = Content.query.get_or_404(id_konten)

    if request.method == 'POST':
        konten.title    = request.form.get('title', konten.title).strip()
        konten.caption  = request.form.get('caption', konten.caption).strip()
        konten.platform = request.form.get('platform', konten.platform)

        if 'media' in request.files:
            file = request.files['media']
            if file and file.filename != '' and allowed_file(file.filename):
                nama_file = secure_filename(file.filename)
                path_file = os.path.join(current_app.config['UPLOAD_FOLDER'], nama_file)
                file.save(path_file)
                konten.media_url = f'static/uploads/{nama_file}'

        tgl_jadwal = request.form.get('scheduled_date', '')
        jam_jadwal = request.form.get('scheduled_time', '')

        if tgl_jadwal and jam_jadwal:
            try:
                waktu_jadwal = datetime.strptime(f'{tgl_jadwal} {jam_jadwal}', '%Y-%m-%d %H:%M')
                if konten.schedule:
                    konten.schedule.scheduled_datetime = waktu_jadwal
                    konten.schedule.is_posted = False
                else:
                    jadwal_baru = Schedule(content_id=konten.id, scheduled_datetime=waktu_jadwal)
                    db.session.add(jadwal_baru)
                konten.status = 'scheduled'
            except ValueError:
                flash('Format tanggal/jam tidak valid.', 'danger')
                return render_template('form_konten.html', konten=konten)

        db.session.commit()
        flash(f'Konten "{konten.title}" berhasil diperbarui! [OK]', 'success')
        return redirect(url_for('content.konten_list'))

    return render_template('form_konten.html', konten=konten)

@content_bp.route('/konten/<int:id_konten>/hapus', methods=['POST'])
@login_required
def konten_hapus(id_konten):
    konten = Content.query.get_or_404(id_konten)
    judul  = konten.title

    db.session.delete(konten)
    db.session.commit()

    flash(f'Konten "{judul}" berhasil dihapus.', 'info')
    return redirect(url_for('content.konten_list'))
