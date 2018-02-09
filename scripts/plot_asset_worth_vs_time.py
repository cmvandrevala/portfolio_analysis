import datetime

from pylab import plot, xlabel, ylabel, title, show

from portfolio.account_builder import AccountBuilder
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass

portfolio = PortfolioCreator().create(DataSource())
separator = "=>"
default_start_date = "2018-01-01"

institution = "Charles Schwab"
name = "Brokerage"
owner = "Cyrus"
investment = "Johnson and Johnson"
account_type = AccountType.ASSET
asset_class = AssetClass.EQUITIES
open_date = None

test_account = AccountBuilder().set_name(name) \
    .set_institution(institution) \
    .set_owner(owner) \
    .set_investment(investment) \
    .set_asset_class(asset_class) \
    .set_account_type(account_type) \
    .set_update_frequency(90) \
    .set_open_date(open_date)\
    .build()

account = None

for a in portfolio.accounts:
    if a.is_identical_to(test_account):
        account = a

if account is None:
    print("No account found")
    exit(1)

if account.open_date is None:
    snapshots = account.history.snapshots
    start_epoch = snapshots[0].timestamp
else:
    start_epoch = EpochDateConverter().date_to_epoch(account.open_date)
end_epoch = EpochDateConverter().date_to_epoch()
number_of_seconds = end_epoch - start_epoch
number_of_days = int(number_of_seconds / Constants.SECONDS_PER_DAY)

times = []
owners_equity = []

for day in range(0, number_of_days):
    historical_time = EpochDateConverter().date_to_epoch() - day * Constants.SECONDS_PER_DAY
    times.append(datetime.datetime.fromtimestamp(historical_time))
    owners_equity.append(account.value(historical_time))

plot(times, owners_equity)

times = []
owners_equity = []

for snapshot in account.history.snapshots:
    times.append(datetime.datetime.fromtimestamp(snapshot.timestamp))
    owners_equity.append(snapshot.value)

plot(times, owners_equity, 'o')

times = []
owners_equity = []

if account.open_date is not None:
    times.append(datetime.datetime.fromtimestamp(EpochDateConverter().date_to_epoch(account.open_date)))
    owners_equity.append(0)

plot(times, owners_equity, 'x')

xlabel('Date')
ylabel("Value")
title("Value of " + institution + separator + name + separator + investment + " vs. Time")
show()
