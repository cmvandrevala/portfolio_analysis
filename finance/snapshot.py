class Snapshot:

    def __init__(self, timestamp, asset_id, value):
        self.timestamp = timestamp
        self.asset_id = asset_id
        self.value = value

    def timestamp(self):
        return self.timestamp

    def asset_id(self):
        return self.asset_id

    def value(self):
        return self.value
