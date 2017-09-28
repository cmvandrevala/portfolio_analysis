import csv

from general_ledger.csv_importer import CsvImporter

importer = CsvImporter("ledger.csv")

importer.consumers("/Users/cyrus/Downloads/consumers_checking.csv", "Checking")
importer.consumers("/Users/cyrus/Downloads/consumers_savings.csv", "Savings")
