import argparse
from manage_ec2 import create_ec2_instance, list_instances, start_instances, stop_instances

parser = argparse.ArgumentParser()
parser.add_argument("set", help="manage instances", choices=["create", "manage", "list"])
parser.add_argument("--image", help="image of the instance", choices=["ubuntu", "amazon linux"])
parser.add_argument("--type", help="type of instance", choices=["t3.nano", "t4.nano"])
parser.add_argument("--action", help="action for managing", choices=['start', 'stop'])
parser.add_argument("--id", help="instance id")
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
    if args.action and args.id:
        if args.action == 'start':
            start_instances(args.id)
        elif args.action == 'stop':
            stop_instances(args.id)
    else:
        print(f"action or id is missing")

elif args.set == 'list':
    print(f"listing the instances")
    list_instances()
