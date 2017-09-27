# Finance Scripts

This repo contains a set of Python scripts that I use in organizing my finances.

## Prerequisites

* Python 3
* Pylab

### General Ledger

The Python scripts pull data from a general, running ledger which is formatted as a CSV file. The ledger has the following columns (in order):

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

## Testing

Tests are written using the `unittest` framework. The test suite can be run using the following command:

```
make test
```

## Running the Scripts

All of the scripts are located in the `scripts/` directory and are associated with a make task.

* `make net` -> Plot owner's equity versus time
* `make percentages` -> Generate percentages for use in Portfolio Visualizer
