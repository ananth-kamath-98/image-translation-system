resource "aws_lambda_function" "post_confirmation" {
  filename      = "${path.module}/post_login_confirmation.zip"
  function_name = "lenslate-post-confirmation"
  handler       = "post_login_confirmation.handler"
  runtime       = "python3.9"
  role          = aws_iam_role.post_confirmation_role.arn

  environment {
    variables = {
      USER_PROFILE_TABLE = aws_dynamodb_table.user_profiles.name
      REGION             = "us-east-1"
    }
  }
}