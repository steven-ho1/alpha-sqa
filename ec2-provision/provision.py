import logging

import boto3
import constants

ec2 = boto3.resource(
    "ec2",
    aws_access_key_id=constants.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=constants.AWS_SECRET_ACCESS_KEY,
    region_name=constants.REGION,
)


def validate_credentials():
    try:
        # https://stackoverflow.com/questions/53548737/verify-aws-credentials-with-boto3
        logging.info("⚙️  Validating credentials...")
        sts = boto3.client(
            "sts",
            aws_access_key_id=constants.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=constants.AWS_SECRET_ACCESS_KEY,
        )
        sts.get_caller_identity()
        logging.info("Credentials validated")
    except Exception:
        raise RuntimeError(
            "Error: Failed to authenticate with AWS. Are your credentials from .env valid?"
        )


def ensure_security_group():
    vpcs = list(ec2.vpcs.all())
    vpc = vpcs[0]
    try:
        sg = list(
            vpc.security_groups.filter(GroupNames=[constants.SECURITY_GROUP_NAME])
        )[0]
        return sg.group_id
    except Exception:
        sg = ec2.create_security_group(
            GroupName=constants.SECURITY_GROUP_NAME,
            Description="Security group",
            VpcId=vpc.id,
        )
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/authorize_ingress.html#
        sg.authorize_ingress(
            IpPermissions=[
                {
                    "IpProtocol": "tcp",
                    "FromPort": constants.SSH_PORT,
                    "ToPort": constants.SSH_PORT,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                },
            ]
        )
        logging.info(f"Created security group: {sg.group_id}")
        return sg.group_id


def get_or_provision_instance(name, user_data, instance_type):
    logging.info(f"⚙️  Provisioning {name} EC2 instance...")

    existing_instance = find_running_instance(name)
    if existing_instance:
        logging.info(
            f"Found existing instance for {name}: ({existing_instance.id}, {existing_instance.public_ip_address})"
        )
        return existing_instance
    return provision_ec2_instance(name, user_data, instance_type)


def provision_ec2_instance(name, user_data, instance_type):
    params = dict(
        ImageId=constants.UBUNTU_AMI,
        MinCount=1,
        MaxCount=1,
        KeyName=constants.AWS_KEY_PAIR_NAME,
        InstanceType=instance_type.value,
        SecurityGroupIds=[ensure_security_group()],
        TagSpecifications=[
            {"ResourceType": "instance", "Tags": [{"Key": "Name", "Value": name}]}
        ],
        UserData=user_data,
    )
    instance = ec2.create_instances(**params)[0]
    instance.wait_until_running()
    instance.reload()
    logging.info(f"{name} instance created")

    logging.info(
        f"✅ {name} provisioned (ID: {instance.id}, IP: {instance.public_ip_address})"
    )
    logging.warning("The instance will shutdown in 20 minutes for resource efficiency.")
    return instance


def find_running_instance(name):
    instances = list(
        ec2.instances.filter(
            Filters=[
                {"Name": "tag:Name", "Values": [name]},
                {"Name": "instance-state-name", "Values": ["running"]},
            ]
        )
    )

    return instances[0] if instances else None
