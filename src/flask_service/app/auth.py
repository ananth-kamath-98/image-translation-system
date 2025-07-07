import time

import requests
from flask import current_app
from jose import jwt, jwk
from jose.utils import base64url_decode


def get_auth_url():
    """
    Constructs the URL to enable user authentication.
    :return: login URL
    """
    domain = current_app.config['COGNITO_DOMAIN']
    client_id = current_app.config['COGNITO_CLIENT_ID']
    redirect_uri = current_app.config['REDIRECT_URI']
    return (
        f"https://{domain}/login?response_type=code"
        f"&client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&scope=openid+email+profile"
    )


def get_logout_url():
    """
    Constructs the URL to enable user logout.
    :return:
    """
    domain = current_app.config['COGNITO_DOMAIN']
    client_id = current_app.config['COGNITO_CLIENT_ID']
    logout_uri = current_app.config.get('POST_LOGOUT_REDIRECT_URI') \
                 or current_app.config['REDIRECT_URI'].rsplit('/', 1)[0]

    return (
        f"https://{domain}/logout"
        f"?client_id={client_id}"
        f"&logout_uri={logout_uri}"
    )


def exchange_code(code):
    """
    Fetches the access token for a given code and returns it.
    :param code:
    :return:
    """
    domain = current_app.config['COGNITO_DOMAIN']
    token_url = f"https://{domain}/oauth2/token"
    data = {
        'grant_type': 'authorization_code',
        'client_id': current_app.config['COGNITO_CLIENT_ID'],
        'code': code,
        'redirect_uri': current_app.config['REDIRECT_URI']
    }
    auth = None
    secret = current_app.config.get('COGNITO_CLIENT_SECRET')
    if secret:
        auth = (current_app.config['COGNITO_CLIENT_ID'], secret)
    resp = requests.post(token_url, data=data, auth=auth)
    resp.raise_for_status()
    return resp.json()


def verify_token(token):
    jwks = requests.get(current_app.config['JWKS_URL']).json()['keys']
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']
    key = next((k for k in jwks if k['kid'] == kid), None)
    if not key:
        raise Exception('Public key not found')
    public_key = jwk.construct(key)
    message, encoded_sig = token.rsplit('.', 1)
    decoded_sig = base64url_decode(encoded_sig.encode('utf-8'))
    if not public_key.verify(message.encode('utf-8'), decoded_sig):
        raise Exception('Signature verification failed')
    claims = jwt.get_unverified_claims(token)
    if time.time() > claims['exp']:
        raise Exception('Token expired')
    if claims['aud'] != current_app.config['COGNITO_CLIENT_ID']:
        raise Exception('Invalid audience')
    return claims
