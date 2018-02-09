from portfolio.snapshot import Snapshot
from portfolio.snapshot_history import SnapshotHistory


class Account:
    def __init__(self, name, owner, investment, asset_class, institution, account_type, update_frequency=None,
                 open_date=None):
        self.name = name
        self.owner = owner
        self.investment = investment
        self.__asset_class = asset_class
        self.institution = institution
        self.__account_type = account_type
        if update_frequency is None:
            self.update_frequency = 7
        else:
            self.update_frequency = update_frequency
        self.open_date = open_date
        self.history = SnapshotHistory()

    def account_type(self):
        return self.__account_type.value

    def asset_class(self):
        return self.__asset_class.value

    def value(self, query_time=None):
        return self.history.value(query_time)

    def import_snapshot(self, time, value):
        snapshot = Snapshot(time, value)
        return self.history.import_snapshot(snapshot)

    def last_updated(self):
        return self.history.last_updated()

    def is_identical_to(self, account):
        return (self.name == account.name and
                self.owner == account.owner and
                self.investment == account.investment and
                self.asset_class() == account.asset_class() and
                self.institution == account.institution and
                self.account_type() == account.account_type() and
                self.open_date == account.open_date)
