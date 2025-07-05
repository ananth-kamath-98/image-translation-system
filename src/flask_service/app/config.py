import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    COGNITO_DOMAIN = os.getenv("COGNITO_DOMAIN")
    COGNITO_USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
    COGNITO_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")
    COGNITO_CLIENT_SECRET = os.getenv("COGNITO_CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    REGION = os.getenv("REGION")
    JWKS_URL = f"https://cognito-idp.{REGION}.amazonaws.com/{COGNITO_USER_POOL_ID}/.well-known/jwks.json"
