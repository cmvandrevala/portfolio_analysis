from functools import reduce
from collections import defaultdict

class Portfolio:

    def __init__(self):
        self.assets = defaultdict(int)

    def addAsset(self, asset, dollarAmount):
        if dollarAmount >= 0: self.assets[asset] += dollarAmount

    def percentages(self):
        return {k: self.__percentOfPortfolio(v) for k, v in self.assets.items()}

    def __percentOfPortfolio(self, dollarAmount):
        return self.__formatedPercent(dollarAmount) if self.__totalDollarAmount() > 0 else 0

    def __formatedPercent(self, dollarAmount):
        return round(dollarAmount/self.__totalDollarAmount(), 3)

    def __totalDollarAmount(self):
        return reduce((lambda x, y: x + y), self.assets.values())
