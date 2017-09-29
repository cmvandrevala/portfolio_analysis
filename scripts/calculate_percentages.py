import csv
import matplotlib.pyplot as plt

from general_ledger.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.presenter import Presenter

portfolio = PortfolioCreator(Constants.GENERAL_LEDGER_PATH).create()
percentages = portfolio.percentages()

with open('percentages.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Symbol', 'Weight'])
    for symbol, percentage in percentages.items():
        writer.writerow([symbol, Presenter.percentage(percentage)])

plt.bar(range(len(percentages)), percentages.values(), align='center')
plt.xticks(range(len(percentages)), percentages.keys())

plt.ylabel('Weight (% of Portfolio)')
plt.title('Asset Weights')

plt.show()
