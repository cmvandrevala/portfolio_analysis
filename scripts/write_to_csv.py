import sys

from finance.portfolio import Portfolio
from finance.file_io import FileIO

fio = FileIO()
portfolio = Portfolio()

for filename in sys.argv[1:]:
    fio.importAssetsToPortfolio(filename, portfolio)

fio.writePortfolioToCsv(portfolio)
