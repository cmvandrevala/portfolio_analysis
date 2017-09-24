import time
import csv
import datetime
from pylab import *
from finance.asset import Asset
from finance.portfolio import Portfolio

portfolio = Portfolio()

x = time.time()

first_row = True
with open('test_ledger.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if first_row:
            first_row = False
            continue
        date = row[0]
        name = row[1]
        value = int(row[3])
        portfolio.import_asset_data({"name": name, "date": date, "value": value})

numDays = 1000

times = []
values = []
percentages = []

for date in range (0, numDays):
    foo = x - (date + 1)*60*60*24
    bar = datetime.datetime.fromtimestamp(foo).strftime('%Y-%m-%d')
    times.append(datetime.datetime.fromtimestamp(foo))
    values.append(portfolio.total_value(bar))

plot(times, values)
xlabel('Date')
ylabel("Owner's Equity")
title("Owner's Equity vs. Time")
show()
