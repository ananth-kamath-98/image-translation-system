resource "aws_iam_role" "post_confirmation_role" {
  name               = "lenslate-post-confirmation-role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume.json
}
resource "aws_iam_role_policy" "post_confirm_policy" {
  name   = "lenslate-post-confirmation-policy"
  role   = aws_iam_role.post_confirmation_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action   = ["dynamodb:PutItem"],
      Effect   = "Allow",
      Resource = aws_dynamodb_table.user_profiles.arn
    }]
  })
}