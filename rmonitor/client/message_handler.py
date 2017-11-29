from rmonitor.client.message_factory import MessageFactory
from rmonitor.common.messages import *
from rmonitor.settings.settings import logger

import re


def lower_case(s):
    """
    Convert string into lower case

    Source: Source: https://github.com/okunishinishi/python-stringcase/blob/master/stringcase.py
    """

    return str(s).lower()


def snake_case(s):
    """
    Convert string into snake case

    Source: https://github.com/okunishinishi/python-stringcase/blob/master/stringcase.py
    """

    ss = re.sub(r"[\-\.\s]", '_', str(s))

    if not ss:
        return ss

    return lower_case(
        ss[0]) + re.sub(
            r"[A-Z]", lambda matched: '_' + lower_case(matched.group(0)), ss[1:]
        )


# TODO: Move this into db.py

# Ghetto data store for bootstrapping this
DB = dict()
DB['race'] = {}
DB['classes'] = set()
DB['drivers'] = set()


class MessageHandler(object):

    @staticmethod
    def handle(msg):

        # Convert class name to method name
        method_name = snake_case(
            str(type(msg).__name__).replace("Message", "")
        )

        method = getattr(MessageHandler, "do_%s" % method_name)

        # Invoke the method, handle the message
        method(msg)

    @staticmethod
    def do_competitor_information(msg):
        print("WAT")
        print(DB)

    # TODO: THIS STUFF - convert to methods
    #CompetitorInformationMessage
        #RunInformationMessage
        #ClassInformationMessage
        #CompInformationMessage
        #SettingInformationMessage
        #HeartbeatMessage
        #RaceInformationMessage
        #PracticeQualifyingInformationMessage
        #InitRecordMessage
        #PassingInformationMessage

        #LapInformationMessage
        #LapInformationMessage



if __name__ == '__main__':

    MessageHandler.handle(
        MessageFactory.get_message(
            b'$A,"1234BE","12X",52474,"John","Johnson","USA",5'
        )
    )
