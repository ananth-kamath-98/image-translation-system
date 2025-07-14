variable "aws_region" { type = string }
variable "environment" { type = string }
variable "user_pool_id" { type = string }

locals {
  user_pool_arn = "arn:aws:cognito-idp:${var.aws_region}:${data.aws_caller_identity.current.account_id}:userpool/${var.user_pool_id}"
}

data "aws_caller_identity" "current" {}

output "api_id" {
  value = aws_api_gateway_rest_api.this.id
}