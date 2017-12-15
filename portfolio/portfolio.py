from collections import defaultdict
from utilities.epoch_timestamp_converter import EpochTimestampConverter
from portfolio.account import Account
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass


class Portfolio:
    def __init__(self):
        self.accounts = []

    def assets(self):
        return list(filter(lambda x: x.account_type() == "ASSET", self.accounts))

    def liabilities(self):
        return list(filter(lambda x: x.account_type() == "LIABILITY", self.accounts))

    def import_data(self, data):
        name = data.get("name")
        date = data.get("date")
        value = data.get("value")
        institution = data.get("institution")
        owner = data.get("owner")
        symbol = data.get("symbol")
        asset_class = AssetClass(data.get("asset_class"))
        account_type = AccountType(data.get("account_type"))
        account = Account(name, owner, symbol, asset_class, institution, account_type)
        self.__create_or_update(date, value, account)

    def percentages(self):
        output = defaultdict(float)
        for asset in self.assets():
            output[asset.symbol] += asset.value()
        self.__normalize_output(output)
        return output

    def asset_classes(self):
        output = dict((v, 0) for v in [e.value for e in AssetClass])
        for asset in self.assets():
            output[asset.asset_class()] += asset.value()
        self.__normalize_output(output)
        del output["None"]
        return output

    def total_value(self, date=None):
        return round(self.__value_of(self.assets(), date) - self.__value_of(self.liabilities(), date), 2)

    def __normalize_output(self, output):
        for key, value in output.items():
            if self.total_value() == 0:
                output[key] = 0
            else:
                output[key] = round(float(value) / self.__value_of(self.assets()), 3)

    def __value_of(self, accounts, date=None):
        return sum(account.value(EpochTimestampConverter().epoch(date)) for account in accounts)

    def __create_or_update(self, date, value, account):
        for existing_account in self.accounts:
            if existing_account.is_identical_to(account):
                existing_account.import_snapshot(EpochTimestampConverter().epoch(date), value)
                return
        account.import_snapshot(EpochTimestampConverter().epoch(date), value)
        self.accounts.append(account)
