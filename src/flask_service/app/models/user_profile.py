from app.resources import dynamodb


class UserProfileModel:
    """
    Wrapper for the user profile model.
    """

    def __init__(self):
        self.table = dynamodb.Table('user_profile')

    def get_profile(self, user_id: str):
        """
        Get a user profile by its user id.
        :param user_id:
        :return: user profile object
        """
        response = self.table.get_item(Key={'user_id': user_id})
        return response.get('Item', {})
