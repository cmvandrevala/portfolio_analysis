from terminaltables import AsciiTable

from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from report.balance_sheet import BalanceSheet

portfolio = PortfolioCreator().create(DataSource())
data = BalanceSheet(portfolio).create()

t = AsciiTable(data)
t.inner_footing_row_border = True
print(t.table)
