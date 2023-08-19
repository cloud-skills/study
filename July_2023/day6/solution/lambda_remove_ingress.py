import json
import boto3

def lambda_handler(event, context):
    # Parameters
    ssh_port = 2222
    sg_id = 'sg-yourid'
    region_name = 'ap-northeast-2'
    
    # Delete IPs
    for record in event['Records']:
        ec2 = boto3.client('ec2', region_name = region_name)
        response = ec2.revoke_security_group_ingress(
            CidrIp = record['body'],
            FromPort = ssh_port,
            ToPort = ssh_port,
            GroupId = sg_id,
            IpProtocol='tcp'
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('done')
    }
