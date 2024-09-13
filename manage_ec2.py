import boto3
ec2_client = boto3.client('ec2')

# configure image
def conf_image_ec2(instance_image):
    if instance_image == 'ubuntu':
        image_id = 'ami-0e86e20dae9224db8'
    else: 
        image_id = 'ami-0e86e20dae9224db8'
    return image_id

#create ec2 
def create_ec2(instance_image, instance_type, instance_name):
    image_id = conf_image_ec2(instance_image)
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
                 {'Key': 'Name', 'Value': instance_name},
                 {'Key': 'Platform', 'Value': 'True-Noa'}]}])
    print(f"\nInitiating instance now, please wait...")
    instance[0].wait_until_running()
    print(f"instance {instance[0].instance_id} was created successfully!\n")

#list ec2
def list_ec2():
    print(f"listing the instances: \n")
    instances = ec2_client.describe_instances(
        Filters=[{'Name': 'tag:Platform', 'Values': ['True-Noa']}])
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(instance['InstanceId'])

#start/stop ec2
def ec2_manage(instance_id, action):
    if action == 'start':
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"starting the instance {instance_id}")
    elif action == 'stop':
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"stopping the instance {instance_id}")