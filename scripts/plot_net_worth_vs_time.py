from pylab import plot, xlabel, ylabel, title, show

from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from report.line_graph import LineGraph
from utilities.epoch_date_converter import EpochDateConverter

portfolio = PortfolioCreator().create(DataSource())
data = LineGraph(portfolio).net_worth_vs_time("2003-01-01", EpochDateConverter().epoch_to_date())

plot(data["times"], data["values"])
xlabel('Date')
ylabel("Owner's Equity")
title("Owner's Equity vs. Time")
show()
