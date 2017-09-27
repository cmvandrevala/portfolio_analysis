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
        if row[4] == "asset":
            portfolio.import_asset_data({"name": row[1], "date": row[0], "value": float(row[3])})
        else:
            portfolio.import_liability_data({"name": row[1], "date": row[0], "value": float(row[3])})

times = []
owners_equity = []

for day in range (0, number_of_days):
    historical_time = current_time - day*seconds_per_day
    formatted_date = datetime.datetime.fromtimestamp(historical_time).strftime('%Y-%m-%d')
    times.append(datetime.datetime.fromtimestamp(historical_time))
    owners_equity.append(portfolio.total_value(formatted_date))

plot(times, owners_equity)
xlabel('Date')
ylabel("Owner's Equity")
title("Owner's Equity vs. Time")
show()
