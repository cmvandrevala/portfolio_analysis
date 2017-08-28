import csv

class FileIO:

    def importAssetsToPortfolio(self, filename, portfolio):
        with open(filename) as csvfile:
            for row in csv.reader(csvfile):
                portfolio.addAsset(row[0], float(row[1]))

    def writePortfolioToCsv(self, portfolio):
        with open('portfolio.csv', 'w') as f:
            for k, v in portfolio.percentages().items():
                f.write(f"{k},{v}\n")
