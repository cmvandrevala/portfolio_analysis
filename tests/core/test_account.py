import unittest

from core.account import Account
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass


class AssetTestCase(unittest.TestCase):

    def setUp(self):
        self.account = Account("account name", "Bob Bobberson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", AccountType.ASSET)
        self.liability = Account("account name", "Bob Bobberson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", AccountType.LIABILITY)

    def test_it_has_a_name(self):
        self.assertEqual(self.account.name, "account name")

    def test_it_has_an_owner(self):
        self.assertEqual(self.account.owner, "Bob Bobberson")

    def test_it_has_a_symbol(self):
        self.assertEqual(self.account.symbol, "SYMBOL")

    def test_it_has_an_asset_class(self):
        self.assertEqual(self.account.asset_class(), "Cash Equivalents")

    def test_it_throws_an_exception_if_a_string_is_passed_in_for_asset_class(self):
        invalid_account = Account("account name", "Bob Bobberson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", "RANDOM")
        self.assertRaises(AttributeError, invalid_account.account_type)

    def test_it_has_an_institution(self):
        self.assertEqual(self.account.institution, "Rachel's Bank")

    def test_it_has_an_account_type(self):
        self.assertEqual(self.account.account_type(), AccountType.ASSET.value)

    def test_it_throws_an_exception_if_a_string_is_passed_in_for_an_account_type(self):
        invalid_account = Account("account name", "Bob Bobberson", "SYMBOL", "Cash Equivalents", "Rachel's Bank", "RANDOM")
        self.assertRaises(AttributeError, invalid_account.account_type)

    def test_it_has_a_value_of_zero_if_there_are_no_snapshots(self):
        value = self.account.value()
        self.assertEqual(value, 0)

    def test_it_returns_an_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = EpochTimestampConverter().epoch()
        query_time = timestamp - 20
        self.account.import_snapshot(timestamp, 100)
        value = self.account.value(query_time)
        self.assertEqual(value, 0)

    def test_it_returns_the_correct_value_when_queried_after_a_snapshot(self):
        timestamp = EpochTimestampConverter().epoch()
        query_time = timestamp + 20
        self.account.import_snapshot(timestamp, 100)
        value = self.account.value(query_time)
        self.assertEqual(value, 100)

    def test_it_returns_the_correct_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = EpochTimestampConverter().epoch()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2
        self.account.import_snapshot(earlier_timestamp, 300)
        self.account.import_snapshot(later_timestamp, 250)
        value = self.account.value(query_time)
        self.assertEqual(value, 300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = EpochTimestampConverter().epoch()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2
        query_time = timestamp1 + 1
        self.account.import_snapshot(timestamp2, 20)
        self.account.import_snapshot(timestamp1, 10)
        self.account.import_snapshot(timestamp3, 30)
        value = self.account.value(query_time)
        self.assertEqual(value, 10)

    def test_it_defaults_to_the_current_time_if_no_argument_is_given(self):
        timestamp = EpochTimestampConverter().epoch()
        self.account.import_snapshot(timestamp - 5, 10)
        self.account.import_snapshot(timestamp - 10, 20)
        value = self.account.value()
        self.assertEqual(value, 10)

    def test_it_returns_the_latest_timestamp(self):
        epoch = EpochTimestampConverter().epoch()
        self.account.import_snapshot(epoch, 100)
        updated = self.account.last_updated()
        self.assertEqual(updated, EpochTimestampConverter().timestamp(epoch))

    def test_an_account_is_identical_to_itself(self):
        self.assertTrue(self.account.is_identical_to(self.account))

    def test_an_account_is_not_identical_to_one_with_a_different_name(self):
        different_account = Account("another name", "Bob Bobberson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", AccountType.ASSET)
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_owner(self):
        different_account = Account("account name", "Sam Sampson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", AccountType.ASSET)
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_symbol(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL_2", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", AccountType.ASSET)
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_asset_class(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL", AssetClass.EQUITIES, "Rachel's Bank", AccountType.ASSET)
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_institution(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Eric's Bank", AccountType.ASSET)
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_account_type(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL", AssetClass.CASH_EQUIVALENTS, "Rachel's Bank", AccountType.LIABILITY)
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_it_returns_a_row_for_a_balance_sheet(self):
        date_difference = Constants.SECONDS_PER_DAY*2
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.account.import_snapshot(timestamp - date_difference, 100)
        balance_sheet_row = self.account.balance_sheet_row()
        self.assertEqual(balance_sheet_row, ["\x1b[0;37;40m" + expected_date + "\x1b[0m", "Rachel's Bank","account name","SYMBOL","Bob Bobberson","Cash Equivalents","100"])

    def test_it_colors_the_date_red_if_it_is_in_the_future(self):
        date_difference = Constants.SECONDS_PER_DAY*91
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp + date_difference)
        self.account.import_snapshot(timestamp + date_difference, 100)
        balance_sheet_row = self.account.balance_sheet_row()
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "Rachel's Bank","account name","SYMBOL","Bob Bobberson","Cash Equivalents","0"])

    def test_it_colors_the_date_yellow_if_it_is_over_30_days_in_the_past(self):
        date_difference = Constants.SECONDS_PER_DAY*31
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.account.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = self.account.balance_sheet_row()
        self.assertEqual(balance_sheet_row, ["\x1b[0;33;40m" + expected_date + "\x1b[0m", "Rachel's Bank","account name","SYMBOL","Bob Bobberson","Cash Equivalents","0"])

    def test_it_colors_the_date_pink_if_it_is_over_60_days_in_the_past(self):
        date_difference = Constants.SECONDS_PER_DAY*61
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.account.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = self.account.balance_sheet_row()
        self.assertEqual(balance_sheet_row, ["\x1b[1;35;40m" + expected_date + "\x1b[0m", "Rachel's Bank","account name","SYMBOL","Bob Bobberson","Cash Equivalents","0"])

    def test_it_colors_the_date_red_if_it_is_over_90_days_in_the_past(self):
        date_difference = Constants.SECONDS_PER_DAY*91
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.account.import_snapshot(timestamp - date_difference, 0)
        balance_sheet_row = self.account.balance_sheet_row()
        self.assertEqual(balance_sheet_row, ["\x1b[1;31;40m" + expected_date + "\x1b[0m", "Rachel's Bank","account name","SYMBOL","Bob Bobberson","Cash Equivalents","0"])

    def test_it_returns_a_row_for_a_liability(self):
        date_difference = Constants.SECONDS_PER_DAY*2
        timestamp = EpochTimestampConverter().epoch()
        expected_date = EpochTimestampConverter().timestamp(timestamp - date_difference)
        self.liability.import_snapshot(timestamp - date_difference, 100)
        liabilities_row = self.liability.liabilities_row()
        self.assertEqual(liabilities_row, [expected_date, "Rachel's Bank","account name","Bob Bobberson","100"])

if __name__ == '__main__':
    unittest.main()
