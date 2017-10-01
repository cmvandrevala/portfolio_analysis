import csv

from general_ledger.row_formatter import RowFormatter
from general_ledger.csv_importer import CsvImporter
from utilities.constants import Constants

importer = CsvImporter(Constants.GENERAL_LEDGER_PATH)

importer.import_csv("/Users/cyrus/Downloads/consumers_checking.csv", RowFormatter.consumers, "Checking")
importer.import_csv("/Users/cyrus/Downloads/consumers_savings.csv", RowFormatter.consumers, "Savings")
importer.import_csv("/Users/cyrus/Downloads/transamerica.csv", RowFormatter.identity)
