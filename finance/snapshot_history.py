import time
import datetime

class SnapshotHistory:

    def __init__(self):
        self.snapshots = []

    def import_snapshot(self, snapshot):
        self.snapshots.append(snapshot)
        self.snapshots.sort(key = lambda x : x.timestamp)

    def all(self):
        return self.snapshots

    def value(self, query_time=None):
        if(self.snapshots == []):
            return 0
        if(query_time == None):
            return self.__find_value(time.time())
        return self.__find_value(query_time)

    def last_updated(self):
        final_snapshot = self.snapshots[-1]
        return datetime.datetime.fromtimestamp(final_snapshot.timestamp).strftime('%Y-%m-%d')

    def __find_value(self, query_time):
        value = 0
        for snapshot in self.snapshots:
            if (query_time > snapshot.timestamp):
                value = snapshot.value
        return value
