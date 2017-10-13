from core.snapshot import Snapshot
from core.snapshot_history import SnapshotHistory

class Account:

    def __init__(self, name, owner, symbol, asset_class, institution, account_type):
        self.name = name
        self.owner = owner
        self.symbol = symbol
        self.asset_class = asset_class
        self.institution = institution
        self.account_type = account_type
        self.history = SnapshotHistory()

    def value(self, query_time=None):
        return self.history.value(query_time)

    def import_snapshot(self, time, value):
        snapshot = Snapshot(time,value)
        return self.history.import_snapshot(snapshot)

    def last_updated(self):
        return self.history.last_updated()

    def is_identical_to(self, account):
        return ( self.name == account.name and
                 self.owner == account.owner and
                 self.symbol == account.symbol and
                 self.asset_class == account.asset_class and
                 self.institution == account.institution and
                 self.account_type == account.account_type )