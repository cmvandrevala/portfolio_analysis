import unittest

import time

from portfolio.account_builder import AccountBuilder
from portfolio.portfolio import Portfolio
from portfolio_analysis.account_recommender import AccountRecommender
from portfolio_analysis.invalid_recommendation_exception import InvalidRecommendationException


class AccountRecommenderCase(unittest.TestCase):
    def setUp(self):
        self.recommender = AccountRecommender()
        self.asset = AccountBuilder().set_name("name") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_institution("institution") \
            .set_asset() \
            .build()
        self.liability = AccountBuilder().set_name("name") \
            .set_owner("owner") \
            .set_investment("investment") \
            .set_institution("institution") \
            .set_liability() \
            .build()

    def test_the_default_account_cannot_be_a_liability(self):
        self.assertRaises(InvalidRecommendationException, self.recommender.recommend, Portfolio(), self.liability)

    def test_it_returns_the_default_account_if_no_accounts_are_in_the_portfolio(self):
        recommended_account = self.recommender.recommend(Portfolio(), self.asset)
        self.assertEqual(recommended_account, self.asset)

    def test_it_returns_the_default_account_if_one_liability_with_zero_balance_is_in_the_portfolio(self):
        portfolio = Portfolio()
        portfolio.import_account(self.liability)
        recommended_account = self.recommender.recommend(portfolio, self.asset)
        self.assertEqual(recommended_account, self.asset)

    def test_it_returns_a_liability_with_a_nonzero_balance(self):
        portfolio = Portfolio()
        self.liability.import_snapshot(time.time(), 1000)
        portfolio.import_account(self.liability)
        recommended_account = self.recommender.recommend(portfolio, self.asset)
        self.assertEqual(recommended_account, self.liability)


if __name__ == '__main__':
    unittest.main()
