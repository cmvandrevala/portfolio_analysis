import time

from finance.snapshot import Snapshot

class Asset:

    def __init__(self, name, symbol, asset_class):
        self.name = name
        self.symbol = symbol
        self.asset_class = asset_class
        self.snapshots = []

    def value(self, query_time=None):
        if(self.snapshots == []):
            return 0
        if(query_time == None):
            return self.__find_asset_value(time.time())
        return self.__find_asset_value(query_time)

    def import_snapshot(self, time, value):
        self.snapshots.append(Snapshot(time, value))
        self.snapshots.sort(key = lambda x : x.timestamp)

    def __find_asset_value(self, query_time):
        asset_value = 0
        for snapshot in self.snapshots:
            if (query_time > snapshot.timestamp):
                asset_value = snapshot.value
        return asset_value
