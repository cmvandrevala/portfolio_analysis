import json

from portfolio.portfolio import Portfolio


class PortfolioCreator:
    def __init__(self):
        self.portfolio = Portfolio()

    def create(self, data_source):
        data = data_source.get()
        snapshots = json.loads(data)
        for item in snapshots["snapshots"]:
            if item["asset"]:
                account_type = "ASSET"
            else:
                account_type = "LIABILITY"
            self.portfolio.import_data({"date": item["timestamp"],
                                        "institution": item["institution"],
                                        "name": item["account"],
                                        "owner": item["owner"],
                                        "symbol": item["investment"],
                                        "account_type": account_type,
                                        "value": float(item["value"])/100,
                                        "asset_class": "Cash Equivalents"})
        return self.portfolio
