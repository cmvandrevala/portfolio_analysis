balance: import
	python3 -m scripts.balance_sheet

classes: import
	python3 -m scripts.plot_asset_classes

clean:
	python3 -m scripts.clean_general_ledger

import:
	rm local_ledger.csv
	python3 -m scripts.import_csv_data

net: import
	python3 -m scripts.plot_net_worth_vs_time

percentages: import
	python3 -m scripts.calculate_percentages

test:
	python3 -m unittest discover tests/core
	python3 -m unittest discover tests/general_ledger
	python3 -m unittest discover tests/utilities
