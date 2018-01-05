from portfolio.snapshot import Snapshot
from portfolio.snapshot_history import SnapshotHistory
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter


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
        snapshot = Snapshot(time, value)
        return self.history.import_snapshot(snapshot)

    def last_updated(self):
        return self.history.last_updated()

    def is_identical_to(self, account):
        return (self.name == account.name and
                self.owner == account.owner and
                self.symbol == account.symbol and
                self.asset_class() == account.asset_class() and
                self.institution == account.institution and
                self.account_type() == account.account_type())

    def balance_sheet_row(self):
        return [self.__last_updated_for_balance_sheet(), self.institution, self.name, self.symbol, self.owner,
                self.asset_class(), str(self.value())]

    def liabilities_row(self):
        return [self.__last_updated_for_liabilities_row(), self.institution, self.name, self.owner, str(self.value())]

    def __last_updated_for_balance_sheet(self):
        last_updated_epoch = EpochTimestampConverter().epoch(self.last_updated())
        if last_updated_epoch > EpochTimestampConverter().epoch():
            return self.__color_last_updated("\x1b[1;31;40m")
        elif self.__within_time_period(last_updated_epoch, 90):
            return self.__color_last_updated("\x1b[1;31;40m")
        elif self.__within_time_period(last_updated_epoch, 60):
            return self.__color_last_updated("\x1b[1;35;40m")
        elif self.__within_time_period(last_updated_epoch, 30):
            return self.__color_last_updated("\x1b[0;33;40m")
        else:
            return self.__color_last_updated("\x1b[0;37;40m")

    def __last_updated_for_liabilities_row(self):
        last_updated_epoch = EpochTimestampConverter().epoch(self.last_updated())
        if self.__within_time_period(last_updated_epoch, 7):
            return self.__color_last_updated("\x1b[0;30;41m")
        else:
            return self.__color_last_updated()

    def __within_time_period(self, last_updated_epoch, days):
        return last_updated_epoch < EpochTimestampConverter().epoch() - days * Constants.SECONDS_PER_DAY

    def __color_last_updated(self, color=None):
        if color == None:
            return self.last_updated()
        else:
            return color + self.last_updated() + "\x1b[0m"
