import unittest

import math

from portfolio.account_builder import AccountBuilder
from portfolio.portfolio import Portfolio
from portfolio_analysis.portfolio_analyzer import PortfolioAnalyzer
from utilities.epoch_timestamp_converter import EpochTimestampConverter
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass


class PortfolioAnalyzerCase(unittest.TestCase):
    def test_it_returns_the_debt_to_equity_ratio_for_a_portfolio_with_no_liabilities(self):
        account = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        account.import_snapshot(EpochTimestampConverter().epoch(), 1234)
        portfolio = Portfolio()
        portfolio.import_account(account)
        self.assertEqual(PortfolioAnalyzer(portfolio).debt_to_equity(), 0.0)

    def test_it_returns_the_debt_to_equity_ratio_for_a_portfolio_with_only_liabilities(self):
        account = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.LIABILITY) \
            .build()
        account.import_snapshot(EpochTimestampConverter().epoch(), 1234)
        portfolio = Portfolio()
        portfolio.import_account(account)
        self.assertEqual(PortfolioAnalyzer(portfolio).debt_to_equity(), 1.0)

    def test_it_returns_the_debt_to_equity_ratio_for_a_portfolio_with_a_mixture_of_accounts_in_equal_value(self):
        asset = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        liability = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.LIABILITY) \
            .build()
        asset.import_snapshot(EpochTimestampConverter().epoch(), 12345)
        liability.import_snapshot(EpochTimestampConverter().epoch(), 12345)
        portfolio = Portfolio()
        portfolio.import_account(asset)
        portfolio.import_account(liability)
        self.assertEqual(PortfolioAnalyzer(portfolio).debt_to_equity(), math.inf)

    def test_it_returns_the_debt_to_equity_ratio_for_a_portfolio_with_a_mixture_of_accounts_in_nonequal_value(self):
        asset = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        liability = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.LIABILITY) \
            .build()
        asset.import_snapshot(EpochTimestampConverter().epoch(), 1234)
        liability.import_snapshot(EpochTimestampConverter().epoch(), 12345)
        portfolio = Portfolio()
        portfolio.import_account(asset)
        portfolio.import_account(liability)
        self.assertAlmostEqual(PortfolioAnalyzer(portfolio).debt_to_equity(), 1.1110611)

    def test_it_returns_the_debt_to_equity_ratio_for_a_historical_time(self):
        asset = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.ASSET) \
            .build()
        liability = AccountBuilder().set_name("name") \
            .set_institution("institution") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_asset_class(AssetClass.NONE) \
            .set_account_type(AccountType.LIABILITY) \
            .build()
        timestamp = EpochTimestampConverter().epoch()
        early_timestamp = timestamp - 200000
        query_time = timestamp - 100000
        asset.import_snapshot(timestamp, 112233)
        liability.import_snapshot(early_timestamp, 223344)
        portfolio = Portfolio()
        portfolio.import_account(asset)
        portfolio.import_account(liability)
        self.assertEqual(PortfolioAnalyzer(portfolio).debt_to_equity(EpochTimestampConverter().timestamp(query_time)), 1.0)


if __name__ == '__main__':
    unittest.main()
