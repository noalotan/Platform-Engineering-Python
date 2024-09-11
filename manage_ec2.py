# this code creates ec2 instances
import boto3
all_ec2 = {}


def create_ec2_instance(image_id, instance_type):
    ec2_client = boto3.resource('ec2')
    instance = ec2_client.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName='noa-python-project.pem',
        SecurityGroupIds=['sg-050e5bfa643d29369'],
        SubnetId='subnet-0ef884acbd166c8c4',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {'ResourceType': 'instance',
             'Tags': [
                 {'Key': 'Platform Engineering', 'Value': 'True'}
             ]
             }
        ]
    )
    print(f"\nInitiating instance now, please wait...")
    instance[0].wait_until_running()
    print(f"instance {instance[0].instance_id} was created successfully!\n")
    all_ec2[instance[0].instance_id] = instance[0]
    return all_ec2


def list_instances():
    for instance in all_ec2:
        print(instance)


def stop_ec2_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance {instance_id}.")
    print(response)
