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
                                        "symbol": item["investment"],
                                        "account_type": self.__account_type(item),
                                        "value": float(item["value"])/100,
                                        "asset_class": "Cash Equivalents"})
        return portfolio

    def __account_type(self, account):
        return "ASSET" if account["asset"] else "LIABILITY"
