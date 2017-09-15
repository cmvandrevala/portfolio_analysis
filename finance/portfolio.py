from functools import reduce
class Portfolio:

    def __init__(self):
        self.assets = []

    def import_asset(self, asset):
        self.assets.append(asset)

    def percentages(self):
        asset_sum = self.__total_portfolio_value()
        return dict((a.name, self.__percentage(a.value(), asset_sum)) for a in self.assets)

    def __total_portfolio_value(self):
        return sum(asset.value() for asset in self.assets)

    def __percentage(self, value, asset_sum):
        return 0 if asset_sum == 0 else round(value / asset_sum, 3)
