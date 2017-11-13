balance:
	python3 -m scripts.balance_sheet

classes:
	python3 -m scripts.plot_asset_classes

net:
	python3 -m scripts.plot_net_worth_vs_time

percentages:
	python3 -m scripts.calculate_percentages

test:
	python3 -m unittest discover tests/annuity
	python3 -m unittest discover tests/core
	python3 -m unittest discover tests/portfolio_creator
	python3 -m unittest discover tests/utilities
