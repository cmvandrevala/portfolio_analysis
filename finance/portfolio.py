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
        date = data["date"]
        value = data["value"]
        self.__create_or_update_asset(name, date, value)

    def import_liability_data(self, data):
        name = data["name"]
        date = data["date"]
        value = data["value"]
        self.__create_or_update_liability(name, date, value)

    def percentages(self):
        return dict((a.name, self.__percentage(a.value())) for a in self.assets)

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

    def __create_or_update_asset(self, name, date, value):
        for asset in self.assets:
            if asset.name == name:
                asset.import_snapshot(self.__extract_date(date), value)
                return
        asset = Asset(name)
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
