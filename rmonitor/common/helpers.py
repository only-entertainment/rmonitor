from datetime import datetime, timedelta


class Duration(object):

    def __init__(self, s):
        self.time = Duration.from_string(s)

    @staticmethod
    def from_string(s):

        try:
            t = datetime.strptime(s, "%H:%M:%S.%f")
        except Exception:
            # Handle this other case...
            t = datetime.strptime(s, "%H:%M:%S")

        delta = timedelta(
            hours=t.hour,
            minutes=t.minute,
            seconds=t.second,
            microseconds=t.microsecond
        )

        return delta

    def since_time(self, t):
        target = Duration.from_string(t)
        return self.time - target

    def until_time(self, t):
        target = Duration.from_string(t)
        return target - self.time

    def __repr__(self):
        return 'Duration(%s)' % self.time


if __name__ == '__main__':

    d = Duration("00:01:09.12345")
    print(str(d))

    print(d.since_time("00:01:09.12345"))
    print(d.since_time("00:00:09.12345"))
    print(d.since_time("00:00:00.12345"))
    print(d.since_time("00:00:00.12341"))

    print(d.until_time("00:01:09.12345"))
    print(d.until_time("00:01:19.12345"))
    print(d.until_time("00:02:19.12345"))
    print(d.until_time("00:02:19.12346"))
