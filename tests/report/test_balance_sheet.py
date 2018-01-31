import unittest

from portfolio.account_builder import AccountBuilder
from portfolio.portfolio import Portfolio
from report.balance_sheet import BalanceSheet
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter


class BalanceSheetTestCase(unittest.TestCase):
    def setUp(self):
        self.asset = AccountBuilder().set_name("name") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_institution("institution") \
            .set_update_frequency(3) \
            .build()
        self.liability = AccountBuilder().set_name("name") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_institution("institution") \
            .set_liability() \
            .build()
        self.portfolio = Portfolio()

    def test_it_returns_a_formatted_row_for_a_balance_sheet(self):
        date_difference = Constants.SECONDS_PER_DAY * 2
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 100)
        balance_sheet_row = BalanceSheet().row(self.asset)
        self.assertEqual(balance_sheet_row, [expected_date, "institution", "name", "investment", "owner", "100.00"])

    def test_it_colors_the_date_red_if_it_is_in_the_future(self):
        date_difference = Constants.SECONDS_PER_DAY * 91
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp + date_difference)
        self.asset.import_snapshot(timestamp + date_difference, 100)
        balance_sheet_row = BalanceSheet().row(self.asset)
        self.assertEqual(balance_sheet_row,
                         ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution", "name", "investment", "owner",
                          "0.00"])

    def test_it_colors_the_date_red_if_it_is_over_7_days_in_the_past_with_no_set_update_frequency(self):
        date_difference = Constants.SECONDS_PER_DAY * 8
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.liability.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().row(self.liability)
        self.assertEqual(balance_sheet_row,
                         ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution", "name", "investment", "owner",
                          "0.00"])

    def test_it_colors_the_date_red_if_it_is_older_than_the_update_frequency(self):
        date_difference = Constants.SECONDS_PER_DAY * 4
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().row(self.asset)
        self.assertEqual(balance_sheet_row,
                         ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution", "name", "investment", "owner",
                          "0.00"])

    def test_it_returns_an_empty_balance_sheet_if_there_are_no_accounts_in_the_portfolio(self):
        balance_sheet = BalanceSheet(self.portfolio)
        expected_output = [["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"],
                           ["---", "---", "---", "---", "---", "---"],
                           ["", "", "", "", "Total", "0.00"]]
        self.assertEqual(balance_sheet.create(), expected_output)

    def test_it_returns_a_balance_sheet_with_one_asset(self):
        self.asset.import_snapshot(EpochTimestampConverter().epoch('2017-12-12'), 100)
        self.portfolio.import_account(self.asset)
        balance_sheet = BalanceSheet(self.portfolio)
        expected_output = [["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"],
                           ["\x1b[1;31;40m2017-12-12\x1b[0m", "institution", "name", "investment", "owner", "100.00"],
                           ["---", "---", "---", "---", "---", "---"],
                           ["", "", "", "", "Total", "100.00"]]
        self.assertEqual(balance_sheet.create(), expected_output)

    def test_it_returns_a_balance_sheet_with_one_liability(self):
        self.liability.import_snapshot(EpochTimestampConverter().epoch('2011-1-1'), 500.12)
        self.portfolio.import_account(self.liability)
        balance_sheet = BalanceSheet(self.portfolio)
        expected_output = [["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"],
                           ["---", "---", "---", "---", "---", "---"],
                           ["\x1b[1;31;40m2011-01-01\x1b[0m", "institution", "name", "investment", "owner", "500.12"],
                           ["", "", "", "", "Total", "-500.12"]]
        self.assertEqual(balance_sheet.create(), expected_output)

    def test_it_returns_a_balance_sheet_with_an_asset_and_a_liability(self):
        self.asset.import_snapshot(EpochTimestampConverter().epoch('2017-11-12'), 1020)
        self.liability.import_snapshot(EpochTimestampConverter().epoch('2013-5-5'), 0.12)
        self.portfolio.import_account(self.asset)
        self.portfolio.import_account(self.liability)
        balance_sheet = BalanceSheet(self.portfolio)
        expected_output = [["Last Updated", "Institution", "Account", "Investment", "Owner", "Value"],
                           ["\x1b[1;31;40m2017-11-12\x1b[0m", "institution", "name", "investment", "owner", "1020.00"],
                           ["---", "---", "---", "---", "---", "---"],
                           ["\x1b[1;31;40m2013-05-05\x1b[0m", "institution", "name", "investment", "owner", "0.12"],
                           ["", "", "", "", "Total", "1019.88"]]
        self.assertEqual(balance_sheet.create(), expected_output)


if __name__ == '__main__':
    unittest.main()
