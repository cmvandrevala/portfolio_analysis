import matplotlib.pyplot as plt
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator().create(DataSource())
unsorted_data = portfolio.asset_classes()
asset_classes = {}

sorted_names = sorted(unsorted_data, key=unsorted_data.__getitem__)
for k in sorted_names:
    asset_classes[k] = unsorted_data[k]

plt.bar(range(len(asset_classes)), asset_classes.values(), align='center')
plt.xticks(range(len(asset_classes)), asset_classes.keys())

plt.ylabel('Weight (% of Portfolio)')
plt.title('Asset Class Weights')

plt.show()
