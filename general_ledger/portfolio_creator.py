import csv
import json
import requests

from valid_options.account_type import AccountType
from utilities.constants import Constants
from core.portfolio import Portfolio

class PortfolioCreator:

    def __init__(self):
        self.portfolio = Portfolio()

    def create(self):
        data = requests.get(Constants.DATA_URL).text
        for item in json.loads(data):
            self.portfolio.import_data({ "date": item["timestamp"],
                                         "institution": item["institution"],
                                         "name": item["description"],
                                         "owner": item["owner"],
                                         "symbol": item["symbol"],
                                         "account_type": item["asset_or_liability"],
                                         "value": float(item["value"]),
                                         "asset_class": item["asset_class"] })
        return self.portfolio
