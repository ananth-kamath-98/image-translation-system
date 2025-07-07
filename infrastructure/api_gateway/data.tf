data "terraform_remote_state" "cognito" {
  backend = "local"
  config = { path = "../cognito/terraform.tfstate" }
}