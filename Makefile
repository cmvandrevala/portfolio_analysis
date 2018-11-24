asset:
	python3 -m scripts.plot_asset_worth_vs_time

classes:
	python3 -m scripts.plot_asset_classes

de:
	python3 -m scripts.plot_debt_to_equity_vs_time

debt:
	python3 -m scripts.plot_debt_vs_time

mypy:
	python3 -m scripts.run_mypy

net:
	python3 -m scripts.plot_net_worth_vs_time

percentages:
	python3 -m scripts.calculate_percentages

start:
	FLASK_APP=app/main.py flask run

test:
	python -m unittest discover
