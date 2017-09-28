import csv

from general_ledger.portfolio_creator import PortfolioCreator

portfolio = PortfolioCreator("tests/test_files/test_ledger.csv").create()

with open('percentages.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Symbol', 'Weight'])
    for symbol, percentage in portfolio.percentages().items():
        writer.writerow([symbol, str(100*percentage) + "%"])