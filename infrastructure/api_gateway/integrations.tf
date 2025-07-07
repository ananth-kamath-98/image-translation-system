resource "aws_apigatewayv2_integration" "login" {
  api_id                 = aws_apigatewayv2_api.lenslate_api.id
  integration_type       = "HTTP_PROXY"
  integration_method     = "GET"
  integration_uri        = "https://<ngrok-url>/login"
  payload_format_version = "1.0"
}
resource "aws_apigatewayv2_integration" "callback" {
  api_id                 = aws_apigatewayv2_api.lenslate_api.id
  integration_type       = "HTTP_PROXY"
  integration_method     = "GET"
  integration_uri        = "https://<ngrok-url>/oauth2/callback"
  payload_format_version = "1.0"
}
resource "aws_apigatewayv2_integration" "dashboard" {
  api_id                 = aws_apigatewayv2_api.lenslate_api.id
  integration_type       = "HTTP_PROXY"
  integration_method     = "GET"
  integration_uri        = "https://<ngrok-url>/dashboard"
  payload_format_version = "1.0"
}