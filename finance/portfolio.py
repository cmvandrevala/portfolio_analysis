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
        return round(self.__assets_value(date) + self.__liabilities_value(date), 2)

    def __normalize_output(self, output):
        for key, value in output.items():
            if self.total_value() == 0:
                output[key] = 0
            else:
                output[key] = round(float(value)/self.__assets_value(), 3)

    def __assets_value(self, date=None):
        if date == None:
            return sum(asset.value() for asset in self.assets)
        else:
            return sum(asset.value(EpochConverter.convert(date)) for asset in self.assets)

    def __liabilities_value(self, date=None):
        if date == None:
            return sum(liability.value() for liability in self.liabilities)
        else:
            return sum(liability.value(EpochConverter.convert(date)) for liability in self.liabilities)

    def __create_entry(self, name, date, value, institution, owner, symbol, asset_class):
        if asset_class == None:
            category = self.liabilities
            j = Liability(name, institution)
        else:
            category = self.assets
            j = Asset(name, owner, symbol, asset_class, institution)
        for i in category:
            if i.name == name and i.symbol == symbol:
                i.import_snapshot(EpochConverter.convert(date), value)
                return
        j.import_snapshot(EpochConverter.convert(date), value)
        category.append(j)

    def __percentage(self, value):
        return 0 if self.__assets_value() == 0 else round(value / self.__assets_value(), 3)
