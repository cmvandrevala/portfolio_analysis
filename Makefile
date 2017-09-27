clean:
	rm -rf */*.pyc */__pycache__ *.csv

net:
	python3 -m scripts.plot_net_worth_vs_time.py

test:
	python3 -m unittest discover tests
