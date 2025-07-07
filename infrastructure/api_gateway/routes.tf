resource "aws_apigatewayv2_route" "login_route" {
  api_id    = aws_apigatewayv2_api.lenslate_api.id
  route_key = "GET /login"
  target    = "integrations/${aws_apigatewayv2_integration.login.id}"
}
resource "aws_apigatewayv2_route" "callback_route" {
  api_id    = aws_apigatewayv2_api.lenslate_api.id
  route_key = "GET /oauth2/callback"
  target    = "integrations/${aws_apigatewayv2_integration.callback.id}"
}
resource "aws_apigatewayv2_route" "dashboard_route" {
  api_id             = aws_apigatewayv2_api.lenslate_api.id
  route_key          = "GET /dashboard"
  target             = "integrations/${aws_apigatewayv2_integration.dashboard.id}"
  authorization_type = "JWT"
  authorizer_id      = aws_apigatewayv2_authorizer.cognito_auth.id
}