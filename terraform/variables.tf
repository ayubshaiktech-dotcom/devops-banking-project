variable "bucket_name" {
  description = "Name of the S3 bucket for banking app storage"
  type        = string
  default     = "banking-app-bucket"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table for bank accounts"
  type        = string
  default     = "banking-accounts"
}

variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}