import math


class PortfolioAnalyzer:

    def __init__(self, portfolio):
        self.__portfolio = portfolio

    def debt_to_equity(self, date=None):
        if self.__portfolio.total_value(date) == 0:
            return math.inf
        else:
            return abs(self.__portfolio.liabilities_value(date) / self.__portfolio.total_value(date))
