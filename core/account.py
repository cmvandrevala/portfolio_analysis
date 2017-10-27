from core.snapshot import Snapshot
from core.snapshot_history import SnapshotHistory
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter
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
        colored_date = self.__unicode_color() + self.last_updated() + "\x1b[0m"
        return [colored_date, self.institution, self.name, self.symbol, self.owner, self.asset_class(), str(self.value())]

    def __unicode_color(self):
        last_updated_epoch = EpochTimestampConverter().epoch(self.last_updated())
        if last_updated_epoch > EpochTimestampConverter().epoch():
            return "\x1b[1;31;40m"
        elif last_updated_epoch < EpochTimestampConverter().epoch() - 90*Constants.SECONDS_PER_DAY:
            return "\x1b[1;31;40m"
        elif last_updated_epoch < EpochTimestampConverter().epoch() - 60*Constants.SECONDS_PER_DAY:
            return "\x1b[1;35;40m"
        elif last_updated_epoch < EpochTimestampConverter().epoch() - 30*Constants.SECONDS_PER_DAY:
            return "\x1b[0;33;40m"
        else:
            return "\x1b[0;37;40m"
