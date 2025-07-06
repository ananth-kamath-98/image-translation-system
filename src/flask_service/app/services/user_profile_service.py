from app.models.user_profile import UserProfileModel


class UserService:
    """
    Service operations to perform user profile operations.
    """

    def __init__(self):
        self.user_profile_instance = UserProfileModel()

    def get_user_profile_by_id(self, user_id):
        return self.user_profile_instance.get_profile(user_id)
