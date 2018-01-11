from portfolio.account import Account
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass
from portfolio.invalid_account_exception import InvalidAccountException


class AccountBuilder:
    def __init__(self):
        self.__owner = None
        self.__name = None
        self.__investment = None
        self.__institution = None
        self.__asset_class = AssetClass.CASH_EQUIVALENTS
        self.__account_type = AccountType.ASSET

    def build(self):
        if self.__name is None:
            raise InvalidAccountException("The name of the account must be set.")
        elif self.__owner is None:
            raise InvalidAccountException("The name of the owner must be set.")
        elif self.__investment is None:
            raise InvalidAccountException("The name of the investment must be set.")
        elif self.__institution is None:
            raise InvalidAccountException("The name of the institution must be set.")
        else:
            return Account(self.__name, self.__owner, self.__investment, self.__asset_class, self.__institution,
                           self.__account_type)

    def set_name(self, name):
        self.__name = name
        return self

    def set_owner(self, owner):
        self.__owner = owner
        return self

    def set_investment(self, investment):
        self.__investment = investment
        return self

    def set_institution(self, institution):
        self.__institution = institution
        return self

    def set_liability(self):
        self.__account_type = AccountType.LIABILITY
        self.__asset_class = AssetClass.NONE
        return self

    def set_asset(self):
        self.__account_type = AccountType.ASSET
        return self

    def set_asset_class(self, asset_class):
        self.__asset_class = asset_class
        return self

    def set_account_type(self, account_type):
        if account_type == AccountType.LIABILITY:
            self.set_liability()
        elif account_type == AccountType.ASSET:
            self.set_asset()
        return self