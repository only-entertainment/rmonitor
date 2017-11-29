import threading

from rmonitor.client.client import Client
from rmonitor.server.server import Server

from rmonitor.settings.settings import logger


# Globals
thread_server = None
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


def run_server():
    """
    Run and send messages as a server
    """

    try:
        logger.info("Running and sending messages as a server...")

        Server.serve()
    except KeyboardInterrupt:
        thread_server.join()


if __name__ == '__main__':
    #
    # Main Driver
    #

    try:
        thread_server = threading.Thread(name='Server', target=run_server, daemon=False)
        #thread_client = threading.Thread(name='Client', target=run_client, daemon=False)

        thread_server.start()
        #thread_client.start()

    except (KeyboardInterrupt, SystemExit):
        pass
