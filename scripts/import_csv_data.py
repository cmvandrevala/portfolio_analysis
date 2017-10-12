import os

from general_ledger.row_formatter import RowFormatter
from general_ledger.csv_importer import CsvImporter
from utilities.constants import Constants

importer = CsvImporter(Constants.LOCAL_LEDGER_PATH)

for filename in os.listdir(Constants.LEDGERS_DIRECTORY):
    if filename.endswith(".csv"):
        importer.import_csv(Constants.LEDGERS_DIRECTORY + filename, RowFormatter.identity)
