from rmonitor.client.message_factory import MessageFactory
from rmonitor.common.helpers import snake_case
from rmonitor.common.messages import *
from rmonitor.settings.settings import logger



class MessageHandler(object):

    @staticmethod
    def handle(db, msg):

        # Convert class name to method name
        method_name = snake_case(
            str(type(msg).__name__).replace("Message", "")
        )

        method = getattr(MessageHandler, "do_%s" % method_name)

        # Invoke the method, handle the message with args
        method(db, msg)

    @staticmethod
    def do_competitor_information(db, msg):
        print("WAT")
        print(db)

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
