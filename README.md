# Finance Scripts

## Background

I love learning about finance and economics and have written a number of small, "toy-box" scripts over the years. Most of these are quick and dirty experiments driven by my own curiosity. As you might guess, these scripts have started to become disorganized and contain quite a bit of repetition.

The main goal of this project is to organize and refine the aforementioned software. This will involve refactoring scripts, extracting duplicate logic into classes, adding tests, etc. Hopefully, this will allow me to write more sophisticated software in the future.

### Disclaimer

I am in no way, shape, or form a financial professional. I am not qualified to offer any financial advice. These scripts work for me in organizing my finances, but they might not work for you.

## Prerequisites

This project uses:

* Python 3.6
* Pylab

Additionally, you need to update `utilities/constants.py` to fit your specific needs.

### General Ledger

The Python scripts pull data from a directory containing a number of CSV files with financial data. Each file has the following columns (in order):

* Timestamp: Formatted as year-month-day
* Institution: Where is the asset or liability held
* Description: The name of the asset or liability
* Owner: The owner of the asset or liability
* Symbol: What is the ticker symbol of the asset or liability
* Account Type: Can take the values of "ASSET" or "LIABILITY"
* Value: The value of the asset or liability on the given day
* Asset Class: The asset class of the account. Liabilities have an asset class of "Cash Equivalents"

For example:

```
Timestamp,Institution,Description,Owner,Symbol,Account Type,Value,Asset Class
2017-05-01,Bobs Bank,Checking_Cyrus,Cyrus,CASHX,ASSET,600,Cash Equivalents
2017-06-07,Sams Bank,Checking_Stephen,Stephen,CASHX,ASSET,500,Cash Equivalents
2017-07-08,Eusavios Loans,Mary_Loan,Mary,CASHX,LIABILITY,400,Cash Equivalents
```

You can set the location of this directory by updating `Constants.LEDGERS_DIRECTORY` in `utilities/constants.py`

## Testing

Tests are written using the `unittest` framework. The test suite can be run using the following command:

```
make test
```

## Running the Scripts

There are a number of Python scripts located in the `scripts/` directory and (most) are associated with a make task.

* `make balance` -> Create a balance sheet with data from
* `make classes` -> Plot asset classes of portfolio
* `make net` -> Plot owner's equity versus time
* `make percentages` -> Generate percentages for use in Portfolio Visualizer

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