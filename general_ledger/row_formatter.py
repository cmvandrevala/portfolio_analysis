from utilities.presenter import Presenter

class RowFormatter:

    @staticmethod
    def identity(row, account_type = None):
        return row

    @staticmethod
    def consumers(row, account_type):
        institution = "Consumers Credit Union"
        owner = "Family"
        symbol = "CASHX"
        classification = "ASSET"
        asset_class = "Cash Equivalents"
        return [ Presenter.date_slashes_as_dashes(row[0]), institution, account_type, owner, symbol, classification, Presenter.value_without_symbols(row[5]), asset_class ]
