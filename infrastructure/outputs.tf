output "cognito_user_pool_id" {
  value       = module.cognito.user_pool_id
  description = "ID of the Cognito User Pool"
}

output "cognito_client_id" {
  value       = module.cognito.user_pool_client_id
  description = "Cognito App Client ID"
}

output "api_gateway_id" {
  value       = module.api_gateway.api_id
  description = "API Gateway REST API ID"
}

output "translation_table_name" {
  value       = module.dynamodb.table_name
  description = "DynamoDB translationHistory table name"
}
