import argparse
from manage_ec2 import create_ec2_instance

parser = argparse.ArgumentParser()
parser.add_argument("set", help="manage instances", choices=["create", "manage", "list"])
parser.add_argument("--image", help="image of the instance", choices=["ubuntu", "amazon linux"])
parser.add_argument("--type", help="type of instance", choices=["t3.nano", "t4.nano"])
parser.add_argument("--action", help="action for managing", choices=['start', 'stop'])
args = parser.parse_args()

if args.set == 'create':
    if args.image and args.type:
        print(f"creating an ec2 instance, instance type is {args.image}, image is {args.type}")
        if args.image == 'ubuntu':
            image_id = 'ami-0e86e20dae9224db8'
        else:
            image_id = 'ami-0e86e20dae9224db8'

        instance_type = args.type

        create_ec2_instance(image_id, instance_type)
    else:
        print(f"instance type/image is missing.")

elif args.set == 'manage':
    if args.action is None:
        print(f"action is missing")
    else:
        print(f"managing instance with {args.action}")

elif args.set == 'list':
    print(f"listing the instances")
