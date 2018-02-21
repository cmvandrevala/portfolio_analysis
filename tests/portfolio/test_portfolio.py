import unittest

from portfolio.account_builder import AccountBuilder
from portfolio.portfolio import Portfolio
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass


class PortfolioTestCase(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio()
        self.asset_data_1 = {"timestamp": "2017-06-01", "name": "Proctor and Gamble", "investment": "PG", "value": 1000,
                             "asset_class": "Equities", "owner": "Bob", "institution": "Bank 1",
                             "account_type": "ASSET", "update_frequency": 2, "term": "none"}
        self.asset_data_2 = {"timestamp": "2017-07-01", "name": "Vanguard Bond Fund", "investment": "VTIBX",
                             "value": 2000, "asset_class": "Fixed Income", "owner": "Sam", "institution": "Bank 2",
                             "account_type": "ASSET", "update_frequency": 9, "term": "none"}
        self.liability_data_1 = {"timestamp": "2017-06-05", "name": "Visa Card", "value": 1000, "investment": "CASHX",
                                 "institution": "Bank 1", "account_type": "LIABILITY", "asset_class": "None",
                                 "owner": "Craig", "update_frequency": 15, "term": "none"}
        self.liability_data_2 = {"timestamp": "2017-07-05", "name": "Personal Loan", "value": 1500,
                                 "investment": "CASHX", "institution": "Bank 2", "account_type": "LIABILITY",
                                 "asset_class": "None", "owner": "Eusavio", "term": "none"}

    def test_it_starts_off_with_no_assets_or_liabilities(self):
        self.assertEqual(self.portfolio.assets_value(), 0)
        self.assertEqual(self.portfolio.liabilities_value(), 0)
        self.assertEqual(self.portfolio.total_value(), 0)

    def test_it_starts_off_no_percentages(self):
        self.assertEqual(self.portfolio.percentages(), {})

    def test_it_imports_asset_data_for_a_new_asset(self):
        self.portfolio.import_data(self.asset_data_1)
        self.assertEqual(self.portfolio.percentages(), {"PG": 1.0})

    def test_it_imports_liability_data_for_a_new_liability(self):
        self.portfolio.import_data(self.liability_data_1)
        self.assertEqual(self.portfolio.assets_value(), 0)
        self.assertEqual(self.portfolio.liabilities_value(), 1000)
        self.assertEqual(self.portfolio.total_value(), -1000)

    def test_it_imports_data_for_two_new_assets(self):
        self.portfolio.import_data(self.asset_data_1)
        self.portfolio.import_data(self.asset_data_2)
        self.assertEqual(self.portfolio.percentages(), {'PG': 0.333, 'VTIBX': 0.667})

    def test_it_imports_data_for_two_new_liabilities(self):
        self.portfolio.import_data(self.liability_data_1)
        self.portfolio.import_data(self.liability_data_2)
        self.assertEqual(self.portfolio.assets_value(), 0)
        self.assertEqual(self.portfolio.liabilities_value(), 2500)
        self.assertEqual(self.portfolio.total_value(), -2500)

    def test_it_imports_asset_data_for_an_existing_asset(self):
        asset_data = {"timestamp": "2017-05-01", "name": "Verizon", "investment": "VZ", "value": 5000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Abraham", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-05-02", "name": "Verizon", "investment": "VZ", "value": 2000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Francis", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 1.0})

    def test_it_imports_asset_data_for_existing_and_new_assets_with_the_same_owner(self):
        asset_data = {"timestamp": "2017-06-01", "name": "VZ", "investment": "VZ", "value": 3000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Willie", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-30", "name": "PEP", "investment": "PEP", "value": 4000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Willie", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-17", "name": "VZ", "investment": "VZ", "value": 6000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Willie", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0.6, "PEP": 0.4})

    def test_it_imports_asset_data_for_existing_and_new_assets_with_different_owners(self):
        asset_data = {"timestamp": "2017-06-01", "name": "VZ", "investment": "VZ", "value": 6000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Willie", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-30", "name": "PEP", "investment": "PEP", "value": 6000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Seymour", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-17", "name": "VZ", "investment": "VZ", "value": 6000,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Jack", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0.667, "PEP": 0.333})

    def test_it_does_not_ignore_a_single_zero_dollar_amount(self):
        asset_data = {"timestamp": "2012-01-01", "name": "T", "investment": "T", "value": 0, "asset_class": "Equities",
                      "owner": "Shauna", "institution": "Bank", "account_type": "ASSET",  "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"T": 0})

    def test_it_does_not_ignore_a_zero_dollar_amount_mixed_with_other_amounts(self):
        asset_data = {"timestamp": "2011-02-08", "name": "Verizon", "investment": "VZ", "value": 0,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Brandine", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2011-02-08", "name": "Something", "investment": "SP", "value": 12.54, "term": "none",
                      "asset_class": "Equities", "owner": "Brittney", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"VZ": 0, "SP": 1.0})

    def test_it_gives_the_total_value_of_the_portfolio_at_the_current_time(self):
        self.portfolio.import_data(self.asset_data_1)
        self.portfolio.import_data(self.asset_data_2)
        self.portfolio.import_data(self.liability_data_1)
        self.assertEqual(self.portfolio.assets_value(), 3000)
        self.assertEqual(self.portfolio.liabilities_value(), 1000)
        self.assertEqual(self.portfolio.total_value(), 2000)

    def test_it_gives_the_total_value_of_the_portfolio_at_a_previous_time(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Verizon", "investment": "VZ", "value": 100,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Carl", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-01", "name": "SP", "investment": "SP", "value": 12.50,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Julie", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        liability_data = {"timestamp": "2017-02-01", "name": "loan", "investment": "Bank of Martin", "value": 50,
                          "institution": "bank", "term": "none",
                          "account_type": "LIABILITY", "asset_class": "None", "owner": "Martin"}
        self.portfolio.import_data(liability_data)
        self.assertEqual(self.portfolio.assets_value("2017-03-01"), 100)
        self.assertEqual(self.portfolio.liabilities_value("2017-03-01"), 50)
        self.assertEqual(self.portfolio.total_value("2017-03-01"), 50)

    def test_it_does_not_include_liabilities_in_percentages(self):
        self.portfolio.import_data(self.asset_data_1)
        self.portfolio.import_data(self.asset_data_2)
        self.portfolio.import_data(self.liability_data_1)
        self.assertEqual(self.portfolio.percentages(), {'PG': 0.333, 'VTIBX': 0.667})

    def test_it_combines_assets_with_the_same_investment_in_percentage_calculations(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Felipe", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-01", "name": "Bar", "investment": "A", "value": 100,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Kent", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-02-01", "name": "Baz", "investment": "B", "value": 100,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Marge", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"A": 0.667, "B": 0.333})

    def test_it_creates_different_assets_given_different_investments_with_the_same_name(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Lucy", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-06-01", "name": "Foo", "investment": "B", "value": 200,
                      "asset_class": "Equities", "term": "none",
                      "owner": "Greg", "institution": "Bank", "account_type": "ASSET"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.percentages(), {"A": 0.333, "B": 0.667})

    def test_it_returns_zero_for_each_asset_class_if_there_is_no_asset_data(self):
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0,
                          "Annuities": 0, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_cash_equivalent(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Cash Equivalents", "owner": "Frank", "institution": "Bank",
                      "account_type": "ASSET", "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 1, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0,
                          "Annuities": 0, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_equity(self):
        self.portfolio.import_data(self.asset_data_1)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 1, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0,
                          "Annuities": 0, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_fixed_income_asset(self):
        self.portfolio.import_data(self.asset_data_2)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 1, "Real Estate": 0, "Commodities": 0,
                          "Annuities": 0, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_real_estate_asset(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Real Estate", "owner": "Anna", "institution": "Bank", "account_type": "ASSET", "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 1, "Commodities": 0,
                          "Annuities": 0, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_commodity(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Commodities", "owner": "Clark", "institution": "Bank", "account_type": "ASSET", "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 1,
                          "Annuities": 0, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_annuity(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Annuities", "owner": "Clark", "institution": "Bank", "account_type": "ASSET", "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0,
                          "Annuities": 1, "Fixed Assets": 0})

    def test_it_returns_asset_data_for_one_fixed_asset(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Fixed Assets", "owner": "Clark", "institution": "Bank", "account_type": "ASSET", "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0, "Fixed Income": 0, "Real Estate": 0, "Commodities": 0,
                          "Annuities": 0, "Fixed Assets": 1})

    def test_it_returns_asset_data_for_two_asset_classes(self):
        asset_data = {"timestamp": "2017-01-01", "name": "Foo", "investment": "A", "value": 100,
                      "asset_class": "Equities", "owner": "Tiffany", "institution": "Bank", "account_type": "ASSET", "term": "long"}
        self.portfolio.import_data(asset_data)
        asset_data = {"timestamp": "2017-02-01", "name": "Bar", "investment": "B", "value": 100, "asset_class": "Fixed Income",
                      "owner": "Eusavio", "institution": "Bank", "account_type": "ASSET", "term": "none"}
        self.portfolio.import_data(asset_data)
        self.assertEqual(self.portfolio.asset_classes(),
                         {"Cash Equivalents": 0, "Equities": 0.5, "Fixed Income": 0.5, "Real Estate": 0,
                          "Commodities": 0, "Annuities": 0, "Fixed Assets": 0})

    def test_it_imports_an_account(self):
        account = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        self.portfolio.import_account(account)
        self.assertEqual(self.portfolio.accounts, [account])

    def test_it_imports_a_second_account_in_the_portfolio(self):
        account_one = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        account_two = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("another owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        self.portfolio.import_account(account_one)
        self.portfolio.import_account(account_two)
        self.assertEqual(self.portfolio.accounts, [account_one, account_two])

    def test_it_does_not_import_an_account_if_it_already_exists_in_the_portfolio(self):
        account = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        self.portfolio.import_account(account)
        self.portfolio.import_account(account)
        self.assertEqual(self.portfolio.accounts, [account])

    def test_it_returns_a_list_of_outdated_assets(self):
        account_one = AccountBuilder().set_name("name one") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .set_update_frequency(120) \
            .build()
        account_two = AccountBuilder().set_name("name two") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .set_update_frequency(1) \
            .build()
        timestamp = EpochDateConverter().date_to_epoch() - 5 * Constants.SECONDS_PER_DAY
        account_one.import_snapshot(timestamp, 100)
        account_two.import_snapshot(timestamp, 100)
        self.portfolio.import_account(account_one)
        self.portfolio.import_account(account_two)
        self.assertEqual(self.portfolio.outdated_assets(), [account_two])

    def test_it_returns_a_list_of_outdated_liabilities(self):
        account_one = AccountBuilder().set_name("name one") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.LIABILITY) \
            .set_update_frequency(10) \
            .build()
        account_two = AccountBuilder().set_name("name two") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.LIABILITY) \
            .set_update_frequency(3) \
            .build()
        timestamp = EpochDateConverter().date_to_epoch() - 7 * Constants.SECONDS_PER_DAY
        account_one.import_snapshot(timestamp, 100)
        account_two.import_snapshot(timestamp, 100)
        self.portfolio.import_account(account_one)
        self.portfolio.import_account(account_two)
        self.assertEqual(self.portfolio.outdated_liabilities(), [account_two])


if __name__ == '__main__':
    unittest.main()
