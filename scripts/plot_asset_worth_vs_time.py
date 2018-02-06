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
number_of_days = Constants.DAYS_PER_YEAR * 5
separator = "=>"

institution = "Charles Schwab"
name = "Brokerage"
owner = "Annamarie"
investment = "Bank of America"
account_type = AccountType.ASSET
asset_class = AssetClass.EQUITIES

test_account = AccountBuilder().set_name(name) \
    .set_institution(institution) \
    .set_owner(owner) \
    .set_investment(investment) \
    .set_asset_class(asset_class) \
    .set_account_type(account_type) \
    .set_update_frequency(90) \
    .build()

account = None

for a in portfolio.accounts:
    if a.is_identical_to(test_account):
        account = a

if account is None:
    print("No account found")
    exit(1)

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

xlabel('Date')
ylabel("Value")
title("Value of " + institution + separator + name + separator + investment + " vs. Time")
show()
