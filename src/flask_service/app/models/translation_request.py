import boto3
import boto3.dynamodb.conditions as conditions
import os

from app.resources import dynamodb


class TranslationRequestModel:
    """
    Wrapper for the TranslationRequests DynamoDB table.
    """

    def __init__(self, table_name: str = None):
        self.table = dynamodb.Table(
            table_name or os.getenv('TRANSLATIONS_TABLE',
                                    'TranslationRequests'))

    def query_by_user(self, user_id: str, limit: int = 10,
                      latest_first: bool = True) -> list:
        """
        Query the latest translation requests for a user.
        """
        params = {
            'IndexName': 'user_id-index',
            'KeyConditionExpression': Key('user_id').eq(user_id),
            'Limit': limit,
            'ScanIndexForward': not latest_first
        }
        response = self.table.query(**params)
        return response.get('Items', [])

    def get_stats(self, user_id: str) -> dict:
        """
        Aggregate count statistics for a user's translation requests.
        Returns dict with keys: total, pending, successful, failed.
        """
        response = self.table.query(
            IndexName='user_id-index',
            KeyConditionExpression=Key('user_id').eq(user_id),
            ProjectionExpression='status'
        )
        items = response.get('Items', [])
        stats = {'total': len(items), 'pending': 0, 'successful': 0,
                 'failed': 0}
        for item in items:
            status = item.get('status')
            if status == 'PENDING':
                stats['pending'] += 1
            elif status == 'SUCCESS':
                stats['successful'] += 1
            elif status == 'FAILED':
                stats['failed'] += 1
        return stats
