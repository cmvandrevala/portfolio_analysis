import unittest
import json

from portfolio_creator.portfolio_creator import PortfolioCreator


class MockDataSource:

    def get(self):
        return json.dumps({"snapshots": [{"timestamp": "2017-01-02",
                            "institution": "John's Union",
                            "account": "Checking",
                            "owner": "Robert",
                            "investment": "CASHX",
                            "asset": True,
                            "value": 98066,
                            "assetClass": "Cash Equivalents"},
                           {"timestamp": "2017-10-25",
                            "institution": "Bob's Bank",
                            "account": "Credit Card",
                            "owner": "John",
                            "investment": "CASHX",
                            "asset": False,
                            "value": 100000,
                            "assetClass": "None"},
                            {"timestamp": "2017-10-26",
                            "institution": "Bob's Bank",
                            "account": "Credit Card",
                            "owner": "John",
                            "investment": "CASHX",
                            "asset": False,
                            "value": 100000}
                            ]})


class PortfolioCreatorTestCase(unittest.TestCase):

    def test_it_creates_a_portfolio(self):
        portfolio = PortfolioCreator().create(MockDataSource())
        self.assertAlmostEqual(portfolio.total_value(), -19.34)
        self.assertEqual(portfolio.percentages(), {"CASHX": 1.0})
        self.assertEqual(portfolio.asset_classes(), {'Annuities': 0.0, 'Cash Equivalents': 1.0, 'Commodities': 0.0, 'Equities': 0.0, 'Fixed Assets': 0.0, 'Fixed Income': 0.0, 'Real Estate': 0.0})


if __name__ == '__main__':
    unittest.main()
