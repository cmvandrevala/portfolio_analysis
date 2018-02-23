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
                                          "asset_class": "Cash Equivalents",
                                          "update_frequency": 12,
                                          "open_date": None},
                                         {"timestamp": "2017-10-25",
                                          "institution": "Bob's Bank",
                                          "account": "Credit Card",
                                          "owner": "John",
                                          "investment": "CASHX",
                                          "asset": False,
                                          "value": 100000,
                                          "asset_class": "None",
                                          "update_frequency": 22,
                                          "open_date": "2000-11-12",
                                          "term": "medium"},
                                         {"timestamp": "2017-10-26",
                                          "institution": "Sam's Bank",
                                          "account": "Credit Card",
                                          "owner": "John",
                                          "investment": "CASHX",
                                          "asset": False,
                                          "value": 100000,
                                          "update_frequency": 195,
                                          "open_date": "2017-1-1",
                                          "term": None}
                                         ]})


class PortfolioCreatorTestCase(unittest.TestCase):
    def setUp(self):
        self.portfolio = PortfolioCreator().create(MockDataSource())

    def test_it_creates_a_portfolio(self):
        self.assertAlmostEqual(self.portfolio.total_value(), -1019.34)
        self.assertEqual(self.portfolio.percentages(), {"CASHX": 1.0})
        self.assertEqual(self.portfolio.asset_classes(),
                         {'Annuities': 0.0, 'Cash Equivalents': 1.0, 'Commodities': 0.0, 'Equities': 0.0,
                          'Fixed Assets': 0.0, 'Fixed Income': 0.0, 'Real Estate': 0.0})

    def test_it_assigns_the_correct_names_to_the_accounts(self):
        accounts = self.portfolio.accounts
        first_account = accounts[0]
        self.assertEqual(first_account.name(), "Checking")
        second_account = accounts[1]
        self.assertEqual(second_account.name(), "Credit Card")
        third_account = accounts[2]
        self.assertEqual(third_account.name(), "Credit Card")

    def test_it_assigns_the_correct_update_frequencies_to_the_accounts(self):
        accounts = self.portfolio.accounts
        first_account = accounts[0]
        self.assertEqual(first_account.update_frequency(), 12)
        second_account = accounts[1]
        self.assertEqual(second_account.update_frequency(), 22)
        third_account = accounts[2]
        self.assertEqual(third_account.update_frequency(), 195)

    def test_it_assigns_the_correct_open_dates_to_the_accounts(self):
        accounts = self.portfolio.accounts
        first_account = accounts[0]
        self.assertEqual(first_account.open_date(), None)
        second_account = accounts[1]
        self.assertEqual(second_account.open_date(), "2000-11-12")
        third_account = accounts[2]
        self.assertEqual(third_account.open_date(), "2017-1-1")

    def test_it_assigns_the_correct_terms_to_the_accounts(self):
        accounts = self.portfolio.accounts
        first_account = accounts[0]
        self.assertEqual(first_account.term(), "none")
        second_account = accounts[1]
        self.assertEqual(second_account.term(), "medium")
        third_account = accounts[2]
        self.assertEqual(third_account.term(), "none")


if __name__ == '__main__':
    unittest.main()
