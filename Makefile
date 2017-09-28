clean:
	python3 -m scripts.clean_general_ledger

import: clean
	python3 -m scripts.import_csv_data

net: clean
	python3 -m scripts.plot_net_worth_vs_time

percentages: clean
	python3 -m scripts.calculate_percentages

test:
	python3 -m unittest discover tests/finance
	python3 -m unittest discover tests/general_ledger
	python3 -m unittest discover tests/utilities
