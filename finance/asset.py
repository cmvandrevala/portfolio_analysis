import time

from finance.snapshot import Snapshot

class Asset:

    def __init__(self, name):
        self.name = name
        self.snapshots = []

    def value(self, query_time=None):
        if(self.snapshots == []):
            return 0
        if(query_time == None):
            return self.__find_asset_value(time.time())
        return self.__find_asset_value(query_time)

    def import_snapshot(self, time, value):
        snapshot = Snapshot(time,value)
        self.snapshots.append(snapshot)
        self.snapshots.sort(key = lambda x : x.timestamp)

    def __find_asset_value(self, query_time):
        asset_value = 0
        for snapshot in self.snapshots:
            if (query_time > snapshot.timestamp):
                asset_value = snapshot.value
        return asset_value
