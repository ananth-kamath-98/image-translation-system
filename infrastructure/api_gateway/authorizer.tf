resource "aws_apigatewayv2_authorizer" "cognito_auth" {
  api_id          = aws_apigatewayv2_api.lenslate_api.id
  name            = "CognitoAuthorizer"
  authorizer_type = "JWT"
  identity_sources = ["$request.header.Authorization"]

  jwt_configuration {
    issuer   = "https://cognito-idp.us-east-1.amazonaws.com/${data.terraform_remote_state.cognito.outputs.user_pool_id}"
    audience = [data.terraform_remote_state.cognito.outputs.app_client_id]
  }
}