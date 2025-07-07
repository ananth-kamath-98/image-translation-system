output "user_pool_id" {
  value = aws_cognito_user_pool.lenslate_pool.id
}
output "app_client_id" {
  value = aws_cognito_user_pool_client.lenslate_client.id
}
output "cognito_domain" {
  value = aws_cognito_user_pool_domain.lenslate_domain.domain
}