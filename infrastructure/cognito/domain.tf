resource "aws_cognito_user_pool_domain" "lenslate_domain" {
  domain       = "lenslate-auth-domain"
  user_pool_id = aws_cognito_user_pool.lenslate_pool.id
}