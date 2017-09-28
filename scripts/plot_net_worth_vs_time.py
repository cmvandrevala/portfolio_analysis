import datetime
import time

from utilities.constants import Constants
from pylab import *

from general_ledger.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator(Constants.GENERAL_LEDGER_PATH).create()
current_time = time.time()
number_of_days = 1000

times = []
owners_equity = []

for day in range (0, number_of_days):
    historical_time = current_time - day*Constants.SECONDS_PER_DAY
    formatted_date = datetime.datetime.fromtimestamp(historical_time).strftime('%Y-%m-%d')
    times.append(datetime.datetime.fromtimestamp(historical_time))
    owners_equity.append(portfolio.total_value(formatted_date))

plot(times, owners_equity)
xlabel('Date')
ylabel("Owner's Equity")
title("Owner's Equity vs. Time")
show()
