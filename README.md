**install jenkins and java**
on amazon linux - https://medium.com/@belek.bagishbekov/how-to-install-and-configure-jenkins-on-amazon-linux-2023-a8d7463a0404

**install python, pip, boto3, aws-cli**

**install git**
sudo yum update -y
sudo yum install git -y
git —-version

# Platform Engineering with Python

Welcome to the **Platform Engineering with Python** repository! This project contains various Python scripts and tools designed to manage and automate infrastructure and platform tasks. The repository includes functionality for working with AWS services like EC2, S3, and Route53.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Usage](#usage)
  - [EC2](#ec2)
  - [S3](#s3)
  - [Route53](#route53)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository provides Python scripts that can be used to interact with AWS services for various platform engineering tasks. The scripts include functionalities to create, manage, and list resources such as EC2 instances, S3 buckets, and Route53 DNS records.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/noalotan/Platform-Engineering-Python.git
   cd Platform-Engineering-Python
Install Dependencies:

Ensure you have Python 3.x installed. Install the required Python packages using pip:

sh
Copy code
pip install -r requirements.txt
Set Up AWS Credentials:

Make sure your AWS credentials are configured. You can set them up using the AWS CLI:

sh
Copy code
aws configure
Usage
The scripts in this repository are designed to be run from the command line. Below are examples of how to use each script.

EC2
Create an EC2 instance:

sh
Copy code
python3 argparse_main.py ec2 create --image <ubuntu|amazon_linux> --type <t3.nano|t4.nano> --name <instance_name>
Manage an EC2 instance:

sh
Copy code
python3 argparse_main.py ec2 manage --id <instance_id> --process <process_name>
List EC2 instances:

sh
Copy code
python3 argparse_main.py ec2 list
S3
Create an S3 bucket:

sh
Copy code
python3 argparse_main.py s3 create --name <bucket_name> --acl <private|public-read>
Upload a file to S3:

sh
Copy code
python3 argparse_main.py s3 upload --file <file_path> --bucket <bucket_name> --key <key_name>
List S3 buckets:

sh
Copy code
python3 argparse_main.py s3 list
Route53
Create a Route53 record:

sh
Copy code
python3 argparse_main.py route53 create --name <record_name> --private <true|false>
List Route53 hosted zones:

sh
Copy code
python3 argparse_main.py route53 list
Manage a Route53 record:

sh
Copy code
python3 argparse_main.py route53 manage --resource-id <resource_id> --comment <comment> --action <action> --name <record_name> --type <record_type> --ip <ip_address>
Project Structure
argparse_main.py: The main script that provides functionality for managing AWS resources.
requirements.txt: Lists the Python packages required for the project.
README.md: This file.
