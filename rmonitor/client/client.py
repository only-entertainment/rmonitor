from telnetlib import Telnet
from time import sleep

from rmonitor.client.message_factory import MessageFactory
from rmonitor.settings.settings import *


class Client(object):

    @staticmethod
    def connect():
        # Blocking!
        try:
            tn = Telnet(HOST, PORT, timeout=TIMEOUT)

            while True:
                # Read line by line...
                msg = tn.read_until(b'\n')
                logger.debug('Raw: %s' % msg)

                # Get message for string
                m = MessageFactory.get_message(msg)
                logger.info('Message: %s' % str(m))

                # Do something with message
                # TODO: ???

                # Wait
                sleep(SLEEP)

        except KeyboardInterrupt:
            pass
        except EOFError:
            logger.error("Connection lost!")


if __name__ == '__main__':
    Client.connect()
