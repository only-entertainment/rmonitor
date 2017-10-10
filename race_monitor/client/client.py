from telnetlib import Telnet
from time import sleep

from race_monitor.client.messages import MessageFactory
from race_monitor.settings.settings import *


try:
    tn = Telnet(HOST, PORT, timeout=5)

    while True:
        # Read line by line...
        msg = tn.read_until(b'\n')

        # Make it a string
        msg = msg.strip(b"\r\n").decode()
        logger.info(msg)

        # Get message for string
        m = MessageFactory.get_message(msg)
        logger.info(m)

        # Wait
        sleep(SLEEP)

except KeyboardInterrupt:
    pass
