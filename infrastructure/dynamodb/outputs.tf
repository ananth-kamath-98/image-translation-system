output "user_profile_table_name" {
  value = aws_dynamodb_table.user_profile.name
}

output "translation_requests_table_name" {
  value = aws_dynamodb_table.translation_requests.name
}
