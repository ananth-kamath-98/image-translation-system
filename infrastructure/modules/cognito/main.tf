resource "aws_cognito_user_pool" "this" {
  name                     = "translation-user-pool-${var.environment}"
  auto_verified_attributes = ["email"]
  password_policy {
    minimum_length    = 8
    require_lowercase = true
    require_uppercase = true
    require_numbers   = true
    require_symbols   = false
  }
}

resource "aws_cognito_user_pool_client" "this" {
  name                 = "translation-client-${var.environment}"
  user_pool_id         = aws_cognito_user_pool.this.id
  generate_secret      = false
  explicit_auth_flows  = ["ALLOW_USER_SRP_AUTH","ALLOW_USER_PASSWORD_AUTH","ALLOW_REFRESH_TOKEN_AUTH"]
  callback_urls        = ["http://localhost:3000/callback"]
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_flows  = ["code"]
  allowed_oauth_scopes = ["openid","email","profile"]
  supported_identity_providers = ["COGNITO"]
}