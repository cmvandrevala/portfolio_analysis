import unittest
import json

from portfolio_creator.portfolio_creator import PortfolioCreator


class MockDataSource:
    def __init__(self):
        pass

    def get(self):
        return json.dumps([{"timestamp": "2017-01-02",
                            "institution": "John's Union",
                            "description": "Checking",
                            "owner": "Robert",
                            "symbol": "CASHX",
                            "asset_or_liability": "ASSET",
                            "value": 980.66,
                            "asset_class": "Cash Equivalents"},
                           {"timestamp": "2017-10-25",
                            "institution": "Bob's Bank",
                            "description": "Credit Card",
                            "owner": "John",
                            "symbol": "CASHX",
                            "asset_or_liability": "LIABILITY",
                            "value": 1000.00,
                            "asset_class": "None"}])


class PortfolioCreatorTestCase(unittest.TestCase):
    def setUp(self):
        self.creator = PortfolioCreator()

    def test_it_creates_a_portfolio(self):
        portfolio = self.creator.create(MockDataSource())
        self.assertEqual(portfolio.total_value(), -19.34)
        self.assertEqual(portfolio.percentages(), {"CASHX": 1.0})


if __name__ == '__main__':
    unittest.main()
