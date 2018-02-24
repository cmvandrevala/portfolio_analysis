from portfolio.account import Account
from valid_options.account_type import AccountType
from valid_options.asset_class import AssetClass
from portfolio.invalid_account_exception import InvalidAccountException
import typing


class AccountBuilder:
    def __init__(self):
        self.__params = {"account_type": AccountType.ASSET, "asset_class": AssetClass.CASH_EQUIVALENTS}

    def build(self) -> Account:
        if self.__params.get("name") is None:
            raise InvalidAccountException("The name of the account must be set.")
        elif self.__params.get("owner") is None:
            raise InvalidAccountException("The name of the owner must be set.")
        elif self.__params.get("investment") is None:
            raise InvalidAccountException("The name of the investment must be set.")
        elif self.__params.get("institution") is None:
            raise InvalidAccountException("The name of the institution must be set.")
        else:
            return Account(self.__params)

    def set_name(self, name: str) -> typing.Any:
        self.__params["name"] = name
        return self

    def set_owner(self, owner: str) -> typing.Any:
        self.__params["owner"] = owner
        return self

    def set_investment(self, investment: str) -> typing.Any:
        self.__params["investment"] = investment
        return self

    def set_institution(self, institution: str) -> typing.Any:
        self.__params["institution"] = institution
        return self

    def set_liability(self) -> typing.Any:
        self.__params["account_type"] = AccountType.LIABILITY
        self.__params["asset_class"] = AssetClass.NONE
        return self

    def set_asset(self) -> typing.Any:
        self.__params["account_type"] = AccountType.ASSET
        return self

    def set_asset_class(self, asset_class: AssetClass) -> typing.Any:
        self.__params["asset_class"] = asset_class
        return self

    def set_account_type(self, account_type: AccountType) -> typing.Any:
        if account_type == AccountType.LIABILITY:
            self.set_liability()
        elif account_type == AccountType.ASSET:
            self.set_asset()
        return self

    def set_update_frequency(self, update_frequency):
        self.__params["update_frequency"] = update_frequency
        return self

    def set_open_date(self, open_date):
        self.__params["open_date"] = open_date
        return self

    def set_term(self, term):
        self.__params["term"] = term
        return self
