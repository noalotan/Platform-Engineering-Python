import argparse
from manage_ec2 import create_ec2, list_ec2, ec2_manage
from manage_s3 import create_s3, set_public_s3, upload_s3

# parser = argparse.ArgumentParser()
# parser.add_argument("set", help="create instance", choices=["create", "manage", "list"])
# parser.add_argument("--image", help="image of the instance", choices=["ubuntu", "amazon linux"])
# parser.add_argument("--type", help="type of instance", choices=["t3.nano", "t4.nano"])
# parser.add_argument("--action", help="action for managing", choices=['start', 'stop'])
# parser.add_argument("--id", help="instance id")
# parser.add_argument("--name", help="name of resource")
# args = parser.parse_args()

parser = argparse.ArgumentParser(description="AWS CLI Tool")
subparsers = parser.add_subparsers(dest="resource")

ec2_parser = subparsers.add_parser('ec2')
ec2_subparsers = ec2_parser.add_subparsers(dest='action')

ec2_create_parser = ec2_subparsers.add_parser('create')
ec2_create_parser.add_argument('--image', required=True, help='Image name', choices=["ubuntu", "amazon linux"])
ec2_create_parser.add_argument('--type', choices=["t3.nano", "t4.nano"], help='Instance Type', required=True)
ec2_create_parser.add_argument('--name', required=True, help='Name for the instance')

ec2_manage_parser = ec2_subparsers.add_parser('manage')
ec2_manage_parser.add_argument('--proccess', required=True, help='proccess you want to perform', choices=["start", "stop"])
ec2_manage_parser.add_argument('--id', required=True, help='id of the instance you want to manage')

ec2_list_parser = ec2_subparsers.add_parser('list')

args = parser.parse_args()

# ec2

if args.resource == 'ec2':
    if args.action == 'create':
        create_ec2(args.image, args.type, args.name)
    elif args.action == 'manage':
        ec2_manage(args.id, args.proccess)
    elif args.action == 'list':
        list_ec2()

# # ec2
# if args.set == 'create':
#     if args.image and args.type:
#         print(f"creating an ec2 instance, instance type is {args.image}, image is {args.type}")
#         if args.image == 'ubuntu':
#             image_id = 'ami-0e86e20dae9224db8'
#         else: 
#             image_id = 'ami-0e86e20dae9224db8'
#         instance_type = args.type
#         create_ec2(image_id, instance_type)
#     else:
#         print(f"instance type/image is missing.")

# elif args.set == 'manage':
#     if args.action and args.id:
#         if args.action == 'start':
#             manage_ec2(args.id, 'start')
#         elif args.action == 'stop':
#             manage_ec2(args.id, 'stop')
#     else:
#         print(f"action or id is missing")

# elif args.set == 'list':
#     list_ec2()


#s3
#parser.add_argument("--id", help="instance id")


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

# #create s3
# if args.resource == 's3':
#     if args.action == 'create':
#         create_s3('private', args.name)
#     elif args.action == 'upload':
#         upload_s3(args.file, args.bucket, args.key_name)
#     elif args.action == 'list':