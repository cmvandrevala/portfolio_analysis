import csv

from terminaltables import AsciiTable
from general_ledger.portfolio_creator import PortfolioCreator
from utilities.constants import Constants

portfolio = PortfolioCreator(Constants.GENERAL_LEDGER_PATH).create()
asset_data = []
liability_data = []

asset_data.append(["Last Updated", "Institution", "Name", "Owner", "Asset Class", "Value"])
liability_data.append(["Last Updated", "Institution", "Name", "Owner", "Asset Class", "Value"])

for asset in portfolio.assets:
    asset_data.append(["", asset.institution, asset.name, asset.owner, asset.asset_class, str(asset.value())])

for liability in portfolio.liabilities:
    liability_data.append(["", liability.institution, liability.name, "", "CASHX", str(-liability.value())])

asset_table = AsciiTable(asset_data)
liability_table = AsciiTable(liability_data)
print(asset_table.table)
print(liability_table.table)
print("Owners Equity: $" + str(portfolio.total_value()))
