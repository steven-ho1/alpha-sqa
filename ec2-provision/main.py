from constants import (
    INSTANCE_NAME,
    INSTANCE_TYPE,
)
from logger import logger
from provision import (
    provision_ec2_instance,
    validate_credentials,
)


def main():
    logger.info("🦊🍃 Starting EC2 provisioning... (Inspired by LOG8415E project)")

    validate_credentials()

    provision_ec2_instance(
        INSTANCE_NAME,
        "user_data.sh",
        instance_type=INSTANCE_TYPE,
    )


if __name__ == "__main__":
    main()
