from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from terminaltables import AsciiTable
from utilities.constants import Constants

portfolio = PortfolioCreator().create(DataSource())
data = []

data.append(Constants.BALANCE_SHEET_HEADERS)

for asset in portfolio.assets():
    data.append(asset.balance_sheet_row())

data.append(Constants.BALANCE_SHEET_SPACERS)

for liability in portfolio.liabilities():
    data.append(liability.balance_sheet_row())

data.append(["", "", "", "", "", "Total", str(portfolio.total_value())])

t = AsciiTable(data)
t.inner_footing_row_border = True
print(t.table)
