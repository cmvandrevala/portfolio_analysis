from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from terminaltables import AsciiTable

from report.balance_sheet import BalanceSheet
from utilities.constants import Constants

portfolio = PortfolioCreator().create(DataSource())
balance_sheet = BalanceSheet()
data = [Constants.BALANCE_SHEET_HEADERS]

for asset in portfolio.assets():
    data.append(balance_sheet.asset_row(asset))

data.append(Constants.BALANCE_SHEET_SPACERS)

for liability in portfolio.liabilities():
    data.append(balance_sheet.liabilities_row(liability))

data.append(["", "", "", "", "Total", str(portfolio.total_value())])

t = AsciiTable(data)
t.inner_footing_row_border = True
print(t.table)
