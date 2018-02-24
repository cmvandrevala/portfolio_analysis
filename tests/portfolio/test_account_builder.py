import unittest

from portfolio.account import Account
from portfolio.account_builder import AccountBuilder
from portfolio.invalid_account_exception import InvalidAccountException
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass
from valid_options.term import Term


class AssetTestCase(unittest.TestCase):

    def setUp(self):
        self.builder = AccountBuilder().set_name("name").set_owner("owner").set_investment("investment").set_institution("institution")

    def test_it_builds_an_account_with_defaults(self):
        account = self.builder.build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "institution",
                  "account_type": AccountType.ASSET}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_an_account_as_a_liability_and_updates_the_asset_class(self):
        account = self.builder.set_liability().build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.NONE, "institution": "institution",
                  "account_type": AccountType.LIABILITY}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_an_account_as_a_liability_by_passing_in_the_account_type(self):
        account = self.builder.set_account_type(AccountType.LIABILITY).build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.NONE, "institution": "institution",
                  "account_type": AccountType.LIABILITY}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_an_account_as_an_asset(self):
        account = self.builder.set_liability().set_asset().build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.NONE, "institution": "institution",
                  "account_type": AccountType.ASSET}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_the_asset_class_of_an_account(self):
        account = self.builder.set_asset_class(AssetClass.ANNUITIES).build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.ANNUITIES, "institution": "institution",
                  "account_type": AccountType.ASSET}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_the_update_frequency_of_an_account(self):
        account = self.builder.set_update_frequency(12).build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "institution",
                  "account_type": AccountType.ASSET}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_the_open_date(self):
        account = self.builder.set_open_date("2005-1-1").build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "institution",
                  "account_type": AccountType.ASSET, "open_date": "2005-1-1"}
        self.assertTrue(account.is_identical_to(Account(params)))

    def test_it_sets_the_term(self):
        account = self.builder.set_term(Term.MEDIUM).build()
        params = {"name": "name", "owner": "owner", "investment": "investment",
                  "asset_class": AssetClass.CASH_EQUIVALENTS, "institution": "institution",
                  "account_type": AccountType.ASSET, "term": Term.MEDIUM}
        self.assertTrue(account.is_identical_to(Account(params)))

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