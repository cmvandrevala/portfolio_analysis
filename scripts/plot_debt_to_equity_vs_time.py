import datetime

from portfolio_analysis.portfolio_analyzer import PortfolioAnalyzer
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from pylab import plot, xlabel, ylabel, title, show
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter

portfolio = PortfolioCreator().create(DataSource())
analyzer = PortfolioAnalyzer(portfolio)
number_of_days = round(Constants.DAYS_PER_YEAR * 0.5)

times = []
debt_equity_ratio = []

for day in range(0, number_of_days):
    historical_time = EpochDateConverter().date_to_epoch() - day * Constants.SECONDS_PER_DAY
    formatted_date = EpochDateConverter().epoch_to_date(historical_time)
    times.append(datetime.datetime.fromtimestamp(historical_time))
    debt_equity_ratio.append(analyzer.debt_to_equity(formatted_date))

plot(times, debt_equity_ratio)
xlabel('Date')
ylabel("Debt to Equity Ratio")
title("Debt to Equity Ratio vs. Time")
show()
