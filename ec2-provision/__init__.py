import logging

# Voir la documentation: https://docs.python.org/3/howto/logging.html

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s][%(levelname)s] %(message)s"
)
