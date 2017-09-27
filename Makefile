clean:
	rm -rf */*.pyc */__pycache__ *.csv

net:
	python3 -m scripts.plot_net_worth_vs_time

percentages:
	python3 -m scripts.calculate_percentages

test:
	python3 -m unittest discover tests/finance
	python3 -m unittest discover tests/general_ledger
