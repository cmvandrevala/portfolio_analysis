# Finance Scripts

## Background

I love learning about finance and economics and have written a number of small, "toy-box" scripts over the years. Most of these are quick and dirty experiments driven by my own curiosity. Unfortunately, these scripts have started to become disorganized and contain quite a bit of repetition.

The main goal of this project is to organize and refine the aforementioned software. This will involve refactoring scripts, extracting duplicate logic into classes, adding tests, etc. Hopefully, this will allow me to write more sophisticated software in the future.

### Disclaimer

I am in no way, shape, or form a financial professional. I am not qualified to offer any financial advice. These scripts work for me in organizing my finances, but they might not work for you. This software is licensed under the MIT license.

## Setup

This project uses Python 3.6 and [pipenv](https://github.com/pypa/pipenv) to manage packages and the workspace. First, make sure that `pipenv` is installed on your system using:

```python
pip install pipenv
```

After you clone this repo, you can install of the project dependencies using:

```python
pipenv install
```

To activate the virtual environment for the project, you can use:

```python
pipenv shell
```

### General Ledger

This project pulls portfolio data from a general ledger server. Refer to [this](https://github.com/cmvandrevala/general_ledger) project for more details about the server and endpoints. You can set the url and port by updating `Constants.LEDGERS_DIRECTORY` in `utilities/constants.py`


### A Note About Matplotlib

If you are using `pipenv` on OSX, you might notice an error complaining that Python has not been installed as a framework:

```bazaar
RuntimeError: Python is not installed as a framework. The Mac OS X backend 
will not be able to function correctly if Python is not installed as a 
framework. See the Python documentation for more information on installing 
Python as a framework on Mac OS X. Please either reinstall Python as a 
framework, or try one of the other backends. If you are using (Ana)Conda 
please install python.app and replace the use of 'python' with 'pythonw'. 
See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more 
information.
```

This might be due to the fact that OSX has a different image-rendering backend for Matplotlib than other operating systems. To fix this problem, create a new file called `~/.matplotlib/matplotlibrc` and add the following line of code:

```python
backend: TkAgg
```

## Testing

Tests are written using the `unittest` framework. The test suite can be run using the following command:

```
make test
```

## Running the Scripts

There are a number of Python scripts located in the `scripts/` directory. Each one is associated with a make task.

* `make asset` -> Plot the net worth of an asset or liability versus time
* `make balance` -> Create a balance sheet with data from
* `make classes` -> Plot asset classes of portfolio
* `make de` -> Plot the debt to equity ratio of the portfolio versus time
* `make mypy` -> Run mypy on each file of the project
* `make net` -> Plot owner's equity versus time
* `make percentages` -> Generate percentages for use in Portfolio Visualizer
* `make recommend` -> Recommend an investment for a future purchase or payment
* `make test` -> Run the test suite
