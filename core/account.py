from core.snapshot import Snapshot
from core.snapshot_history import SnapshotHistory

class Account:

    def __init__(self, name, owner, symbol, asset_class, institution):
        self.name = name
        self.owner = owner
        self.symbol = symbol
        self.asset_class = asset_class
        self.institution = institution
        self.history = SnapshotHistory()

    def value(self, query_time=None):
        return self.history.value(query_time)

    def import_snapshot(self, time, value):
        snapshot = Snapshot(time,value)
        return self.history.import_snapshot(snapshot)

    def last_updated(self):
        return self.history.last_updated()
