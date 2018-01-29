from collections import defaultdict

from portfolio.account_builder import AccountBuilder
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass


class Portfolio:
    def __init__(self):
        self.accounts = []

    def assets(self):
        return list(filter(lambda x: x.account_type() == "ASSET", self.accounts))

    def outdated_assets(self):
        return self.__outdated_account(self.assets())

    def liabilities(self):
        return list(filter(lambda x: x.account_type() == "LIABILITY", self.accounts))

    def outdated_liabilities(self):
        return self.__outdated_account(self.liabilities())

    def import_data(self, data):
        account = AccountBuilder()\
            .set_name(data.get("name"))\
            .set_institution(data.get("institution"))\
            .set_owner(data.get("owner"))\
            .set_investment(data.get("investment"))\
            .set_asset_class(AssetClass(data.get("asset_class")))\
            .set_account_type(AccountType(data.get("account_type")))\
            .set_update_frequency(data.get("update_frequency"))\
            .build()
        self.__create_or_update(data.get("timestamp"), data.get("value"), account)

    def import_account(self, account):
        for existing_account in self.accounts:
            if existing_account.is_identical_to(account):
                return
        self.accounts.append(account)

    def percentages(self):
        output = defaultdict(float)
        for asset in self.assets():
            output[asset.investment] += asset.value()
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
        return self.assets_value(date) - self.liabilities_value(date)

    def assets_value(self, date=None):
        return self.__value_of(self.assets(), date)

    def liabilities_value(self, date=None):
        return self.__value_of(self.liabilities(), date)

    def __outdated_account(self, accounts):
        output = []
        for account in accounts:
            last_updated = EpochTimestampConverter().epoch(account.last_updated())
            expected_update = EpochTimestampConverter().epoch() - account.update_frequency*Constants.SECONDS_PER_DAY
            if last_updated < expected_update:
                output.append(account)
        return output

    def __value_of(self, accounts, date=None):
        return sum(account.value(EpochTimestampConverter().epoch(date)) for account in accounts)

    def __normalize_output(self, output):
        for key, value in output.items():
            if self.total_value() == 0:
                output[key] = 0
            else:
                output[key] = round(float(value) / self.__value_of(self.assets()), 3)

    def __create_or_update(self, date, value, account):
        for existing_account in self.accounts:
            if existing_account.is_identical_to(account):
                existing_account.import_snapshot(EpochTimestampConverter().epoch(date), value)
                return
        account.import_snapshot(EpochTimestampConverter().epoch(date), value)
        self.accounts.append(account)
