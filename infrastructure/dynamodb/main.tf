terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# DynamoDB table for storing user translation requests
resource "aws_dynamodb_table" "translation_requests" {
  name         = "TranslationRequests"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "requestId"

  attribute {
    name = "userId"
    type = "S"
  }
  attribute {
    name = "requestId"
    type = "S"
  }
  attribute {
    name = "createdAt"
    type = "S"
  }
  attribute {
    name = "status"
    type = "S"
  }

  attribute {
    name = "originalImageKey"
    type = "S"
  }
  attribute {
    name = "thumbnailKey"
    type = "S"
  }
  attribute {
    name = "sourceLanguage"
    type = "S"
  }
  attribute {
    name = "targetLanguage"
    type = "S"
  }

  # Text fields
  attribute {
    name = "extractedText"
    type = "S"
  }
  attribute {
    name = "translatedText"
    type = "S"
  }

  local_secondary_index {
    name            = "createdAt-index"
    range_key       = "createdAt"
    projection_type = "ALL"
  }

  global_secondary_index {
    name            = "status-index"
    hash_key        = "userId"
    range_key       = "status"
    projection_type = "ALL"
  }

  tags = {
    Environment = "dev"
    Project     = "ImageTranslation"
  }
}

# DynamoDB table for storing user profile metadata
resource "aws_dynamodb_table" "user_profiles" {
  name         = "UserProfiles"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"

  attribute {
    name = "userId"
    type = "S"
  }

  tags = {
    Environment = "dev"
    Project     = "ImageTranslation"
  }
}
