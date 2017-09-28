import csv

from utilities.presenter import Presenter

class CsvImporter:

    def __init__(self, general_ledger_path):
        self.general_ledger_path = general_ledger_path

    def consumers(self, file_path, account_type):
        data_to_append = []
        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                data_to_append.append([ Presenter.date(row[0]), "Consumers Credit Union", account_type, "Family", "CASHX", "ASSET", Presenter.value(row[5]) ])
        with open(self.general_ledger_path, 'a') as f:
            writer = csv.writer(f)
            for a in data_to_append:
                writer.writerow(a)
