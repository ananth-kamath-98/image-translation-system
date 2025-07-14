variable "aws_region" {
  type = string
}

variable "environment" {
  type = string
}

output "table_name" {
  value = aws_dynamodb_table.translation_history.name
}