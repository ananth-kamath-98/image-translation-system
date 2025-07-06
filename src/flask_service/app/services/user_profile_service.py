import time

from app.models.user_profile import UserProfileModel


class UserService:
    """
    Service operations to perform user profile operations.
    """

    def __init__(self):
        self.user_profile_instance = UserProfileModel()

    def get_user_profile_by_id(self, user_id):
        return self.user_profile_instance.get_profile(user_id)

    def create_user_profile_from_claims(self, claims):
        user_id = claims['sub']
        email = claims.get('email')
        now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        self.create_user_profile(user_id, email, now_iso)

    def create_user_profile(self, user_id: str, email: str, now_iso: time):
        pass