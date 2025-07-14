module "cognito" {
  source      = "./modules/cognito"
  aws_region  = var.aws_region
  environment = var.environment
}

module "api_gateway" {
  source         = "./modules/api_gateway"
  aws_region     = var.aws_region
  environment    = var.environment
  user_pool_id   = module.cognito.user_pool_id
}

module "dynamodb" {
  source      = "./modules/dynamodb"
  aws_region  = var.aws_region
  environment = var.environment
}