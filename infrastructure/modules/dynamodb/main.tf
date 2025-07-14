resource "aws_dynamodb_table" "translation_history" {
  name         = "translationHistory"
  billing_mode = "PAY_PER_REQUEST"

  hash_key  = "userId"
  range_key = "timestamp"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "timestamp"
    type = "S"
  }
}
