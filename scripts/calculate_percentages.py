import csv

from general_ledger.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.presenter import Presenter

portfolio = PortfolioCreator(Constants.GENERAL_LEDGER_PATH).create()

with open('percentages.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Symbol', 'Weight'])
    for symbol, percentage in portfolio.percentages().items():
        writer.writerow([symbol, Presenter.percentage(percentage)])
