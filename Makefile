clean:
	rm -rf */*.pyc */__pycache__ *.csv

test:
	python3 -m unittest discover tests
