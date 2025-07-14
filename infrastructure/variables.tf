variable "aws_region" {
  type        = string
  description = "AWS region, e.g. us-east-1"
  default     = "us-east-1"
}

variable "environment" {
  type        = string
  description = "Deployment environment tag"
  default     = "dev"
}
