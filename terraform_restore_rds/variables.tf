variable "region" {
  default = "cn-north-1"
}
variable "copy_tags_to_snapshot" {}
variable "db_subnet_group_name" {}
variable "snapshot_identifier" {}
variable "identifier" {}
variable "instance_class" {}
variable "port" {}
variable "publicly_accessible" {}
variable "vpc_security_group_ids" { type = list }
