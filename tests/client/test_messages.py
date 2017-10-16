from unittest import TestCase
from race_monitor.client.messages import *


class TestHeartbeatMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$F,14,"00:12:45","13:34:23","00:09:47","Green"'
        )

        self.assertEqual(obj.type, '$F')
        self.assertEqual(obj.laps_to_go, '14')
        self.assertEqual(obj.time_to_go, '00:12:45')
        self.assertEqual(obj.time_of_day, '13:34:23')
        self.assertEqual(obj.race_time, '00:09:47')
        self.assertEqual(obj.flag_status, 'Green')

        self.assertEqual(
            str(obj),
            'Heartbeat($F, 14, 00:12:45, 13:34:23, 00:09:47, Green)'
        )


class TestRunInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$B,5,"Friday free practice"'
        )

        self.assertEqual(obj.type, '$B')
        self.assertEqual(obj.unique_number, '5')
        self.assertEqual(obj.description, 'Friday free practice')

        self.assertEqual(
            str(obj),
            'RunInformation($B, 5, Friday free practice)'
        )


class TestRaceInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$G,3,"1234BE",14,"01:12:47.872"'
        )

        self.assertEqual(obj.type, '$G')
        self.assertEqual(obj.position, '3')
        self.assertEqual(obj.registration_number, '1234BE')
        self.assertEqual(obj.laps, '14')
        self.assertEqual(obj.total_time, '01:12:47.872')

        self.assertEqual(
            str(obj),
            'RaceInformation($G, 3, 1234BE, 14, 01:12:47.872)'
        )


class TestCompetitorInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$A,"1234BE","12X",52474,"John","Johnson","USA",5'
        )

        self.assertEqual(obj.type, '$A')
        self.assertEqual(obj.registration_number, '1234BE')
        self.assertEqual(obj.number, '12X')
        self.assertEqual(obj.transponder_number, '52474')
        self.assertEqual(obj.first_name, 'John')
        self.assertEqual(obj.last_name, 'Johnson')
        self.assertEqual(obj.nationality, 'USA')
        self.assertEqual(obj.class_number, '5')

        self.assertEqual(
            str(obj),
            'CompetitorInformation($A, 1234BE, 12X, 52474, John, Johnson, USA, 5)'
        )
        

class TestCompInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$COMP,"1234BE","12X",5,"John","Johnson","USA","CAMEL"'
        )

        self.assertEqual(obj.type, '$COMP')
        self.assertEqual(obj.registration_number, '1234BE')
        self.assertEqual(obj.number, '12X')
        self.assertEqual(obj.class_number, '5')
        self.assertEqual(obj.first_name, 'John')
        self.assertEqual(obj.last_name, 'Johnson')
        self.assertEqual(obj.nationality, 'USA')
        self.assertEqual(obj.additional_data, 'CAMEL')

        self.assertEqual(
            str(obj),
            'CompInformation($COMP, 1234BE, 12X, 5, John, Johnson, USA, CAMEL)'
        )


class TestClassInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$C,5,"Formula 300"'
        )

        self.assertEqual(obj.type, '$C')
        self.assertEqual(obj.unique_number, '5')
        self.assertEqual(obj.description, "Formula 300")

        self.assertEqual(
            str(obj),
            'ClassInformation($C, 5, Formula 300)'
        )


class TestPracticeQualifyingInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$H,2,"1234BE",3,"00:02:17.872"'
        )

        self.assertEqual(obj.type, '$H')
        self.assertEqual(obj.position, '2')
        self.assertEqual(obj.registration_number, '1234BE')
        self.assertEqual(obj.best_lap, '3')
        self.assertEqual(obj.best_lap_time, '00:02:17.872')

        self.assertEqual(
            str(obj),
            'PracticeQualifyingInformation($H, 2, 1234BE, 3, 00:02:17.872)'
        )


class TestSettingInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$E,"TRACKNAME","Indianapolis Motor Speedway"'

        )

        self.assertEqual(obj.type, '$E')
        self.assertEqual(obj.description, 'TRACKNAME')
        self.assertEqual(obj.value, 'Indianapolis Motor Speedway')

        self.assertEqual(
            str(obj),
            'SettingInformation($E, TRACKNAME, Indianapolis Motor Speedway)'
        )

        obj = MessageFactory.get_message(
            b'$E,"TRACKLENGTH","2.500"'
        )

        self.assertEqual(obj.type, '$E')
        self.assertEqual(obj.description, 'TRACKLENGTH')
        self.assertEqual(obj.value, '2.500')

        self.assertEqual(
            str(obj),
            'SettingInformation($E, TRACKLENGTH, 2.500)'
        )


class TestInitRecordMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$I,"16:36:08.000","12 jan 01"'
        )

        self.assertEqual(obj.type, '$I')
        self.assertEqual(obj.time_of_day, '16:36:08.000')
        self.assertEqual(obj.date, '12 jan 01')

        self.assertEqual(
            str(obj),
            'InitRecord($I, 16:36:08.000, 12 jan 01)'
        )


class TestPassingInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$J,"1234BE","00:02:03.826","01:42:17.672"'
        )

        self.assertEqual(obj.type, '$J')
        self.assertEqual(obj.registration_number, '1234BE')
        self.assertEqual(obj.lap_time, '00:02:03.826')
        self.assertEqual(obj.total_time, '01:42:17.672')

        self.assertEqual(
            str(obj),
            'PassingInformation($J, 1234BE, 00:02:03.826, 01:42:17.672)'
        )


class TestLapInformationMessage(TestCase):

    def test_parse(self):
        obj = MessageFactory.get_message(
            b'$SP,1,"ABCD123",3,"00:01:08.123"'
        )

        self.assertEqual(obj.type, '$SP/$SR')
        self.assertEqual(obj.position, '1')
        self.assertEqual(obj.registration_number, 'ABCD123')
        self.assertEqual(obj.lap_number, '3')
        self.assertEqual(obj.lap_time, '00:01:08.123')

        self.assertEqual(
            str(obj),
            'LapInformation($SP/$SR, 1, ABCD123, 3, 00:01:08.123)'
        )

        obj = MessageFactory.get_message(
            b'$SR,1,"ABCD123",3,"00:01:08.123"'
        )

        self.assertEqual(obj.type, '$SP/$SR')
        self.assertEqual(obj.position, '1')
        self.assertEqual(obj.registration_number, 'ABCD123')
        self.assertEqual(obj.lap_number, '3')
        self.assertEqual(obj.lap_time, '00:01:08.123')

        self.assertEqual(
            str(obj),
            'LapInformation($SP/$SR, 1, ABCD123, 3, 00:01:08.123)'
        )


class TestMessageFactory(TestCase):

    def test_get_message(self):
        msg = MessageFactory.get_message(b'')
        self.assertEqual(msg, None)

        # Binary
        msg = MessageFactory.get_message(b'$MONEY,1,2,3')
        self.assertEqual(msg, None)

        # String
        msg = MessageFactory.get_message('$MONEY,1,2,3')
        self.assertEqual(msg, None)

        msg = MessageFactory.get_message(b'$I,"16:36:08.000","12 jan 01"')
        self.assertTrue(msg)
