from telnetlib import Telnet
from time import sleep

from race_monitor.client.messages import MessageFactory
from race_monitor.settings.settings import *


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

                # Wait
                sleep(SLEEP)

        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    Client.connect()
