from utilities.epoch_timestamp_converter import EpochTimestampConverter
from utilities.constants import Constants
from pylab import *

from general_ledger.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator(Constants.LOCAL_LEDGER_PATH).create()
number_of_days = Constants.DAYS_PER_YEAR*15

times = []
owners_equity = []

for day in range (0, number_of_days):
    historical_time = EpochTimestampConverter().epoch() - day*Constants.SECONDS_PER_DAY
    formatted_date = EpochTimestampConverter().timestamp(historical_time)
    times.append(datetime.datetime.fromtimestamp(historical_time))
    owners_equity.append(portfolio.total_value(formatted_date))

plot(times, owners_equity)
xlabel('Date')
ylabel("Owner's Equity")
title("Owner's Equity vs. Time")
show()
