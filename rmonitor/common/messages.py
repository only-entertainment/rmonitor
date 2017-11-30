from datetime import datetime

from rmonitor.common.helpers import Duration


class HeartbeatMessage(object):

    def __init__(self, fields):
        self.type = '$F'
        self.timestamp = datetime.now()

        # Number of laps to go
        # (0 - 99999)
        self.laps_to_go = fields[0]

        # Time until the session ends
        # ("HH:MM:SS")
        self.time_to_go = Duration(fields[1])

        # The current time
        # ("HH:MM:SS")
        self.time_of_day = Duration(fields[2])

        # The time from the first green flag ("HH:MM:SS")
        self.race_time = Duration(fields[3])

        # The status field is 6 characters long with trailing spaces
        # (GREEN, etc.)
        self.flag_status = fields[4]

    def __repr__(self):
        return "Heartbeat(%s, %s, %s, %s, %s, %s, %s)" % (
            self.type,
            self.laps_to_go,
            self.time_to_go,
            self.time_of_day,
            self.race_time,
            self.flag_status,
            self.timestamp
        )


class RunInformationMessage(object):

    def __init__(self, fields):
        self.type = '$B'
        self.timestamp = datetime.now()

        # A unique run number
        # (1 - 99)
        self.unique_number = fields[0]

        # 40 characters maximum
        # (characters)
        self.description = fields[1]

    def __repr__(self):
        return "RunInformation(%s, %s, %s, %s)" % (
            self.type,
            self.unique_number,
            self.description,
            self.timestamp
        )


class RaceInformationMessage(object):

    def __init__(self, fields):
        self.type = '$G'
        self.timestamp = datetime.now()

        # The race position
        # (1 - 99)
        self.position = fields[0]

        # 8 characters maximum
        # (characters)
        self.registration_number = fields[1]

        # The number of laps
        # (0 - 99999)
        self.laps = fields[2]

        # Race time
        # (HH:MM:SS.DDD)
        self.total_time = Duration(fields[3])

    def __repr__(self):
        return "RaceInformation(%s, %s, %s, %s, %s, %s)" % (
            self.type,
            self.position,
            self.registration_number,
            self.laps,
            self.total_time,
            self.timestamp
        )


class CompetitorInformationMessage(object):

    def __init__(self, fields):
        self.type = '$A'
        self.timestamp = datetime.now()

        # 8 characters maximum (usually the competitor number)
        # (characters)
        self.registration_number = fields[0]

        # 5 characters maximum
        # (characters)
        self.number = fields[1]

        # No notes
        # (1 - 2.097.151)
        self.transponder_number = fields[2]

        # 9 characters maximum
        # (characters)
        self.first_name = fields[3]

        # 30 characters maximum
        # (characters)
        self.last_name = fields[4]

        # 50 characters maximum
        # (characters)
        self.nationality = fields[5]

        # The unique class number (see $C record description for details)
        # (1 - 99)
        self.class_number = fields[6]

    def __repr__(self):
        return "CompetitorInformation(%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.type,
            self.registration_number,
            self.number,
            self.transponder_number,
            self.first_name,
            self.last_name,
            self.nationality,
            self.class_number,
            self.timestamp
        )


class CompInformationMessage(object):

    def __init__(self, fields):
        self.type = '$COMP'
        self.timestamp = datetime.now()

        # 8 characters maximum (usually the competitor number)
        # (characters)
        self.registration_number = fields[0]

        # 5 characters maximum
        # (characters)
        self.number = fields[1]

        # The unique class number (see $C record description for details)
        # (1 - 99)
        self.class_number = fields[2]

        # 9 characters maximum
        # (characters)
        self.first_name = fields[3]

        # 30 characters maximum
        # (characters)
        self.last_name = fields[4]

        # 50 characters maximum
        # (characters)
        self.nationality = fields[5]

        # 50 characters maximum
        # (characters)
        self.additional_data = fields[6]

    def __repr__(self):
        return "CompInformation(%s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.type,
            self.registration_number,
            self.number,
            self.class_number,
            self.first_name,
            self.last_name,
            self.nationality,
            self.additional_data,
            self.timestamp
        )


class ClassInformationMessage(object):

    def __init__(self, fields):
        self.type = '$C'
        self.timestamp = datetime.now()

        # A unique class number
        # (1 - 99)
        self.unique_number = fields[0]

        # 40 characters
        # (characters)
        self.description = fields[1]

    def __repr__(self):
        return "ClassInformation(%s, %s, %s, %s)" % (
            self.type,
            self.unique_number,
            self.description,
            self.timestamp
        )


class PracticeQualifyingInformationMessage(object):

    def __init__(self, fields):
        self.type = '$H'
        self.timestamp = datetime.now()

        # The practice/qualifying position
        # (1 - 999)
        self.position = fields[0]

        # 8 characters maximum
        # (characters)
        self.registration_number = fields[1]

        # The lap number of the best lap
        # (0 - 9999)
        self.best_lap = fields[2]

        # The lap time of the best lap
        # (HH:MM:SS.DDD)
        self.best_lap_time = Duration(fields[3])

    def __repr__(self):
        return "PracticeQualifyingInformation(%s, %s, %s, %s, %s, %s)" % (
            self.type,
            self.position,
            self.registration_number,
            self.best_lap,
            self.best_lap_time,
            self.timestamp
        )


class SettingInformationMessage(object):

    def __init__(self, fields):
        self.type = '$E'
        self.timestamp = datetime.now()

        # Track name, track length
        # (name of the setting)
        self.description = fields[0]

        # 40 characters maximum for track name
        # 8 characters maximum for track length
        # (characters)
        self.value = fields[1]

    def __repr__(self):
        return "SettingInformation(%s, %s, %s, %s)" % (
            self.type,
            self.description,
            self.value,
            self.timestamp
        )


class InitRecordMessage(object):

    def __init__(self, fields):
        self.type = '$I'
        self.timestamp = datetime.now()

        # The current time
        # (HH:MM:SS.DDD)
        self.time_of_day = Duration(fields[0])

        # The current date
        # (dd mmmm yy)
        self.date = fields[1]

    def __repr__(self):
        return "InitRecord(%s, %s, %s, %s)" % (
            self.type,
            self.time_of_day,
            self.date,
            self.timestamp
        )


class PassingInformationMessage(object):

    def __init__(self, fields):
        self.type = '$J'
        self.timestamp = datetime.now()

        # 8 characters maximum
        # (characters)
        self.registration_number = fields[0]

        # The current lap time
        # (HH:MM:SS.DDD)
        self.lap_time = Duration(fields[1])

        # The total time
        # (HH:MM:SS.DDD)
        self.total_time = Duration(fields[2])

    def __repr__(self):
        return "PassingInformation(%s, %s, %s, %s, %s)" % (
            self.type,
            self.registration_number,
            self.lap_time,
            self.total_time,
            self.timestamp
        )


class LapInformationMessage(object):

    def __init__(self, fields):
        self.type = '$SP/$SR'
        self.timestamp = datetime.now()

        # Undocumented...
        self.position = fields[0]
        self.registration_number = fields[1]
        self.lap_number = fields[2]
        self.lap_time = Duration(fields[3])

    def __repr__(self):
        return "LapInformation(%s, %s, %s, %s, %s, %s)" % (
            self.type,
            self.position,
            self.registration_number,
            self.lap_number,
            self.lap_time,
            self.timestamp
        )


#############
#  Helpers
#############

MESSAGE_TYPES = {
    # Documented...
    "$A":    CompetitorInformationMessage,
    "$B":    RunInformationMessage,
    "$C":    ClassInformationMessage,
    "$COMP": CompInformationMessage,
    "$E":    SettingInformationMessage,
    "$F":    HeartbeatMessage,
    "$G":    RaceInformationMessage,
    "$H":    PracticeQualifyingInformationMessage,
    "$I":    InitRecordMessage,
    "$J":    PassingInformationMessage,

    # Undocumented...
    "$SP":   LapInformationMessage,
    "$SR":   LapInformationMessage,

    # TODO: Figure out what these are for?
    # $RMLT
    # $RMS
    # $RMDTL
    # $RMCA
}
