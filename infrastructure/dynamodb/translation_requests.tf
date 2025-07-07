resource "aws_dynamodb_table" "translation_requests" {
  name         = "TranslationRequests"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "user_id"
  sort_key     = "timestamp"

  attribute {
    name = "user_id"
    type = "S"
  }
  attribute {
    name = "timestamp"
    type = "S"
  }

  tags = {
    Environment = "dev"
    Project     = "ImageTranslation"
  }
}