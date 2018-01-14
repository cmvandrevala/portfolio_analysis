from portfolio.account_builder import AccountBuilder
from portfolio_analysis.account_recommender import AccountRecommender
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator().create(DataSource())
default_account = AccountBuilder().set_name("Slush Fund")\
    .set_owner("Family")\
    .set_institution("Home")\
    .set_investment("Slush Fund")\
    .build()

account = AccountRecommender().recommend(portfolio, default_account)

print("~~~~~~~~~~~~~~~~~~~~~~~~")

print(account.institution)
print(account.name)
print(account.owner)

print("~~~~~~~~~~~~~~~~~~~~~~~~")
