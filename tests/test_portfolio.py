import unittest
import time

from finance.asset import Asset
from finance.portfolio import Portfolio

class PortfolioTestCase(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_it_starts_off_with_no_assets_or_liabilities(self):
        self.assertEqual(self.portfolio.total_value(), 0)

    def test_it_starts_off_no_percentages(self):
        self.assertEqual(self.portfolio.percentages(), {})

    def test_it_imports_asset_data_for_a_new_asset(self):
        assetData = {"date": "2017-06-01", "name": "PG", "value": 1000}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"PG": 1.0})

    def test_it_imports_liability_data_for_a_new_liability(self):
        liabilityData = {"date": "2017-06-01", "name": "Visa Card", "value": 1000}
        self.portfolio.import_liability_data(liabilityData)
        self.assertEqual(self.portfolio.total_value(), -1000)

    def test_it_imports_data_for_two_new_assets(self):
        assetData = {"date": "2017-05-01", "name": "VZ", "value": 5000}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-06-08", "name": "KO", "value": 5000}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"KO": 0.5, "VZ": 0.5})

    def test_it_imports_data_for_two_new_liabilities(self):
        liabilityData = {"date": "2017-05-01", "name": "loan1", "value": 5000}
        self.portfolio.import_liability_data(liabilityData)
        liabilityData = {"date": "2017-06-08", "name": "loan2", "value": 5000}
        self.portfolio.import_liability_data(liabilityData)
        self.assertEqual(self.portfolio.total_value(), -10000)

    def test_it_imports_asset_data_for_two_new_assets_in_different_amounts(self):
        assetData = {"date": "2017-05-01", "name": "AAPL", "value": 2000}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-06-08", "name": "BSX", "value": 8000}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"AAPL": 0.2, "BSX": 0.8})

    def test_it_imports_asset_data_for_an_existing_asset(self):
        assetData = {"date": "2017-05-01", "name": "VZ", "value": 5000}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-05-02", "name": "VZ", "value": 2000}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 1.0})

    def test_it_imports_asset_data_for_existing_and_new_assets(self):
        assetData = {"date": "2017-06-01", "name": "VZ", "value": 3000}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-06-30", "name": "PEP", "value": 4000}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-06-17", "name": "VZ", "value": 6000}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0.6, "PEP": 0.4})

    def test_it_does_not_ignore_a_single_zero_dollar_amount(self):
        assetData = {"date": "2012-01-01", "name": "T", "value": 0}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"T": 0})

    def test_it_does_not_ignore_a_zero_dollar_amount_mixed_with_other_amounts(self):
        assetData = {"date": "2011-02-08", "name": "VZ", "value": 0}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2011-02-08", "name": "SP", "value": 12.54}
        self.portfolio.import_asset_data(assetData)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0, "SP": 1.0})

    def test_it_gives_the_total_value_of_the_portfolio_at_the_current_time(self):
        assetData = {"date": "2011-02-08", "name": "VZ", "value": 100}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2011-02-08", "name": "SP", "value": 12.50}
        self.portfolio.import_asset_data(assetData)
        liabilityData = {"date": "2011-04-05", "name": "loan", "value": 93.10}
        self.portfolio.import_liability_data(liabilityData)
        self.assertEqual(self.portfolio.total_value(), 19.40)

    def test_it_gives_the_total_value_of_the_portfolio_at_a_previous_time(self):
        assetData = {"date": "2017-01-01", "name": "VZ", "value": 100}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-06-01", "name": "SP", "value": 12.50}
        self.portfolio.import_asset_data(assetData)
        liabilityData = {"date": "2017-02-01", "name": "loan", "value": 50}
        self.portfolio.import_liability_data(liabilityData)
        self.assertEqual(self.portfolio.total_value("2017-03-01"), 50)

    def test_it_does_not_include_liabilities_in_percentages(self):
        assetData = {"date": "2017-01-01", "name": "VZ", "value": 100}
        self.portfolio.import_asset_data(assetData)
        assetData = {"date": "2017-06-01", "name": "SP", "value": 12.50}
        self.portfolio.import_asset_data(assetData)
        liabilityData = {"date": "2017-02-01", "name": "loan", "value": 50}
        self.portfolio.import_liability_data(liabilityData)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0.889, "SP": 0.111})

if __name__ == '__main__':
    unittest.main()
