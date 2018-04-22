from portfolio.portfolio import Portfolio


class BalanceSheet:

    def __init__(self, portfolio=Portfolio()):
        self.portfolio = portfolio
        self.headers = ["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"]
        self.spacers = ["---", "---", "---", "---", "---", "---"]

    def json(self):
        assets = []
        liabilities = []
        for asset in self.portfolio.assets():
            assets.append(self.json_object(asset))
        for liability in self.portfolio.liabilities():
            liabilities.append(self.json_object(liability))
        return {"assets": assets, "liabilities": liabilities}

    def create(self):
        data = []
        for asset in self.portfolio.assets():
            data.append(self.row(asset))
        data.append(self.spacers)
        for liability in self.portfolio.liabilities():
            data.append(self.row(liability))
        data.append(["", "", "", "", "Total", '%.2f' % self.portfolio.total_value()])
        return data

    def row(self, account):
        return [account.last_updated(), account.institution(), account.name(), account.investment(), account.owner(),
                '%.2f' % account.value()]

    def json_object(self, account):
        return { "lastUpdated": account.last_updated() + "T12:00:00-05:00",
                 "institution": account.institution(),
                 "account": account.name(),
                 "investment": account.investment(),
                 "owner": account.owner(),
                 "value": account.value()
                }
