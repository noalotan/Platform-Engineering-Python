import boto3

def create_ec2_instance(image_id, instance_type):
    ec2_client = boto3.resource('ec2')
    instance = ec2_client.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName='noa-python-project',
        SecurityGroupIds=['sg-050e5bfa643d29369'],
        SubnetId='subnet-0ef884acbd166c8c4',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {'ResourceType': 'instance',
             'Tags': [
                 {'Key': 'Platform', 'Value': 'True-Noa'}
             ]
             }
        ]
    )
    print(f"\nInitiating instance now, please wait...")
    instance[0].wait_until_running()
    print(f"instance {instance[0].instance_id} was created successfully!\n")





def list_instances():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances(
        Filters=[{'Name': 'tag:Platform',
                   'Values': ['True-Noa']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'])


def stop_instances(instance_id):
    ec2_client = boto3.client('ec2')
    instance_ids = [instance_id]
    instances = ec2_client.stop_instances(InstanceIds=instance_ids)
    print(f"stopping the instance {instance_id}")


def start_instances(instance_id):
    ec2_client = boto3.client('ec2')
    instance_ids = [instance_id]
    instances = ec2_client.start_instances(InstanceIds=instance_ids)
    print(f"starting the instance {instance_id}")
