import time

from finance.snapshot import Snapshot

class Liability:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.snapshots = []

    def value(self, query_time=None):
        if(self.snapshots == []):
            return 0
        if(query_time == None):
            return -self.__find_liability_value(time.time())
        return -self.__find_liability_value(query_time)

    def import_snapshot(self, time, value):
        self.snapshots.append(Snapshot(time, value))
        self.snapshots.sort(key = lambda x : x.timestamp)

    def __find_liability_value(self, query_time):
        liability_value = 0
        for snapshot in self.snapshots:
            if (query_time > snapshot.timestamp):
                liability_value = snapshot.value
        return liability_value
