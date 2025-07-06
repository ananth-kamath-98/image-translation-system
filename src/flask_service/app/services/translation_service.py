from decimal import Decimal

from app.models.translation_request import TranslationRequestModel


class TranslationService:
    """
    Service layer for translation request operations
    """

    def __init__(self):
        self.translation_request_model = TranslationRequestModel()

    def get_translation_stats(self, user_id):
        """
        Get aggregated translation statistics for a user
        :param user_id:
        :return:
        """
        return self.translation_request_model.get_stats(user_id)

    def list_recent_translations(self, user_id):
        """
        Retrieve recent translation requests for a user
        :param user_id:
        :return:
        """
        items = self.translation_request_model.query_by_user(user_id)

        for item in items:
            for k, v in item.items():
                if isinstance(v, Decimal):
                    item[k] = int(v)

        return items
