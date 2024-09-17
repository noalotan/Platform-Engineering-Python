import boto3
import time

route53_client = boto3.client('route53')

#create route53

def create_public_route53(route53_name):
    response = route53_client.create_hosted_zone(
        Name=route53_name,
        CallerReference= str(time.time()),
        HostedZoneConfig={
            'Comment': 'Created By Noa-cli',
            'PrivateZone': False
        },
    )
    resource_name = response['HostedZone']['Name']
    resource_id = response['HostedZone']['Id']
    add_tag_route53(resource_id)
    print(f"Public hosted zone {resource_name}, {resource_id} was created")


def create_private_route53(route53_name):
    response = route53_client.create_hosted_zone(
        Name=route53_name,
        CallerReference= str(time.time()),
        VPC={
            'VPCRegion': 'us-east-1',
            'VPCId': 'vpc-0e10a3db09e90dd48'
        },
        HostedZoneConfig={
            'Comment': 'Created By Noa-cli',
            'PrivateZone': True
        },
    )
    resource_name = response['HostedZone']['Name']
    full_resource_id = response['HostedZone']['Id']
    resource_id = full_resource_id.split('/')[-1]
    add_tag_route53(resource_id)
    print(f"Private hosted zone {resource_name}, {resource_id} was created")

 # add tag
def add_tag_route53(resource_id):
    response = route53_client.change_tags_for_resource(
        ResourceType='hostedzone',
        ResourceId=resource_id,
        AddTags=[
            {
                'Key': 'Platform',
                'Value': 'True-Noa'
            },
        ]
    )

# list route53 zones
def list_hosted_zones():
    response = route53_client.list_hosted_zones()
    all_hosted_zones = response['HostedZones']
    return all_hosted_zones

# check hosted zones tags
def get_hosted_zone_tags(hostedzone_id):
    tags_response = route53_client.list_tags_for_resource(
        ResourceType='hostedzone',
        ResourceId=hostedzone_id
    )
    tags_set = tags_response.get('ResourceTagSet', {})
    return tags_set.get('Tags', [])

#filter hosted zones by tags
def filter_hosted_zones(all_hosted_zones):
    my_hostedzones = []
    for zone in all_hosted_zones:
        hosted_zone_id = zone['Id'].split('/')[-1]
        tags = get_hosted_zone_tags(hosted_zone_id)
        tags_result = {tag['Key']: tag['Value'] for tag in tags}

        if tags_result.get('Platform') == 'True-Noa':
            my_hostedzones.append({
                    'Id': hosted_zone_id,
                    'Name': zone['Name']})
    return my_hostedzones

def cli_created_hosted_zones():
    all_hosted_zones = list_hosted_zones()
    filtered_zones = filter_hosted_zones(all_hosted_zones)
    return filtered_zones

# CREATE, DELETE, UPSET records
def route53_manage(hostedzone_id, comment, action, record_name, record_type, ip_address):
    response = route53_client.change_resource_record_sets(
        HostedZoneId=hostedzone_id,
        ChangeBatch={
            'Comment': comment,
            'Changes': [
                {
                    'Action': action,
                    'ResourceRecordSet': {
                        'Name': record_name,
                        'Type': record_type,
                        'TTL': 300,
                        'ResourceRecords': [
                            {'Value': ip_address}]}}]})
    return(response)