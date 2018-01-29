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
            .set_update_frequency(3) \
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
        balance_sheet_row = BalanceSheet().row(self.asset)
        self.assertEqual(balance_sheet_row, [expected_date, "institution", "name", "investment", "owner", "100"])

    def test_it_colors_the_date_red_if_it_is_in_the_future(self):
        date_difference = Constants.SECONDS_PER_DAY*91
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp + date_difference)
        self.asset.import_snapshot(timestamp + date_difference, 100)
        balance_sheet_row = BalanceSheet().row(self.asset)
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])

    def test_it_colors_the_date_red_if_it_is_over_7_days_in_the_past_with_no_set_update_frequency(self):
        date_difference = Constants.SECONDS_PER_DAY*8
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.liability.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().row(self.liability)
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])

    def test_it_colors_the_date_red_if_it_is_older_than_the_update_frequency(self):
        date_difference = Constants.SECONDS_PER_DAY*4
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.asset.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = BalanceSheet().row(self.asset)
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "institution","name","investment","owner","0"])


if __name__ == '__main__':
    unittest.main()
