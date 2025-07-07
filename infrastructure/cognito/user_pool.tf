resource "aws_cognito_user_pool" "lenslate_pool" {
  name                     = "lenslate-user-pool"
  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]

  password_policy {
    minimum_length    = 8
    require_uppercase = true
    require_lowercase = true
    require_numbers   = true
    require_symbols   = false
  }

  lambda_config {
    post_confirmation = aws_lambda_function.post_confirmation.arn
  }
}