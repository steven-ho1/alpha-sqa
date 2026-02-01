from constants import (
    INSTANCE_NAME,
    INSTANCE_TYPE,
)
from logger import logger
from provision import (
    get_or_provision_instance,
    validate_credentials,
)


def main():
    logger.info("🦊🍃 Starting EC2 provisioning...")

    validate_credentials()

    ec2_instance = get_or_provision_instance(
        INSTANCE_NAME,
        "./user_data.sh",
        instance_type=INSTANCE_TYPE,
    )

    # print pour que l'adresse IP soit utilisée en dehors du script
    print(ec2_instance.public_ip_address)


if __name__ == "__main__":
    main()
