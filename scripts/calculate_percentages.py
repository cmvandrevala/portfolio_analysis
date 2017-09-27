from general_ledger.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator("tests/test_files/test_ledger.csv").create()

print(portfolio.percentages())
