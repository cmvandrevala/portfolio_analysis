from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from visualizations.bar_graph import BarGraph

portfolio = PortfolioCreator().create(DataSource())
unsorted_data = portfolio.asset_classes()
asset_classes = {}

sorted_names = sorted(unsorted_data, key=unsorted_data.__getitem__)
for k in sorted_names:
    asset_classes[k] = unsorted_data[k]

params = {"title": "Asset Class Weights", "ylabel": "Weight (% of Portfolio)"}
BarGraph.single_dataset(asset_classes, params)
