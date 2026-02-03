import logging

# https://docs.python.org/3/howto/logging.html

logger = logging.getLogger("project_logger")

logger.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
