import datetime
import time

from collections import defaultdict
from finance.asset import Asset
from finance.liability import Liability

class Portfolio:

    def __init__(self):
        self.assets = []
        self.liabilities = []

    def import_data(self, data):
        if "asset_class" in data:
            self.__create_or_update_asset(data["name"], data["symbol"], data["date"], data["value"], data["asset_class"])
        else:
            self.__create_or_update_liability(data["name"], data["date"], data["value"])

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
                output[key] = round(float(value)/self.__assets_value(),3)

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

    def __create_or_update_liability(self, name, date, value):
        for liability in self.liabilities:
            if liability.name == name:
                liability.import_snapshot(self.__extract_date(date), value)
                return
        liability = Liability(name)
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
