import threading

from rmonitor.client.client import Client
from rmonitor.settings.settings import logger


# Globals
thread_client = None


def run_client():
    """
    Run and receive messages as a client
    """

    try:
        logger.info("Running and monitoring as a client...")

        Client.connect()
    except KeyboardInterrupt:
        thread_client.join()


if __name__ == '__main__':
    #
    # Main Driver
    #

    try:
        thread_client = threading.Thread(name='Client', target=run_client, daemon=False)
        thread_client.start()

    except (KeyboardInterrupt, SystemExit):
        pass
