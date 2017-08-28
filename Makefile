clean:
	rm -rf */*.pyc */__pycache__

test:
	python3 -m unittest discover tests
