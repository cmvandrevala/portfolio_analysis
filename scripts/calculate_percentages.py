from general_ledger.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator("test_ledger.csv").create()

print(portfolio.percentages())
