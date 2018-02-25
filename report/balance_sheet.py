from portfolio.portfolio import Portfolio


class BalanceSheet:

    def __init__(self, portfolio=Portfolio()):
        self.portfolio = portfolio
        self.headers = ["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"]
        self.spacers = ["---", "---", "---", "---", "---", "---"]

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