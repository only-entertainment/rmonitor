from datetime import datetime

from rmonitor.common.messages import MESSAGE_TYPES
from rmonitor.settings.settings import logger


class MessageFactory(object):

    @staticmethod
    def get_message(msg):
        # Little cleanup
        msg = msg.strip(b"\r\n").decode()
        msg = msg.replace('\"', '')

        # Add a timestamp to each message
        msg += ",%s" % datetime.now()

        # Comma separated string
        fields = msg.split(",")

        # Split off the type
        msg_type = fields[0]

        # Split off the data fields
        fields = fields[1:]

        logger.debug(msg_type)
        logger.debug(fields)

        # Find the corresponding message class
        clazz = MESSAGE_TYPES.get(msg_type)

        if not clazz:
            logger.debug("Missing message type: %s", msg_type)
            return None

        # Return class instance with data
        return clazz(fields)
