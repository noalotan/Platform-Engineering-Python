import boto3
import json
s3_client = boto3.client('s3', region_name='us-east-1')



#create es3
def create_s3(ACL_conf, bucket_name):
    s3_client.create_bucket(Bucket=bucket_name,ACL=ACL_conf)
    s3_client.put_bucket_tagging(
        Bucket=bucket_name, 
        Tagging=
        {'TagSet': [{'Key': 'Platform','Value': 'True-Noa'},]})


#set s3 public
def set_public_s3(bucket_name):
    s3_client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"}]}))

    s3_client.put_public_access_block(Bucket=bucket_name,PublicAccessBlockConfiguration={
    'BlockPublicAcls': False,
    'IgnorePublicAcls': False,
    'BlockPublicPolicy': False,
    'RestrictPublicBuckets': False})

    print("the bucket allows public")
    
#upload file
def upload_s3(bucket_name, path_to_file, key_name):
    s3_client.upload_file(bucket_name, path_to_file, key_name, ExtraArgs={'ACL':'public-read'})

#list s3