import csv

from utilities.presenter import Presenter

class CsvImporter:

    def __init__(self, general_ledger_path):
        self.general_ledger_path = general_ledger_path

    def import_csv(self, file_path, row_fn, account_type = None):
        data = []
        self.__read_from_csv(file_path, data, account_type, row_fn)
        self.__append_to_general_ledger(data)

    def __read_from_csv(self, file_path, data_to_append, account_type, row_fn):
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                data_to_append.append(row_fn(row, account_type))

    def __append_to_general_ledger(self, data_rows):
        with open(self.general_ledger_path, 'a') as f:
            writer = csv.writer(f)
            for row in data_rows:
                writer.writerow(row)
