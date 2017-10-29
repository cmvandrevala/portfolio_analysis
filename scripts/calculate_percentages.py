import csv
import matplotlib.pyplot as plt

from portfolio_creator.portfolio_creator import PortfolioCreator
from portfolio_creator.data_source import DataSource
from utilities.presenter import Presenter

portfolio = PortfolioCreator().create(DataSource())
unsorted_data = portfolio.percentages()
percentages = {}

sorted_names = sorted(unsorted_data, key=unsorted_data.__getitem__)
for k in sorted_names:
    percentages[k] = unsorted_data[k]

with open("percentages.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Symbol', 'Weight'])
    for symbol, percentage in percentages.items():
        writer.writerow([symbol, Presenter.decimal_as_percentage(percentage)])

plt.bar(range(len(percentages)), percentages.values(), align='center')
plt.xticks(range(len(percentages)), percentages.keys(), rotation=90)

plt.ylabel('Weight (% of Portfolio)')
plt.title('Asset Weights')

plt.show()
