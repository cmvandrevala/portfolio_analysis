# Finance Scripts

This repo contains a set of Python scripts that I use in organizing my finances.

## Prerequisites

* Python 3
* Pylab

### General Ledger

The Python scripts pull data from a general, running ledger which is formatted as a CSV file. The ledger has the following columns (in order):

* Date: Formatted as year-month-day
* Name: The name of the asset or liability
* Owner: The owner of the asset or liability
* Value: The value of the asset or liability on the given day
* Classification: Can take the values of "asset" or "liability"

For example:

```
Date,Name,Owner,Value,Classification
2017-01-01,GE,Cyrus,1000.12,asset
2017-02-03,FB,Charles,12.34,asset
2017-03-04,Loan,Bob,100.50,liability
```

## Testing

Tests are written using the `unittest` framework. The test suite can be run using the following command:

```
make test
```

## Running the Scripts

All of the scripts are located in the `scripts/` directory and are associated with a make task.

* `make net` -> Plot owner's equity versus time
