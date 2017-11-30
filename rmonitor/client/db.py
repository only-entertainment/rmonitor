import json
from collections import namedtuple
from datetime import datetime

# Tuples for easier storage and access
from rmonitor.common.helpers import JSONEncoder, as_sorted_list

Meta = namedtuple('Meta', 'last_updated')
Driver = namedtuple('Driver', 'TODO')
Team = namedtuple('Team', 'TODO')
Class = namedtuple('Class', 'unique_number, description')
Race = namedtuple('Race', 'laps_to_go, time_to_go, time_of_day, race_time, flag_status')
Track = namedtuple('Track', 'name, length')


class DB(object):
    """
    In-memory data store for bootstrapping this quickly.

    TODO: Use a real database!
    """
    db = None

    def __init__(self):
        self.initialize()

    def initialize(self):
        """
        Can be called at __init__ or as a clear later
        """

        db = dict()

        db['meta'] = Meta(None)
        db['race'] = Race(None, None, None, None, None)
        db['track'] = Track(None, None)
        db['classes'] = set([])
        db['teams'] = set([])
        db['drivers'] = set([])

        self.db = db

    def __repr__(self):
        return json.dumps(
            self.db,
            cls=JSONEncoder,
            indent=4,
            sort_keys=True
        )

    def last_updated(self):
        # Gross.
        meta = self.db['meta']
        meta = meta._replace(last_updated=datetime.now())
        self.db['meta'] = meta

    def update_race(self, r):
        # Overwrite previous contents
        self.db['race'] = Race(**r)
        self.last_updated()

    def get_race(self):
        return self.db['race']

    def update_track(self, t):
        # Overwrite previous contents
        self.db['track'] = Track(**t)
        self.last_updated()

    def get_track(self):
        return self.db['track']

    def add_class(self, c):
        self.db['classes'].add(
            Class(**c)
        )
        self.last_updated()

    def get_classes(self):
        return as_sorted_list(
            self.db['classes'], 'unique_number'
        )

    def add_driver(self, d):
        self.db['drivers'].add(
            Driver(**d)
        )
        self.last_updated()

    def get_drivers(self):
        return self.db['drivers']

    def add_driver_to_team(self, t, d):
        # TODO
        self.last_updated()

    def get_drivers_for_team(self, t):
        # TODO
        pass

    def add_team(self, t):
        self.db['teams'].add(
            Team(**t)
        )
        self.last_updated()

    def get_teams(self):
        return self.db['teams']

    def get_teams_for_class(self, c):
        # TODO
        pass
