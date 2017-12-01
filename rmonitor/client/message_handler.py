from rmonitor.client.db import DB
from rmonitor.client.message_factory import MessageFactory
from rmonitor.common.helpers import snake_case
from rmonitor.settings.settings import logger


class MessageHandler(object):

    @staticmethod
    def handle(db, msg):
        """
        Take the data in the messages and process them
        into something useful and then store it.

        :param db:
        :param msg:
        :return: None
        """

        # Convert class name to method name
        method_name = snake_case(
            str(type(msg).__name__).replace("Message", "")
        )

        try:
            method = getattr(MessageHandler, "do_%s" % method_name)
        except Exception:
            # For messages we don't have yet or can't handle
            method = getattr(MessageHandler, "do_default")

        # Invoke the method, handle the message with args
        method(db, msg)

    @staticmethod
    def do_default(db, msg):

        print('Default!')
        print(msg)

    # @staticmethod
    # def do_competitor_information(db, msg):
    #     print('Competitor Information!')
    #     print(db)
    #     print(msg)
    #
    # @staticmethod
    # def do_run_information(db, msg):
    #     print('Class Information!')
    #     print(db)
    #     print(msg)
    #
    # @staticmethod
    # def do_comp_information(db, msg):
    #     print('Comp Information!')
    #     print(db)
    #     print(msg)
    #

    @staticmethod
    def do_setting_information(db, msg):
        description = msg.description.lower()
        if 'name' in description:
            key = 'name'
        elif 'length' in description:
            key = 'length'
        else:
            return

        db.update_track({
            'description': key,
            'value': msg.value
        })

    @staticmethod
    def do_heartbeat(db, msg):
        db.update_race({
            'laps_to_go': msg.laps_to_go,
            'time_to_go': msg.time_to_go,
            'time_of_day': msg.time_of_day,
            'race_time': msg.race_time,
            'flag_status': msg.flag_status
        })

    #@staticmethod
    # def do_race_information(db, msg):
    #     print('Race Information!')
    #     print(db)
    #     print(msg)
    #
    # @staticmethod
    # def do_practice_qualifying_information(db, msg):
    #     print('Practice Qualifying Information!')
    #     print(db)
    #     print(msg)
    #

    @staticmethod
    def do_init_record(db, msg):
        # DB needs to be cleared
        db.initialize()

    @staticmethod
    def do_class_information(db, msg):
        # Add the class
        db.add_class({
            'unique_number': msg.unique_number,
            'description': msg.description
        })

    # @staticmethod
    # def do_passing_information(db, msg):
    #     print('Passing Information!')
    #     print(db)
    #     print(msg)
    #
    # @staticmethod
    # def do_lap_information(db, msg):
    #     print('Lap Information!')
    #     print(db)
    #     print(msg)


if __name__ == '__main__':

    db = DB()
    for msg in [
        # Init Record
        #b'$I,"16:36:08.000","12 jan 01","1234567890"',

        # Class Record
        #b'$C,1,"Formula 100","1234567890"',
        #b'$C,2,"Formula 200","1234567890"',
        #b'$C,3,"Formula 300","1234567890"',
        #b'$C,4,"Formula 400","1234567890"',
        #b'$C,5,"Formula 500","1234567890"',

        # It should ignore this one, dupe
        #b'$C,5,"Formula 500","1234567890"',

        # Heartbeat
        #b'$F,9999,"00:01:45","13:31:23","00:01:47","Green","1234567890"',
        #b'$F,9999,"00:02:45","13:32:23","00:02:47","Yellow","1234567890"',
        #b'$F,9999,"00:03:45","13:33:23","00:03:47","Black","1234567890"',
        #b'$F,9999,"00:04:45","13:34:23","00:04:47","Green","1234567890"',

        # Settings
        b'$E,"TRACKNAME","Indianapolis Motor Speedway","1234567890"'
        b'$E,"TRACKLENGTH","2.500","1234567890"'

        # Init Record, again
        #b'$I,"16:36:08.000","12 jan 01","1234567890"',

        # Default
        #b'$A,"1234BE","12X",52474,"John","Johnson","USA",5'
    ]:
        MessageHandler.handle(
            db,
            MessageFactory.get_message(msg)
        )
        print(db)
        print('')
        print(db.get_classes())


