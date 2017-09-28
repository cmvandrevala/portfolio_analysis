import csv

from finance.portfolio import Portfolio

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
            self.__create_asset_or_liability(row)

    def __create_asset_or_liability(self, row):
        if row[5] == "ASSET":
            self.portfolio.import_asset_data({"name": row[2], "date": row[0], "value": float(row[6]), "symbol": row[4]})
        else:
            self.portfolio.import_liability_data({"name": row[2], "date": row[0], "value": float(row[6]), "symbol": row[4]})
