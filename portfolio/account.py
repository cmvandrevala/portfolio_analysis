from portfolio.snapshot import Snapshot
from portfolio.snapshot_history import SnapshotHistory
from valid_options.term import Term


class Account:
    def __init__(self, name, owner, investment, asset_class, institution, account_type, update_frequency=None, open_date=None, term=None):
        self.__name = name
        self.__owner = owner
        self.__investment = investment
        self.__asset_class = asset_class
        self.__institution = institution
        self.__account_type = account_type
        self.__update_frequency = update_frequency
        self.__term = term
        self.__open_date = open_date
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
