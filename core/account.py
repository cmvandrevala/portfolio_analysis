from core.snapshot import Snapshot
from core.snapshot_history import SnapshotHistory
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass

class Account:

    def __init__(self, name, owner, symbol, asset_class, institution, account_type):
        self.name = name
        self.owner = owner
        self.symbol = symbol
        self.__asset_class = asset_class
        self.institution = institution
        self.__account_type = account_type
        self.history = SnapshotHistory()

    def account_type(self):
        return self.__account_type.value

    def asset_class(self):
        return self.__asset_class.value

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
                 self.asset_class() == account.asset_class() and
                 self.institution == account.institution and
                 self.account_type() == account.account_type() )

    def balance_sheet_row(self):
        return [self.last_updated(), self.institution, self.name, self.symbol, self.owner, self.asset_class(), str(self.value())]
