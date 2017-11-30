from telnetlib import Telnet
from time import sleep

import sys

from rmonitor.client.message_factory import MessageFactory
from rmonitor.settings.settings import *


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
                    logger.info(str(m))

                    # Do something with message
                    # TODO: ???

        except KeyboardInterrupt:
            pass
        except EOFError:
            logger.error("Connection lost!")


if __name__ == '__main__':
    Client.connect()
