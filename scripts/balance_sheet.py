import csv

from terminaltables import AsciiTable
from general_ledger.portfolio_creator import PortfolioCreator
from utilities.constants import Constants

portfolio = PortfolioCreator(Constants.LOCAL_LEDGER_PATH).create()
data = []

data.append(["Last Updated", "Institution", "Name", "Owner", "Asset Class", "Value"])

for asset in portfolio.assets():
    data.append([asset.last_updated(), asset.institution, asset.name, asset.owner, asset.asset_class(), str(asset.value())])

for liability in portfolio.liabilities():
    data.append([liability.last_updated(), liability.institution, liability.name, "-", "-", str(liability.value())])

data.append(["", "", "", "", "Total", str(portfolio.total_value())])

t = AsciiTable(data)
t.inner_footing_row_border = True
print(t.table)
