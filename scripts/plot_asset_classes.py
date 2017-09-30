import csv
import matplotlib.pyplot as plt

from general_ledger.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.presenter import Presenter

portfolio = PortfolioCreator(Constants.GENERAL_LEDGER_PATH).create()
asset_classes = portfolio.asset_classes()

plt.bar(range(len(asset_classes)), asset_classes.values(), align='center')
plt.xticks(range(len(asset_classes)), asset_classes.keys())

plt.ylabel('Weight (% of Portfolio)')
plt.title('Asset Class Weights')

plt.show()
