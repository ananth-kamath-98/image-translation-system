from flask import Blueprint, request, redirect, jsonify

from app.auth import verify_token
from app.services.translation_service import TranslationService
from app.services.user_profile_service import UserService

dashboard_blue_print = Blueprint('dashboard', __name__)
user_service = UserService()
translation_service = TranslationService()


@dashboard_blue_print.route('/dashboard')
def dashboard():
    token = request.cookies.get('id_token')
    if not token:
        return redirect('/login')
    try:
        claims = verify_token(token)
    except Exception as e:
        return f'Invalid token: {str(e)}', 401
    return jsonify({
        'message': f"Welcome, {claims.get('email')}",
        'claims': claims
    })


@dashboard_blue_print.route('/user/profile', methods=['GET'])
def get_user_profile():
    auth = request.environ.get('authorizer')
    user_id = auth['claims']['sub'] if auth else request.args.get('user_id')
