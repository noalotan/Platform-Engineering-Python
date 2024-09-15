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
    print(f"Public hosted zone {response['HostedZone']['Name']} was created")


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
    print(f"Private hosted zone {response['HostedZone']['Name']} was created")

#list route53

def list_hosted_zones():
    response = route53_client.list_hosted_zones()
    print(response)

# dns records
def list_records():
    response = client.list_resource_record_sets(
        HostedZoneId='string',
        StartRecordName='string',
        StartRecordType='SOA'|'A'|'TXT'|'NS'|'CNAME'|'MX'|'NAPTR'|'PTR'|'SRV'|'SPF'|'AAAA'|'CAA',
        StartRecordIdentifier='string',
        MaxItems='string'
    )   




def create_dns_record(dns_record_name, ):
    response = route53_client.change_resource_record_sets(
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'CREATE',
                    'ResourceRecordSet': {
                        'Name': dns_record_name,
                        'ResourceRecords': [
                            {
                                'Value': '3.128.188.18',
                            },
                        ],
                        'TTL': 60,
                        'Type': 'A',
                    },
                },
            ],
            'Comment': 'Web Server',
        },
        HostedZoneId='Z00594533FY3S68ROG6V2',
    )
    print(response)
