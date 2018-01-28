from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter


class BalanceSheet:

    def __init__(self):
        self.RED = "\x1b[1;31;40m"

    def row(self, account):
        return [self.__last_updated(account), account.institution, account.name, account.investment, account.owner,
                str(account.value())]

    def __last_updated(self, account):
        last_updated_epoch = EpochTimestampConverter().epoch(account.last_updated())
        if last_updated_epoch > EpochTimestampConverter().epoch():
            return self.__color_last_updated(account, self.RED)
        elif self.__within_time_period(last_updated_epoch, 7):
            return self.__color_last_updated(account, self.RED)
        else:
            return self.__color_last_updated(account)

    def __within_time_period(self, last_updated_epoch, days):
        return last_updated_epoch < EpochTimestampConverter().epoch() - days * Constants.SECONDS_PER_DAY

    def __color_last_updated(self, account, color=None):
        if color is None:
            return account.last_updated()
        else:
            return color + account.last_updated() + "\x1b[0m"
