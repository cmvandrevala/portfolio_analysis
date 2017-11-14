import csv

from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from utilities.presenter import Presenter
from visualizations.bar_graph import BarGraph

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

params = {"title": "Asset Weights", "ylabel": "Weight (% of Portfolio)", "rotation": 90}
BarGraph.single_dataset(percentages, params)
