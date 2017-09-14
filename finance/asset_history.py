import time

class AssetHistory:

    def __init__(self):
        self.snapshots = []

    def asset_value(self, query_time=None):
        if(self.snapshots == []):
            return 0
        if(query_time == None):
            return self.__find_asset_value(time.time())
        return self.__find_asset_value(query_time)

    def import_snapshot(self, snapshot):
        self.snapshots.append(snapshot)
        self.snapshots.sort(key = lambda x : x.timestamp)

    def __find_asset_value(self, query_time):
        asset_value = 0
        for snapshot in self.snapshots:
            if (query_time > snapshot.timestamp):
                asset_value = snapshot.value
        return asset_value
