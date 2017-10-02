import time

from finance.snapshot import Snapshot
from finance.snapshot_history import SnapshotHistory

class Liability:

    def __init__(self, name):
        self.name = name
        self.symbol = "CASHX"
        self.history = SnapshotHistory()

    def value(self, query_time=None):
        return -self.history.value(query_time)

    def import_snapshot(self, time, value):
        snapshot = Snapshot(time,value)
        return self.history.import_snapshot(snapshot)
