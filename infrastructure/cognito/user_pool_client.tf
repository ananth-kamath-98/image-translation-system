resource "aws_cognito_user_pool_client" "lenslate_client" {
  name         = "lenslate-app-client"
  user_pool_id = aws_cognito_user_pool.lenslate_pool.id

  generate_secret              = false
  supported_identity_providers = ["COGNITO"]

  explicit_auth_flows = [
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH"
  ]

  allowed_oauth_flows                   = ["code"]
  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_scopes                  = ["openid", "email", "profile"]

  callback_urls = [
    "https://<api-id>.execute-api.us-east-1.amazonaws.com/oauth2/callback"
  ]
  logout_urls = [
    "https://<api-id>.execute-api.us-east-1.amazonaws.com/"
  ]
}