import constants
from logger import logger
from provision import ec2


def cleanup_resources():
    logger.info("⚙️  Running EC2 cleanup...")

    # Delete EC2 instance
    filters = [
        {"Name": "tag:Name", "Values": [constants.INSTANCE_NAME]},
        {"Name": "instance-state-name", "Values": ["running", "pending"]},
    ]
    instances = list(ec2.instances.filter(Filters=filters))

    if not instances:
        logger.info("No matching instances found.")
    else:
        instance_ids = [i.id for i in instances]
        logger.info(f"Terminating instances...: {instance_ids}")
        ec2.instances.filter(InstanceIds=instance_ids).terminate()

        for instance in instances:
            instance.wait_until_terminated()

    # Delete created security group
    try:
        logger.info(
            f"Attempting to delete security group '{constants.SECURITY_GROUP_NAME}'..."
        )
        sgs = list(
            ec2.security_groups.filter(GroupNames=[constants.SECURITY_GROUP_NAME])
        )
        if sgs:
            sg = sgs[0]
            sg.delete()
            logger.info(f"Security group '{constants.SECURITY_GROUP_NAME}' deleted.")
    except Exception:
        logger.exception("Error deleting security group")


if __name__ == "__main__":
    cleanup_resources()
