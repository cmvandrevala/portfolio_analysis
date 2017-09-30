import datetime
import time

from finance.asset import Asset
from finance.liability import Liability

class Portfolio:

    def __init__(self):
        self.assets = []
        self.liabilities = []

    def import_asset_data(self, data):
        name = data["name"]
        symbol = data["symbol"]
        date = data["date"]
        value = data["value"]
        asset_class = data["asset_class"]
        self.__create_or_update_asset(name, symbol, date, value, asset_class)

    def import_liability_data(self, data):
        name = data["name"]
        symbol = data["symbol"]
        date = data["date"]
        value = data["value"]
        self.__create_or_update_liability(name, symbol, date, value)

    def percentages(self):
        output = {}
        for asset in self.assets:
            if asset.symbol in output:
                output[asset.symbol] += asset.value()
            else:
                output[asset.symbol] = asset.value()
        for key, value in output.items():
            if self.total_value() == 0:
                output[key] = 0
            else:
                output[key] = round(float(value)/self.__assets_value(),3)
        return output

    def asset_classes(self):
        output = {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0}
        for asset in self.assets:
            output[asset.asset_class] += asset.value()
        for key, value in output.items():
            if self.total_value() == 0:
                output[key] = 0
            else:
                output[key] = round(float(value)/self.__assets_value(),3)
        return output

    def total_value(self, date=None):
        return round(self.__assets_value(date) + self.__liabilities_value(date), 2)

    def __assets_value(self, date=None):
        if date == None:
            return sum(asset.value() for asset in self.assets)
        else:
            return sum(asset.value(self.__extract_date(date)) for asset in self.assets)

    def __liabilities_value(self, date=None):
        if date == None:
            return sum(liability.value() for liability in self.liabilities)
        else:
            return sum(liability.value(self.__extract_date(date)) for liability in self.liabilities)

    def __create_or_update_asset(self, name, symbol, date, value, asset_class):
        for asset in self.assets:
            if asset.name == name and asset.symbol == symbol:
                asset.import_snapshot(self.__extract_date(date), value)
                return
        asset = Asset(name, symbol, asset_class)
        asset.import_snapshot(self.__extract_date(date), value)
        self.assets.append(asset)

    def __create_or_update_liability(self, name, symbol, date, value):
        for liability in self.liabilities:
            if liability.name == name:
                liability.import_snapshot(self.__extract_date(date), value)
                return
        liability = Liability(name, symbol)
        liability.import_snapshot(self.__extract_date(date), value)
        self.liabilities.append(liability)

    def __extract_date(self, date_string):
        year = int(date_string.split("-")[0])
        month = int(date_string.split("-")[1])
        day = int(date_string.split("-")[2])
        dt = datetime.datetime(year=year, month=month, day=day)
        return time.mktime(dt.timetuple())

    def __percentage(self, value):
        return 0 if self.__assets_value() == 0 else round(value / self.__assets_value(), 3)
