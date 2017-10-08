from collections import defaultdict
from utilities.epoch_converter import EpochConverter
from finance.asset import Asset
from finance.liability import Liability

class Portfolio:

    def __init__(self):
        self.assets = []
        self.liabilities = []

    def import_data(self, data):
        name = data.get("name")
        date = data.get("date")
        value = data.get("value")
        institution = data.get("institution")
        owner = data.get("owner", None)
        symbol = data.get("symbol", "CASHX")
        asset_class = data.get("asset_class", None)
        self.__create_entry(name, date, value, institution, owner, symbol, asset_class)

    def percentages(self):
        output = defaultdict(float)
        for asset in self.assets:
            output[asset.symbol] += asset.value()
        self.__normalize_output(output)
        return output

    def asset_classes(self):
        output = {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0}
        for asset in self.assets:
            output[asset.asset_class] += asset.value()
        self.__normalize_output(output)
        return output

    def total_value(self, date=None):
        return round(self.__value_of(self.assets, date) + self.__value_of(self.liabilities, date), 2)

    def __normalize_output(self, output):
        for key, value in output.items():
            if self.total_value() == 0:
                output[key] = 0
            else:
                output[key] = round(float(value)/self.__value_of(self.assets), 3)

    def __value_of(self, assets_or_liabilities, date=None):
        if date == None:
            return sum(asset_or_liability.value() for asset_or_liability in assets_or_liabilities)
        else:
            return sum(asset_or_liability.value(EpochConverter.date_to_epoch(date)) for asset_or_liability in assets_or_liabilities)

    def __create_entry(self, name, date, value, institution, owner, symbol, asset_class):
        if asset_class == None:
            self.__create_or_update(name, date, value, symbol, self.liabilities, Liability(name, institution))
        else:
            self.__create_or_update(name, date, value, symbol, self.assets, Asset(name, owner, symbol, asset_class, institution))

    def __create_or_update(self, name, date, value, symbol, category, asset_or_liability):
        for i in category:
            if i.name == name and i.symbol == symbol:
                i.import_snapshot(EpochConverter.date_to_epoch(date), value)
                return
        asset_or_liability.import_snapshot(EpochConverter.date_to_epoch(date), value)
        category.append(asset_or_liability)

    def __percentage(self, value):
        return 0 if self.__assets_value() == 0 else round(value / self.__assets_value(), 3)
