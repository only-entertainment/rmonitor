from rmonitor.client.client import Client
from rmonitor.settings.settings import logger


def run():
    """
    Run and receive messages
    """

    try:
        Client.connect()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    #
    # Main Driver
    #

    logger.info("Running and monitoring...")
    run()
