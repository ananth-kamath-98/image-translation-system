from datetime import datetime

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

    def upsert_profile(self, user_id: str, email: str, created_at: str):
        try:
            self.table.put_item(
                Item={
                    "user_id": user_id,
                    "email": email,
                    "created_at": created_at,
                    "preferences": {}
                },
                ConditionExpression="attribute_not_exists(user_id)"
            )
        except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
            pass
