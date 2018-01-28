from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter


class BalanceSheet:
    def asset_row(self, account):
        return [self.__last_updated_for_balance_sheet(account), account.institution, account.name, account.investment,
                account.owner, str(account.value())]

    def liabilities_row(self, account):
        return [self.__last_updated_for_liabilities_row(account), account.institution, account.name, account.investment, account.owner,
                str(account.value())]

    def __last_updated_for_balance_sheet(self, account):
        last_updated_epoch = EpochTimestampConverter().epoch(account.last_updated())
        if last_updated_epoch > EpochTimestampConverter().epoch():
            return self.__color_last_updated(account, "\x1b[1;31;40m")
        elif self.__within_time_period(last_updated_epoch, 90):
            return self.__color_last_updated(account, "\x1b[1;31;40m")
        elif self.__within_time_period(last_updated_epoch, 60):
            return self.__color_last_updated(account, "\x1b[1;35;40m")
        elif self.__within_time_period(last_updated_epoch, 30):
            return self.__color_last_updated(account, "\x1b[0;33;40m")
        else:
            return self.__color_last_updated(account)

    def __last_updated_for_liabilities_row(self, account):
        last_updated_epoch = EpochTimestampConverter().epoch(account.last_updated())
        if self.__within_time_period(last_updated_epoch, 7):
            return self.__color_last_updated(account, "\x1b[1;31;40m")
        else:
            return self.__color_last_updated(account)

    def __within_time_period(self, last_updated_epoch, days):
        return last_updated_epoch < EpochTimestampConverter().epoch() - days * Constants.SECONDS_PER_DAY

    def __color_last_updated(self, account, color=None):
        if color is None:
            return account.last_updated()
        else:
            return color + account.last_updated() + "\x1b[0m"
