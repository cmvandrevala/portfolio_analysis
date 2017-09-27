import csv
import datetime
import time
from pylab import *

from finance.portfolio import Portfolio

portfolio = Portfolio()
current_time = time.time()
number_of_days = 1000
seconds_per_day = 24*60*60

with open('test_ledger.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if row[5] == "ASSET":
            portfolio.import_asset_data({"name": row[2], "date": row[0], "value": float(row[6])})
        else:
            portfolio.import_liability_data({"name": row[2], "date": row[0], "value": float(row[6])})

print(portfolio.percentages())
