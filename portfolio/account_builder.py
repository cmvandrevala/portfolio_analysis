from portfolio.account import Account
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass
from portfolio.invalid_account_exception import InvalidAccountException
import typing


class AccountBuilder:
    def __init__(self):
        self.__owner = None  # type: str
        self.__name = None  # type: str
        self.__investment = None  # type: str
        self.__institution = None  # type: str
        self.__update_frequency = None  # type: int
        self.__asset_class = AssetClass.CASH_EQUIVALENTS  # type: AssetClass
        self.__account_type = AccountType.ASSET  # type: AccountType

    def build(self) -> Account:
        if self.__name is None:
            raise InvalidAccountException("The name of the account must be set.")
        elif self.__owner is None:
            raise InvalidAccountException("The name of the owner must be set.")
        elif self.__investment is None:
            raise InvalidAccountException("The name of the investment must be set.")
        elif self.__institution is None:
            raise InvalidAccountException("The name of the institution must be set.")
        elif self.__update_frequency is None:
            return Account(self.__name, self.__owner, self.__investment, self.__asset_class, self.__institution,
                           self.__account_type)
        else:
            return Account(self.__name, self.__owner, self.__investment, self.__asset_class, self.__institution,
                           self.__account_type, self.__update_frequency)

    def set_name(self, name: str) -> typing.Any:
        self.__name = name
        return self

    def set_owner(self, owner: str) -> typing.Any:
        self.__owner = owner
        return self

    def set_investment(self, investment: str) -> typing.Any:
        self.__investment = investment
        return self

    def set_institution(self, institution: str) -> typing.Any:
        self.__institution = institution
        return self

    def set_liability(self) -> typing.Any:
        self.__account_type = AccountType.LIABILITY
        self.__asset_class = AssetClass.NONE
        return self

    def set_asset(self) -> typing.Any:
        self.__account_type = AccountType.ASSET
        return self

    def set_asset_class(self, asset_class: AssetClass) -> typing.Any:
        self.__asset_class = asset_class
        return self

    def set_account_type(self, account_type: AccountType) -> typing.Any:
        if account_type == AccountType.LIABILITY:
            self.set_liability()
        elif account_type == AccountType.ASSET:
            self.set_asset()
        return self

    def set_update_frequency(self, update_frequency):
        self.__update_frequency = update_frequency
        return self
