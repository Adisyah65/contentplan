from flask import Blueprint, jsonify
from flask_login import login_required
from models import Content
from routes.main_routes import get_dashboard_stats

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/konten')
@login_required
def api_konten():
    semua_konten = Content.query.order_by(Content.created_at.desc()).all()
    return jsonify([k.to_dict() for k in semua_konten])

@api_bp.route('/stats')
@login_required
def api_stats():
    return jsonify(get_dashboard_stats())
