import unittest
import json

from portfolio_creator.portfolio_creator import PortfolioCreator


class MockDataSource:
    def __init__(self):
        pass

    def get(self):
        return json.dumps({"snapshots": [{"timestamp": "2017-01-02",
                            "institution": "John's Union",
                            "account": "Checking",
                            "owner": "Robert",
                            "investment": "CASHX",
                            "asset": True,
                            "value": 98066},
                           {"timestamp": "2017-10-25",
                            "institution": "Bob's Bank",
                            "account": "Credit Card",
                            "owner": "John",
                            "investment": "CASHX",
                            "asset": False,
                            "value": 100000,
                            "asset_class": "None"}]})


class PortfolioCreatorTestCase(unittest.TestCase):
    def setUp(self):
        self.creator = PortfolioCreator()

    def test_it_creates_a_portfolio(self):
        portfolio = self.creator.create(MockDataSource())
        self.assertEqual(portfolio.total_value(), -19.34)
        self.assertEqual(portfolio.percentages(), {"CASHX": 1.0})


if __name__ == '__main__':
    unittest.main()
