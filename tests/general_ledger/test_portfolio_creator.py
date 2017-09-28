import unittest

from general_ledger.portfolio_creator import PortfolioCreator

class PortfolioCreatorTestCase(unittest.TestCase):

    def setUp(self):
        self.portfolio = PortfolioCreator("tests/test_files/test_ledger.csv").create()

    def test_it_creates_a_portfolio_with_the_correct_percentages(self):
        self.assertEqual(self.portfolio.percentages(), {"CASHX": 0.8, "CASH": 0.2})

    def test_it_creates_a_portfolio_with_the_correct_total_value(self):
        self.assertEqual(self.portfolio.total_value(), 170)

if __name__ == '__main__':
    unittest.main()
