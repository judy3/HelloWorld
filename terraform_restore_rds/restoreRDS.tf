provider "aws" {
  region     = var.region
}
resource "aws_db_instance" "db_uat" {
  instance_class       = var.instance_class
  identifier           = var.identifier
  db_subnet_group_name = var.db_subnet_group_name
  snapshot_identifier  = var.snapshot_identifier
  copy_tags_to_snapshot = var.copy_tags_to_snapshot
  port = var.port
  publicly_accessible = var.publicly_accessible
  vpc_security_group_ids = var.vpc_security_group_ids
  apply_immediately = "true"
  allocated_storage     = 500
  max_allocated_storage = 1000
  deletion_protection = "true"
}
