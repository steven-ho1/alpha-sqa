import os

from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

AWS_KEY_PAIR_NAME = os.getenv("AWS_KEY_PAIR_NAME")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# https://ca-central-1.console.aws.amazon.com/ec2/home?region=ca-central-1#LaunchInstances:
UBUNTU_AMI = "ami-0938a60d87953e820"
REGION = "ca-central-1"
INSTANCE_NAME = "log8371_instance"
SECURITY_GROUP_NAME = "project-sg"
SSH_PORT = 22
THINGSBOARD_PORT = 8080
INSTANCE_TYPE = "m7i-flex.large"
