import unittest

from portfolio.account import Account
from portfolio.account_builder import AccountBuilder
from portfolio.invalid_account_exception import InvalidAccountException
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass


class AssetTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = AccountBuilder().set_name("name").set_owner("owner").set_investment("investment").set_institution("institution")

    def test_it_builds_an_account_with_defaults(self):
        account = self.builder.build()
        self.assertTrue(account.is_identical_to(Account("name", "owner", "investment", AssetClass.CASH_EQUIVALENTS, "institution", AccountType.ASSET)))

    def test_it_sets_an_account_as_a_liability_and_updates_the_asset_class(self):
        account = self.builder.set_liability().build()
        self.assertTrue(account.is_identical_to(Account("name", "owner", "investment", AssetClass.NONE, "institution", AccountType.LIABILITY)))

    def test_it_sets_an_account_as_a_liability_by_passing_in_the_account_type(self):
        account = self.builder.set_account_type(AccountType.LIABILITY).build()
        self.assertTrue(account.is_identical_to(Account("name", "owner", "investment", AssetClass.NONE, "institution", AccountType.LIABILITY)))

    def test_it_sets_an_account_as_an_asset(self):
        account = self.builder.set_liability().set_asset().build()
        self.assertTrue(account.is_identical_to(Account("name", "owner", "investment", AssetClass.NONE, "institution", AccountType.ASSET)))

    def test_it_sets_the_asset_class_of_an_account(self):
        account = self.builder.set_asset_class(AssetClass.ANNUITIES).build()
        self.assertTrue(account.is_identical_to(Account("name", "owner", "investment", AssetClass.ANNUITIES, "institution", AccountType.ASSET)))

    def test_it_sets_the_update_frequency_of_an_account(self):
        account = self.builder.set_update_frequency(12).build()
        self.assertTrue(account.is_identical_to(
            Account("name", "owner", "investment", AssetClass.CASH_EQUIVALENTS, "institution", AccountType.ASSET, 12)))

    def test_the_account_name_is_required(self):
        builder = AccountBuilder().set_owner("owner").set_investment("investment").set_institution("institution")
        self.assertRaises(InvalidAccountException, builder.build)

    def test_the_account_owner_is_required(self):
        builder = AccountBuilder().set_name("name").set_investment("investment").set_institution("institution")
        self.assertRaises(InvalidAccountException, builder.build)

    def test_the_account_investment_is_required(self):
        builder = AccountBuilder().set_name("name").set_owner("owner").set_institution("institution")
        self.assertRaises(InvalidAccountException, builder.build)

    def test_the_account_institution_is_required(self):
        builder = AccountBuilder().set_name("name").set_owner("owner").set_investment("investment")
        self.assertRaises(InvalidAccountException, builder.build)
