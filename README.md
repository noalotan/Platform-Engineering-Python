# Platform Engineering with Python

Welcome to the **Platform Engineering with Python** repository! This project contains various Python scripts and tools designed to manage and automate infrastructure and platform tasks. The repository includes functionality for working with AWS services like EC2, S3, and Route53.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Installing Jenkins, Java, and Git](#installing-jenkins-java-and-git)
  - [Installing Python, pip, boto3, and AWS CLI](#installing-python-pip-boto3-and-aws-cli)
- [Usage](#usage)
  - [EC2](#ec2)
  - [S3](#s3)
  - [Route53](#route53)

## Overview

This repository provides Python scripts that can be used to interact with AWS services for various platform engineering tasks. The scripts include functionalities to create, manage, and list resources such as EC2 instances, S3 buckets, and Route53 DNS records.

## Getting Started

Follow these steps to set up the environment and start using the scripts.

### Installing Jenkins, Java, and Git

To install Jenkins and Java on Amazon Linux, follow the guide provided [here](https://medium.com/@belek.bagishbekov/how-to-install-and-configure-jenkins-on-amazon-linux-2023-a8d7463a0404).

To install Git, run:

```sh
sudo yum update -y
sudo yum install git -y
git --version
```

### Installing Python, pip, boto3, and AWS CLI
Install Python:

```sh
sudo yum install python3 -y
```

Install pip:

```sh
sudo yum install python3-pip -y
```

Install boto3 and AWS CLI:

```sh
pip install boto3 awscli
```

## Usage
The scripts in this repository are designed to be run from the command line. Below are examples of how to use each script.

### EC2

Create an EC2 instance:
```sh
python3 argparse_main.py ec2 create --image <ubuntu|amazon_linux> --type <t3.nano|t4.nano> --name <instance_name>
```

Manage an EC2 instance:
```sh
python3 argparse_main.py ec2 manage --id <instance_id> --process <process_name>
```

List EC2 instances:
```sh
python3 argparse_main.py ec2 list
```

### S3

Create an S3 bucket:
```sh
python3 argparse_main.py s3 create --name <bucket_name> --acl <private|public-read>
```

Upload a file to S3:
```sh
python3 argparse_main.py s3 upload --file <file_path> --bucket <bucket_name> --key <key_name>
```

List S3 buckets:
```sh
python3 argparse_main.py s3 list
```

### Route53

Create a Route53 record:
```sh
python3 argparse_main.py route53 create --name <record_name> --private <True|False>
```

List Route53 hosted zones:
```sh
python3 argparse_main.py route53 list
```

Manage a Route53 record:
```sh
python3 argparse_main.py route53 manage --resource-id <resource_id> --comment <comment> --action <action> --name <record_name> --type <record_type> --ip <ip_address>
```
