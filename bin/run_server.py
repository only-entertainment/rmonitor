import threading

from rmonitor.server.server import Server
from rmonitor.settings.settings import logger


# Globals
thread_server = None


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
        thread_server.start()

    except (KeyboardInterrupt, SystemExit):
        pass
