import csv

from general_ledger.row_formatter import RowFormatter
from general_ledger.csv_importer import CsvImporter
from utilities.constants import Constants

importer = CsvImporter(Constants.LOCAL_LEDGER_PATH)

importer.import_csv("../general_ledger/consumers_credit_union_checking.csv", RowFormatter.identity)
importer.import_csv("../general_ledger/consumers_credit_union_savings.csv", RowFormatter.identity)
importer.import_csv("/Users/cyrus/Downloads/transamerica.csv", RowFormatter.identity)
importer.import_csv("/Users/cyrus/Downloads/usbank_anna_checking.csv", RowFormatter.identity)
importer.import_csv("/Users/cyrus/Downloads/usbank_cyrus_checking.csv", RowFormatter.identity)
importer.import_csv("/Users/cyrus/Downloads/usbank_cyrus_savings.csv", RowFormatter.identity)
importer.import_csv("/Users/cyrus/Downloads/schwab_cyrus.csv", RowFormatter.identity)
