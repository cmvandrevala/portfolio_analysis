from portfolio_analysis.invalid_recommendation_exception import InvalidRecommendationException


class AccountRecommender:
    def recommend(self, portfolio, default_account):
        if default_account.account_type() == "LIABILITY":
            raise InvalidRecommendationException("The default account must have an account type of asset.")
        for account in portfolio.accounts:
            if account.account_type() == "LIABILITY" and account.value() > 0:
                return account
        return default_account
