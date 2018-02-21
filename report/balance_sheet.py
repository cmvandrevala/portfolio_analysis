from portfolio.portfolio import Portfolio
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter
from valid_options.snapshot_status import SnapshotStatus


class BalanceSheet:

    def __init__(self, portfolio=Portfolio()):
        self.portfolio = portfolio
        self.headers = ["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"]
        self.spacers = ["---", "---", "---", "---", "---", "---"]

    def create(self):
        data = [self.headers]
        for asset in self.portfolio.assets():
            data.append(self.row(asset))
        data.append(self.spacers)
        for liability in self.portfolio.liabilities():
            data.append(self.row(liability))
        data.append(["", "", "", "", "Total", '%.2f' % self.portfolio.total_value()])
        return data

    def row(self, account):
        return [self.__last_updated(account), account.institution(), account.name(), account.investment(), account.owner(),
                '%.2f' % account.value()]

    def __last_updated(self, account):
        last_updated_epoch = EpochDateConverter().date_to_epoch(account.last_updated())
        if self.__outside_valid_time_period(last_updated_epoch, account.update_frequency()):
            return self.__color_last_updated(account, SnapshotStatus.OUTDATED)
        else:
            return self.__color_last_updated(account, SnapshotStatus.CURRENT)

    def __outside_valid_time_period(self, last_updated_epoch: int, days: int) -> bool:
        return last_updated_epoch < EpochDateConverter().date_to_epoch() - days * Constants.SECONDS_PER_DAY or last_updated_epoch > EpochDateConverter().date_to_epoch()

    def __color_last_updated(self, account, snapshot_status):
        if snapshot_status == SnapshotStatus.CURRENT:
            return account.last_updated()
        else:
            return self.__color_red(account.last_updated())

    def __color_red(self, string_to_color: str) -> str:
        return "\x1b[1;31;40m" + string_to_color + "\x1b[0m"
