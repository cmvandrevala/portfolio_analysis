import unittest

from utilities.epoch_converter import EpochConverter
from core.account import Account

class AssetTestCase(unittest.TestCase):

    def setUp(self):
        self.account = Account("account name", "Bob Bobberson", "SYMBOL", "Cash Equivalents", "Rachel's Bank", "ASSET")

    def test_it_has_a_name(self):
        self.assertEqual(self.account.name, "account name")

    def test_it_has_an_owner(self):
        self.assertEqual(self.account.owner, "Bob Bobberson")

    def test_it_has_a_symbol(self):
        self.assertEqual(self.account.symbol, "SYMBOL")

    def test_it_has_an_asset_class(self):
        self.assertEqual(self.account.asset_class, "Cash Equivalents")

    def test_it_has_an_institution(self):
        self.assertEqual(self.account.institution, "Rachel's Bank")

    def test_it_has_an_account_type(self):
        self.assertEqual(self.account.account_type, "ASSET")

    def test_it_has_a_value_of_zero_if_there_are_no_snapshots(self):
        value = self.account.value()
        self.assertEqual(value, 0)

    def test_it_returns_an_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = EpochConverter.current_epoch()
        query_time = timestamp - 20
        self.account.import_snapshot(timestamp, 100)
        value = self.account.value(query_time)
        self.assertEqual(value, 0)

    def test_it_returns_the_correct_value_when_queried_after_a_snapshot(self):
        timestamp = EpochConverter.current_epoch()
        query_time = timestamp + 20
        self.account.import_snapshot(timestamp, 100)
        value = self.account.value(query_time)
        self.assertEqual(value, 100)

    def test_it_returns_the_correct_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = EpochConverter.current_epoch()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2
        self.account.import_snapshot(earlier_timestamp, 300)
        self.account.import_snapshot(later_timestamp, 250)
        value = self.account.value(query_time)
        self.assertEqual(value, 300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = EpochConverter.current_epoch()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2
        query_time = timestamp1 + 1
        self.account.import_snapshot(timestamp2, 20)
        self.account.import_snapshot(timestamp1, 10)
        self.account.import_snapshot(timestamp3, 30)
        value = self.account.value(query_time)
        self.assertEqual(value, 10)

    def test_it_defaults_to_the_current_time_if_no_argument_is_given(self):
        timestamp = EpochConverter.current_epoch()
        self.account.import_snapshot(timestamp - 5, 10)
        self.account.import_snapshot(timestamp - 10, 20)
        value = self.account.value()
        self.assertEqual(value, 10)

    def test_it_returns_the_latest_timestamp(self):
        epoch = EpochConverter.current_epoch()
        self.account.import_snapshot(epoch, 100)
        updated = self.account.last_updated()
        self.assertEqual(updated, EpochConverter.epoch_to_date(epoch))

    def test_an_account_is_identical_to_itself(self):
        self.assertTrue(self.account.is_identical_to(self.account))

    def test_an_account_is_not_identical_to_one_with_a_different_name(self):
        different_account = Account("another name", "Bob Bobberson", "SYMBOL", "Cash Equivalents", "Rachel's Bank", "ASSET")
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_owner(self):
        different_account = Account("account name", "Sam Sampson", "SYMBOL", "Cash Equivalents", "Rachel's Bank", "ASSET")
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_symbol(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL_2", "Cash Equivalents", "Rachel's Bank", "ASSET")
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_asset_class(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL", "Equities", "Rachel's Bank", "ASSET")
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_institution(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL", "Cash Equivalents", "Eric's Bank", "ASSET")
        self.assertFalse(self.account.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_account_type(self):
        different_account = Account("account name", "Bob Bobberson", "SYMBOL", "Cash Equivalents", "Rachel's Bank", "LIABILITY")
        self.assertFalse(self.account.is_identical_to(different_account))

if __name__ == '__main__':
    unittest.main()
