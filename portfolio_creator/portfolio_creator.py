import json

from portfolio.portfolio import Portfolio

class PortfolioCreator:

    def create(self, data_source):
        portfolio = Portfolio()
        data = data_source.get()
        snapshots = json.loads(data)
        for item in snapshots["snapshots"]:
            portfolio.import_data({"timestamp": item["timestamp"],
                                   "institution": item["institution"],
                                   "name": item["account"],
                                   "owner": item["owner"],
                                   "investment": item["investment"],
                                   "update_frequency": item["update_frequency"],
                                   "account_type": self.__account_type(item),
                                   "value": self.__value(item),
                                   "asset_class": self.__asset_class(item),
                                   "open_date": item["open_date"],
                                   "term": self.__term(item)})
        return portfolio

    def __account_type(self, account):
        return "ASSET" if account["asset"] else "LIABILITY"

    def __value(self, account):
        return float(account["value"])/100

    def __asset_class(self, account):
        return account.get("asset_class", "None")

    def __term(self, account):
        return account["term"] or "none"
