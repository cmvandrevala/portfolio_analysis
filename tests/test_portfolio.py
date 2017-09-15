import unittest
import time

from finance.asset import Asset
from finance.portfolio import Portfolio

class PortfolioTestCase(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_it_starts_off_with_no_assets(self):
        self.assertEqual(self.portfolio.percentages(), {})

    def test_it_adds_an_asset(self):
        asset = Asset("PG")
        asset.import_snapshot(time.time(), 1043.15)
        self.portfolio.import_asset(asset)
        self.assertEqual(self.portfolio.percentages(), {"PG": 1.0})

    def test_it_adds_two_assets_in_equal_amounts(self):
        asset1 = Asset("JJ")
        asset1.import_snapshot(time.time(), 100)
        asset2 = Asset("MCD")
        asset2.import_snapshot(time.time(), 100)
        self.portfolio.import_asset(asset1)
        self.portfolio.import_asset(asset2)
        self.assertEqual(self.portfolio.percentages(), {"JJ": 0.5, "MCD": 0.5})

    def test_it_adds_two_assets_in_different_amounts(self):
        asset1 = Asset("AAPL")
        asset1.import_snapshot(time.time(), 1000.50)
        asset2 = Asset("BSX")
        asset2.import_snapshot(time.time(), 100)
        self.portfolio.import_asset(asset1)
        self.portfolio.import_asset(asset2)
        self.assertEqual(self.portfolio.percentages(), {"AAPL": 0.909, "BSX": 0.091})

    def test_it_does_not_ignore_a_single_zero_dollar_amount(self):
        asset = Asset("T")
        self.portfolio.import_asset(asset)
        self.assertEqual(self.portfolio.percentages(), {"T": 0})

    def test_it_does_not_ignore_a_zero_dollar_amount_mixed_with_other_amounts(self):
        asset1 = Asset("VZ")
        asset1.import_snapshot(time.time(), 0.0)
        asset2 = Asset("SP")
        asset2.import_snapshot(time.time(), 12.54)
        self.portfolio.import_asset(asset1)
        self.portfolio.import_asset(asset2)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0, "SP": 1.0})

if __name__ == '__main__':
    unittest.main()
