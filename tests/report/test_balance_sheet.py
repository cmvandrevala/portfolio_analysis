import unittest

from portfolio.account_builder import AccountBuilder
from report.balance_sheet import BalanceSheet
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter


class BalanceSheetTestCase(unittest.TestCase):
    def setUp(self):
        self.asset = AccountBuilder().set_name("name") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_institution("institution") \
            .build()
        self.liability = AccountBuilder().set_name("name") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_institution("institution") \
            .set_liability()\
            .build()

    def test_it_returns_a_formatted_row_for_a_balance_sheet(self):
        date_difference = Constants.SECONDS_PER_DAY * 2
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 100)
        balance_sheet_row = BalanceSheet().asset_row(self.asset)
        self.assertEqual(balance_sheet_row, [expected_date, "institution", "name", "investment", "owner", "100"])

    def test_it_colors_the_date_red_if_it_is_in_the_future(self):
        date_difference = Constants.SECONDS_PER_DAY*91
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp + date_difference)
        self.asset.import_snapshot(timestamp + date_difference, 100)
        balance_sheet_row = BalanceSheet().asset_row(self.asset)
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])

    def test_it_colors_the_date_yellow_if_it_is_over_30_days_in_the_past(self):
        date_difference = Constants.SECONDS_PER_DAY*31
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().asset_row(self.asset)
        self.assertEqual(balance_sheet_row, ["\x1b[0;33;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])

    def test_it_colors_the_date_pink_if_it_is_over_60_days_in_the_past(self):
        date_difference = Constants.SECONDS_PER_DAY*61
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().asset_row(self.asset)
        self.assertEqual(balance_sheet_row, ["\x1b[1;35;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])

    def test_it_colors_the_date_red_if_it_is_over_90_days_in_the_past(self):
        date_difference = Constants.SECONDS_PER_DAY*91
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().asset_row(self.asset)
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])

    def test_it_returns_a_row_for_a_liability_less_than_one_week_old(self):
        date_difference = Constants.SECONDS_PER_DAY*2
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.liability.import_snapshot(timestamp - date_difference, 100)
        liabilities_row = BalanceSheet().liabilities_row(self.liability)
        self.assertEqual(liabilities_row, [expected_date, "institution","name","investment","owner","100"])

    def test_it_returns_a_row_for_a_liability_greater_than_one_week_old(self):
        date_difference = Constants.SECONDS_PER_DAY*9
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.liability.import_snapshot(timestamp - date_difference, 100)
        liabilities_row = BalanceSheet().liabilities_row(self.liability)
        self.assertEqual(liabilities_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","100"])


if __name__ == '__main__':
    unittest.main()
