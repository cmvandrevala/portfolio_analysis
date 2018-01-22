asset:
	python3 -m scripts.plot_asset_worth_vs_time

balance:
	python3 -m scripts.balance_sheet

classes:
	python3 -m scripts.plot_asset_classes

de:
	python3 -m scripts.plot_debt_to_equity_vs_time

mypy:
	python3 -m scripts.run_mypy

net:
	python3 -m scripts.plot_net_worth_vs_time

percentages:
	python3 -m scripts.calculate_percentages

recommend:
	python3 -m scripts.recommend_investment

test:
	python3 -m unittest discover tests/app
	python3 -m unittest discover tests/portfolio
	python3 -m unittest discover tests/portfolio_analysis
	python3 -m unittest discover tests/portfolio_creator
	python3 -m unittest discover tests/report
	python3 -m unittest discover tests/utilities
