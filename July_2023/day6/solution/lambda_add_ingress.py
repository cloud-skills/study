import json
import boto3
    
def lambda_handler(event, context):
    # Parameters
    sg_id = 'sg-yourid'
    ssh_port = 2222
    region_name = 'ap-northeast-2'
    requested_ip_addr = event['queryStringParameters']['ip'] + '/32'
    response_code = 0
    response_body = 'PLACEHOLDER'
    sqs_url = 'https://your sqs url'
    
    try:
        # Initialize boto
        ec2 = boto3.resource('ec2', region_name=region_name)
        security_group = ec2.SecurityGroup(sg_id)
        
        sqs = boto3.client('sqs', region_name=region_name)

    
        # Allowlist
        response = security_group.authorize_ingress(
            IpPermissions=[
                {
                    'FromPort': ssh_port,
                    'ToPort': ssh_port,
                    'IpProtocol': 'tcp',
                    'IpRanges': [
                        {
                            'CidrIp': requested_ip_addr,
                            'Description': 'added by allowlist API'
                        },
                    ]
                },
            ]
        )
        
        # Enqueue
        sqs_res = sqs.send_message(
            QueueUrl=sqs_url,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': 'Deleting IP from SG'
                },
                'Author': {
                    'DataType': 'String',
                    'StringValue': 'Lambda'
                },
            },
            MessageBody=(
                requested_ip_addr
            )
        )
        
        # Response status
        response_code = 200
        response_body = 'succesfully added'
    except Exception as e:
        print(e)
        response_code = 500
        response_body = 'execution failed'
    finally:
        return {
            'statusCode': response_code,
            'body': json.dumps(response_body)
        }

