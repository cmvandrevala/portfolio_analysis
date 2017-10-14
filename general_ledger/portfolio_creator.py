import csv

from valid_options.account_type import AccountType
from core.portfolio import Portfolio

class PortfolioCreator:

    def __init__(self, general_ledger_path):
        self.general_ledger_path = general_ledger_path
        self.portfolio = Portfolio()

    def create(self):
        with open(self.general_ledger_path) as csvfile:
            self.__import_all_rows(csvfile)
        return self.portfolio

    def __import_all_rows(self, csvfile):
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            self.__create_account(row)

    def __create_account(self, row):
        self.portfolio.import_data({ "date": row[0],
                                     "institution": row[1],
                                     "name": row[2],
                                     "owner": row[3],
                                     "symbol": row[4],
                                     "account_type": row[5],
                                     "value": float(row[6]),
                                     "asset_class": row[7] })
