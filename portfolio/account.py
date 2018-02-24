import uuid

from portfolio.snapshot import Snapshot
from portfolio.snapshot_history import SnapshotHistory
from valid_options.term import Term


class Account:
    def __init__(self, params):
        self.__name = params.get("name")
        self.__owner = params.get("owner")
        self.__investment = params.get("investment")
        self.__asset_class = params.get("asset_class")
        self.__institution = params.get("institution")
        self.__account_type = params.get("account_type")
        self.__update_frequency = params.get("update_frequency")
        self.__term = params.get("term")
        self.__open_date = params.get("open_date")
        self.__uuid = params.get("uuid", str(uuid.uuid4()))
        self.__history = SnapshotHistory()

    def name(self):
        return self.__name

    def owner(self):
        return self.__owner

    def investment(self):
        return self.__investment

    def institution(self):
        return self.__institution

    def account_type(self):
        return self.__account_type.value

    def update_frequency(self):
        return self.__update_frequency or 7

    def asset_class(self):
        return self.__asset_class.value

    def term(self):
        return (self.__term or Term.NONE).value

    def open_date(self):
        return self.__open_date

    def uuid(self):
        return self.__uuid

    def value(self, query_time=None):
        return self.__history.value(query_time)

    def import_snapshot(self, time, value):
        snapshot = Snapshot(time, value)
        return self.__history.import_snapshot(snapshot)

    def last_updated(self):
        return self.__history.last_updated()

    def is_identical_to(self, account):
        return (self.name() == account.name() and
                self.owner() == account.owner() and
                self.investment() == account.investment() and
                self.asset_class() == account.asset_class() and
                self.institution() == account.institution() and
                self.account_type() == account.account_type() and
                self.open_date() == account.open_date() and
                self.term() == account.term())
