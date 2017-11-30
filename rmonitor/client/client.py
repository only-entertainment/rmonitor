from telnetlib import Telnet
from time import sleep

from rmonitor.client.db import DB
from rmonitor.client.message_factory import MessageFactory
from rmonitor.client.message_handler import MessageHandler
from rmonitor.settings.settings import *


# Initialize the DB
db = DB()


class Client(object):

    @staticmethod
    def connect():
        # TODO: Break this into two methods: connect and listen
        tn = None

        try:
            # Block until we make a connection
            while True:
                try:
                    logger.info('Trying to connect...')

                    # Very persistent way to retry
                    tn = Telnet(HOST, PORT, timeout=5)
                    break

                except Exception:
                    # Wait, then keep trying...
                    sleep(1.0)

            logger.info('Connected.')

            while True:
                # Read line by line...
                msg = tn.read_until(b'\n')
                logger.debug('Raw: %s' % msg)

                # Get message for string
                m = MessageFactory.get_message(msg)

                if m:
                    # We got something usable
                    logger.info(str(m))

                    # Do something with message
                    MessageHandler.handle(db, m)

        except KeyboardInterrupt:
            pass
        except EOFError:
            logger.error("Connection lost!")


if __name__ == '__main__':
    Client.connect()
