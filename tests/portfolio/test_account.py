import unittest

from portfolio.account import Account
from utilities.epoch_date_converter import EpochDateConverter
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass
from valid_options.term import Term


class AssetTestCase(unittest.TestCase):
    def setUp(self):
        self.asset_params = {"name": "account name", "owner": "Bob Bobberson", "investment": "investment", "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "Rachel's Bank", "account_type": AccountType.ASSET, "open_date": "2001-12-12", "update_frequency": 12, "term": Term.SHORT}
        self.asset = Account(self.asset_params)
        liability_params = {"name": "account name", "owner": "Bob Bobberson", "investment": "investment", "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "Rachel's Bank", "account_type": AccountType.ASSET}
        self.liability = Account(liability_params)

    def test_it_has_a_name(self):
        self.assertEqual(self.asset.name(), "account name")

    def test_it_has_an_owner(self):
        self.assertEqual(self.asset.owner(), "Bob Bobberson")

    def test_it_has_a_investment(self):
        self.assertEqual(self.asset.investment(), "investment")

    def test_it_has_an_asset_class(self):
        self.assertEqual(self.asset.asset_class(), "Cash Equivalents")

    def test_it_has_a_suggested_frequency_of_updates_in_days(self):
        self.assertEqual(self.asset.update_frequency(), 12)

    def test_it_has_a_default_frequency_of_one_week(self):
        self.assertEqual(self.liability.update_frequency(), 7)

    def test_it_throws_an_exception_if_a_random_string_is_passed_in_for_account_type(self):
        params = {"name": "account name", "owner": "Bob Bobberson", "investment": "investment", "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "Rachel's Bank", "account_type": "RANDOM"}
        invalid_account = Account(params)
        self.assertRaises(AttributeError, invalid_account.account_type)

    def test_it_has_an_institution(self):
        self.assertEqual(self.asset.institution(), "Rachel's Bank")

    def test_it_has_an_account_type(self):
        self.assertEqual(self.asset.account_type(), AccountType.ASSET.value)

    def test_it_has_a_default_open_date_of_None(self):
        self.assertIsNone(self.liability.open_date())

    def test_it_has_an_open_date(self):
        self.assertEqual(self.asset.open_date(), "2001-12-12")

    def test_it_has_a_default_term(self):
        self.assertEqual(self.liability.term(), Term.NONE.value)

    def test_it_can_have_a_term_of_short(self):
        self.assertEqual(self.asset.term(), Term.SHORT.value)

    def test_it_can_have_a_term_of_medium(self):
        self.asset_params["term"] = Term.MEDIUM
        asset = Account(self.asset_params)
        self.assertEqual(asset.term(), Term.MEDIUM.value)

    def test_it_can_have_a_term_of_long(self):
        self.asset_params["term"] = Term.LONG
        asset = Account(self.asset_params)
        self.assertEqual(asset.term(), Term.LONG.value)

    def test_it_throws_an_exception_if_a_string_is_passed_in_for_an_account_type(self):
        self.asset_params["account_type"] = "RANDOM"
        invalid_account = Account(self.asset_params)
        self.assertRaises(AttributeError, invalid_account.account_type)

    def test_it_has_a_value_of_zero_if_there_are_no_snapshots(self):
        value = self.asset.value()
        self.assertEqual(value, 0)

    def test_it_returns_an_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = EpochDateConverter().date_to_epoch()
        query_time = timestamp - 20
        self.asset.import_snapshot(timestamp, 100)
        value = self.asset.value(query_time)
        self.assertEqual(value, 0)

    def test_it_returns_the_correct_value_when_queried_after_a_snapshot(self):
        timestamp = EpochDateConverter().date_to_epoch()
        query_time = timestamp + 20
        self.asset.import_snapshot(timestamp, 100)
        value = self.asset.value(query_time)
        self.assertEqual(value, 100)

    def test_it_returns_the_correct_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = EpochDateConverter().date_to_epoch()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2
        self.asset.import_snapshot(earlier_timestamp, 300)
        self.asset.import_snapshot(later_timestamp, 250)
        value = self.asset.value(query_time)
        self.assertEqual(value, 300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = EpochDateConverter().date_to_epoch()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2
        query_time = timestamp1 + 1
        self.asset.import_snapshot(timestamp2, 20)
        self.asset.import_snapshot(timestamp1, 10)
        self.asset.import_snapshot(timestamp3, 30)
        value = self.asset.value(query_time)
        self.assertEqual(value, 10)

    def test_it_defaults_to_the_current_time_if_no_argument_is_given(self):
        timestamp = EpochDateConverter().date_to_epoch()
        self.asset.import_snapshot(timestamp - 5, 10)
        self.asset.import_snapshot(timestamp - 10, 20)
        value = self.asset.value()
        self.assertEqual(value, 10)

    def test_it_returns_the_latest_timestamp(self):
        epoch = EpochDateConverter().date_to_epoch()
        self.asset.import_snapshot(epoch, 100)
        updated = self.asset.last_updated()
        self.assertEqual(updated, EpochDateConverter().epoch_to_date(epoch))

    def test_an_account_is_identical_to_itself(self):
        self.assertTrue(self.asset.is_identical_to(self.asset))

    def test_an_account_is_not_identical_to_one_with_a_different_name(self):
        self.asset_params["name"] = "another name"
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_owner(self):
        self.asset_params["owner"] = "another owner"
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_investment(self):
        self.asset_params["investment"] = "another investment"
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_asset_class(self):
        self.asset_params["asset_class"] = AssetClass.EQUITIES
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_institution(self):
        self.asset_params["institution"] = "another institution"
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_account_type(self):
        self.asset_params["account_type"] = AccountType.LIABILITY
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_identical_to_one_with_a_different_update_frequency(self):
        self.asset_params["update_frequency"] = 1000000
        different_account = Account(self.asset_params)
        self.assertTrue(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_open_date(self):
        self.asset_params["open_date"] = "another open date"
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))

    def test_an_account_is_not_identical_to_one_with_a_different_term(self):
        self.asset_params["term"] = Term.MEDIUM
        different_account = Account(self.asset_params)
        self.assertFalse(self.asset.is_identical_to(different_account))


if __name__ == '__main__':
    unittest.main()
