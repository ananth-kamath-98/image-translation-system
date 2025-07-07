resource "aws_apigatewayv2_api" "lenslate_api" {
  name          = "lenslate-http-api"
  protocol_type = "HTTP"
}