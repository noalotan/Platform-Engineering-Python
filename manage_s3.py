import boto3
import json
from botocore.exceptions import ClientError

s3_client = boto3.client('s3', region_name='us-east-1')

#create es3
def create_s3(bucket_name, acl):
    s3_client.create_bucket(Bucket=bucket_name)
    s3_client.put_bucket_tagging(
        Bucket=bucket_name, 
        Tagging={'TagSet': [{'Key': 'Platform','Value': 'True-Noa'}]}
        )
    acl_conf(acl, bucket_name)
    print("Bucket created succesfully!")

#configure ACL (ACL_conf)
def acl_conf(acl, bucket_name):
    if acl == 'public-read':
        public_s3 = input("Are you sure you want to make S3 public? (yes/no)")
        if public_s3.lower() in ['no', 'yes']:
            if public_s3.lower() == 'yes':
                set_public_s3(bucket_name)       
        else:
            print("invalid input. Please enter 'yes' or 'no'.")


#set s3 public
def set_public_s3(bucket_name):
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }]
    }
    public_access_block_config = {
    'BlockPublicAcls': False,
    'IgnorePublicAcls': False,
    'BlockPublicPolicy': False,
    'RestrictPublicBuckets': False
    }
    try:
        s3_client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
        s3_client.put_public_access_block(Bucket=bucket_name,PublicAccessBlockConfiguration=public_access_block_config)
        print("The bucket allows public access.")

    except ClientError as e:
        print(f"Error setting public access: {e}")

#upload file
def upload_s3(bucket_name, path_to_file, key_name):
    s3_client.upload_file(bucket_name, path_to_file, key_name)

#list s3
def list_s3():
    tag_key = 'Platform'
    tag_value = 'True-Noa'
    response = s3_client.list_buckets()
    all_s3=response['Buckets']
    my_s3 = []
    for bucket in all_s3:
        bucket_name = bucket['Name']
        try:
            tags_response = s3_client.get_bucket_tagging(Bucket=bucket_name)
            tags = tags_response.get('TagSet', [])

            for tag in tags:
                if tag['Key'] == tag_key and tag['Value'] == tag_value:
                    my_s3.append(bucket_name)
                    break

        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchTagSet':
                continue
    
    print("S3 buckets with the specified tag:", my_s3)