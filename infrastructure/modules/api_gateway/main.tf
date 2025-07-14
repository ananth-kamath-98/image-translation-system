resource "aws_api_gateway_rest_api" "this" {
  name        = "translation-api-${var.environment}"
  description = "REST API for image translation"
}

resource "aws_api_gateway_authorizer" "cognito" {
  name            = "cognito-authorizer"
  rest_api_id     = aws_api_gateway_rest_api.this.id
  type            = "COGNITO_USER_POOLS"
  provider_arns   = [local.user_pool_arn]
  identity_source = "method.request.header.Authorization"
}
