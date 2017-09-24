import datetime
import time
from functools import reduce
from finance.asset import Asset

class Portfolio:

    def __init__(self):
        self.assets = []

    def import_asset_data(self, data):
        name = data["name"]
        date = data["date"]
        value = data["value"]
        self.__create_or_update_asset(name, date, value)

    def percentages(self):
        asset_sum = self.__total_portfolio_value()
        return dict((a.name, self.__percentage(a.value(), asset_sum)) for a in self.assets)

    def __create_or_update_asset(self, name, date, value):
        for asset in self.assets:
            if asset.name == name:
                asset.import_snapshot(self.__extract_date(date), value)
                return
        asset = Asset(name)
        asset.import_snapshot(self.__extract_date(date), value)
        self.assets.append(asset)

    def __extract_date(self):
        for asset in self.assets:
            if asset.name == name:
                asset.import_snapshot(self.__extract_date(date), value)
                return
        asset = Asset(name)
        asset.import_snapshot(self.__extract_date(date), value)
        self.assets.append(asset)

    def __extract_date(self, date_string):
        year = int(date_string.split("-")[0])
        month = int(date_string.split("-")[1])
        day = int(date_string.split("-")[2])
        dt = datetime.datetime(year=year, month=month, day=day)
        return time.mktime(dt.timetuple())

    def __total_portfolio_value(self):
        return sum(asset.value() for asset in self.assets)

    def __percentage(self, value, asset_sum):
        return 0 if asset_sum == 0 else round(value / asset_sum, 3)
