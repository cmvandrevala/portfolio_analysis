import csv

from finance.portfolio import Portfolio

class PortfolioCreator:

    def __init__(self, general_ledger_path):
        self.general_ledger_path = general_ledger_path

    def create(self):
        portfolio = Portfolio()
        with open(self.general_ledger_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                if row[5] == "ASSET":
                    portfolio.import_asset_data({"name": row[2], "date": row[0], "value": float(row[6])})
                else:
                    portfolio.import_liability_data({"name": row[2], "date": row[0], "value": float(row[6])})
        return portfolio
