import csv

from utilities.presenter import Presenter

class CsvImporter:

    def __init__(self, general_ledger_path):
        self.general_ledger_path = general_ledger_path

    def consumers(self, file_path, account_type):
        data_to_append = []
        self.__read_from_csv(file_path, data_to_append, account_type, self.__consumer_row)
        self.__append_to_general_ledger(data_to_append)

    def manual(self, file_path):
        data_to_append = []
        self.__read_from_csv(file_path, data_to_append, None, self.__manual_row)
        self.__append_to_general_ledger(data_to_append)

    def __consumer_row(self, row, account_type):
        return [ Presenter.date(row[0]), "Consumers Credit Union", account_type, "Family", "CASHX", "ASSET", Presenter.value(row[5]) ]

    def __manual_row(self, row, account_type=None):
        return row

    def __read_from_csv(self, file_path, data_to_append, account_type, row_fn):
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                data_to_append.append(row_fn(row, account_type))

    def __append_to_general_ledger(self, data):
        with open(self.general_ledger_path, 'a') as f:
            writer = csv.writer(f)
            for a in data:
                writer.writerow(a)
