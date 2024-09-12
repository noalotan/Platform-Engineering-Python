import argparse
from manage_ec2 import create_ec2, list_ec2, ec2_manage
from manage_s3 import create_s3, set_public_s3, upload_s3, list_s3

#ec2 parsers
parser = argparse.ArgumentParser(description="AWS CLI Tool")
subparsers = parser.add_subparsers(dest="resource")

ec2_parser = subparsers.add_parser('ec2')
ec2_subparsers = ec2_parser.add_subparsers(dest='action')

ec2_create_parser = ec2_subparsers.add_parser('create')
ec2_create_parser.add_argument('--image', required=True, help='Image name', choices=["ubuntu", "amazon linux"])
ec2_create_parser.add_argument('--type', choices=["t3.nano", "t4.nano"], help='Instance Type', required=True)
ec2_create_parser.add_argument('--name', required=True, help='Name for the instance')

ec2_manage_parser = ec2_subparsers.add_parser('manage')
ec2_manage_parser.add_argument('--process', required=True, help='proccess you want to perform', choices=["start", "stop"])
ec2_manage_parser.add_argument('--id', required=True, help='id of the instance you want to manage')

ec2_list_parser = ec2_subparsers.add_parser('list')

args = parser.parse_args()

# ec2 functions

if args.resource == 'ec2':
    if args.action == 'create':
        create_ec2(args.image, args.type, args.name)
    elif args.action == 'manage':
        ec2_manage(args.id, args.process)
    elif args.action == 'list':
        list_ec2()


#s3 parsers

s3_parser = subparsers.add_parser('s3')
s3_subparsers = s3_parser.add_subparsers(dest='action')

s3_create_parser = s3_subparsers.add_parser('create')
s3_create_parser.add_argument('--name', required=True, help='Bucket name')
s3_create_parser.add_argument('--acl', choices=['public-read', 'private'], default='private', help='Configure ACL for thr bucket')

s3_upload_parser = s3_subparsers.add_parser('upload')
s3_upload_parser.add_argument('--bucket', required=True, help='Bucket name')
s3_upload_parser.add_argument('--file', required=True, help='File path to upload')
s3_upload_parser.add_argument('--key_name', required=True, help='New name for the file')

s3_list_parser = s3_subparsers.add_parser('list')

args = parser.parse_args()

#s3 functions 

if args.resource == 's3':
    if args.action == 'create':
        create_s3('private', args.name)
    elif args.action == 'upload':
        upload_s3(args.file, args.bucket, args.key_name)
    elif args.action == 'list':
        list_s3()