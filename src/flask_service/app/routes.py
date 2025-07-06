# from flask import Blueprint, redirect, request, make_response, jsonify
#
# from .auth import get_auth_url, exchange_code, verify_token
#
# main = Blueprint('main', __name__)
#
#
# @main.route('/login')
# def login():
#     return redirect(get_auth_url())
#
#
# @main.route('/oauth2/callback')
# def callback():
#     code = request.args.get('code')
#     if not code:
#         return 'Missing code', 400
#     tokens = exchange_code(code)
#     id_token = tokens.get('id_token')
#     if not id_token:
#         return 'No id_token returned', 400
#     claims = verify_token(id_token)
#     response = make_response(redirect('/dashboard'))
#     response.set_cookie('id_token', id_token, httponly=True, secure=True)
#     return response
#
#
# @main.route('/dashboard')
# def dashboard():
#     token = request.cookies.get('id_token')
#     if not token:
#         return redirect('/login')
#     try:
#         claims = verify_token(token)
#     except Exception as e:
#         return f'Invalid token: {str(e)}', 401
#     return jsonify({
#         'message': f"Welcome, {claims.get('email')}",
#         'claims': claims
#     })
