import json
from collections import namedtuple
from datetime import datetime

# Tuples for easier storage and access
Meta = namedtuple('Meta', ('last_updated',))
Driver = namedtuple('Driver', ('TODO',))
Team = namedtuple('Team', ('TODO',))
Class = namedtuple('Class', ('TODO',))
Race = namedtuple('Race', ('TODO',))
Track = namedtuple('Track', ('name', 'length',))


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

        db['meta'] = Meta()
        db['race'] = Race()
        db['track'] = Track()
        db['classes'] = set()
        db['teams'] = set()
        db['drivers'] = set()

        self.db = db

    def __repr__(self):
        return json.dumps(self.db)

    def last_updated(self):
        self.db['meta'].last_updated = datetime.now()

    def update_race(self, r):
        # Overwrite previous contents
        self.db['race'] = Race(r)
        self.last_updated()

    def get_race(self):
        return self.db['race']

    def update_track(self, t):
        # Overwrite previous contents
        self.db['track'] = Track(t)
        self.last_updated()

    def get_track(self):
        return self.db['track']

    def add_class(self, c):
        self.db['classes'].add(
            Class(**c)
        )
        self.last_updated()

    def get_classes(self):
        return self.db['classes']

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
