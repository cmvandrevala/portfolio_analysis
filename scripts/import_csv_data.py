import csv

from general_ledger.csv_importer import CsvImporter
from utilities.constants import Constants

importer = CsvImporter(Constants.GENERAL_LEDGER_PATH)

importer.consumers("/Users/cyrus/Downloads/consumers_checking.csv", "Checking")
importer.consumers("/Users/cyrus/Downloads/consumers_savings.csv", "Savings")

importer.manual("/Users/cyrus/Downloads/transamerica.csv")
