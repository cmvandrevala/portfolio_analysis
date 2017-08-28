import unittest
from finance.portfolio import Portfolio

class PortfolioTestCase(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_it_starts_off_with_no_assets(self):
        self.assertEqual(self.portfolio.percentages(), {})

    def test_it_adds_an_asset(self):
        self.portfolio.addAsset("PG", 1043.15)
        self.assertEqual(self.portfolio.percentages(), {"PG": 1.0})

    def test_it_adds_two_assets_in_equal_amounts(self):
        self.portfolio.addAsset("JJ", 100)
        self.portfolio.addAsset("MCD", 100)
        self.assertEqual(self.portfolio.percentages(), {"JJ": 0.5, "MCD": 0.5})

    def test_it_adds_two_assets_in_different_amounts(self):
        self.portfolio.addAsset("AAPL", 1000.5)
        self.portfolio.addAsset("BSX", 100)
        self.assertEqual(self.portfolio.percentages(), {"AAPL": 0.909, "BSX": 0.091})

    def test_it_does_not_create_duplicate_entries(self):
        self.portfolio.addAsset("FB", 100)
        self.portfolio.addAsset("FB", 150)
        self.portfolio.addAsset("GOOG", 500)
        self.assertEqual(self.portfolio.percentages(), {"FB": 0.333, "GOOG": 0.667})

    def test_it_does_not_create_duplicate_entries(self):
        self.portfolio.addAsset("FB", 100)
        self.portfolio.addAsset("FB", 150)
        self.portfolio.addAsset("GOOG", 500)
        self.assertEqual(self.portfolio.percentages(), {"FB": 0.333, "GOOG": 0.667})

    def test_it_ignores_a_negative_dollar_amount(self):
        self.portfolio.addAsset("GE", -10.5)
        self.assertEqual(self.portfolio.percentages(), {})

    def test_it_does_not_ignore_a_single_zero_dollar_amount(self):
        self.portfolio.addAsset("T", 0.0)
        self.assertEqual(self.portfolio.percentages(), {"T": 0})

    def test_it_does_not_ignore_a_zero_dollar_amount_mixed_with_other_amounts(self):
        self.portfolio.addAsset("VZ", 0.0)
        self.portfolio.addAsset("SP", 12.54)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0, "SP": 1.0})

if __name__ == '__main__':
    unittest.main()
