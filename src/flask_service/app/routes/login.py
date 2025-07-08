from flask import Blueprint, redirect, request, make_response

from ..auth import get_auth_url, exchange_code, verify_token

main = Blueprint('main', __name__)


@main.route('/login')
def login():
    return redirect(get_auth_url())


@main.route('/oauth2/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'Missing code', 400

    # Exchange the code for tokens
    tokens = exchange_code(code)
    id_token = tokens.get('id_token')
    if not id_token:
        return 'No id_token returned', 400
    claims = verify_token(id_token)

    # On first login, write user profile to user_profile table in database

    response = make_response(redirect('/dashboard'))
    response.set_cookie('id_token', id_token, httponly=True, secure=True)
    return response


@main.route('/logout')
def logout():
    response = make_response(redirect(get_auth_url()))
    response.delete_cookie('id_token', path='/', httponly=True)
    return response
