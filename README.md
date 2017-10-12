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

* Date: Formatted as year-month-day
* Institution: Where is the asset or liability held
* Name: The name of the asset or liability
* Owner: The owner of the asset or liability
* Symbol: What is the ticker symbol of the asset or liability
* Classification: Can take the values of "ASSET" or "LIABILITY"
* Value: The value of the asset or liability on the given day

For example:

```
Date,Institution,Name,Owner,Symbol,Classification,Value
2017-05-01,Bobs Bank,Checking_Cyrus,Cyrus,CASHX,ASSET,600
2017-06-07,Sams Bank,Checking_Stephen,Stephen,CASHX,ASSET,500
2017-07-08,Eusavios Loans,Mary_Loan,Mary,CASHX,LIABILITY,400
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
* `make clean` -> Remove duplicate entries from the general ledger
* `make import` -> Import finance data into a general ledger
* `make net` -> Plot owner's equity versus time
* `make percentages` -> Generate percentages for use in Portfolio Visualizer

Note that there is no `make append` command since this requires command line arguments. For now, you can run this script using:

```
python3 -m scripts.append <name of CSV file without extension> <value> <optional date>
```

In the future, I will add a command line task for this command or come up with a prettier solution.
