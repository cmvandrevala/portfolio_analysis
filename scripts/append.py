from pathlib import Path
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter
import sys


def collect_data_from_terminal(timestamp, value):
    asset_or_liability = input("Is this an asset (ASSET) or a liability (LIABILITY)? > ")
    asset_class = input("What is the asset class? > ")
    owner = input("Who is the owner of this account? > ")
    institution = input("What is the institution of this asset or liability? > ")
    description = input("Enter a description of the asset or liability. > ")
    symbol = input("Enter a symbol for this asset or liability. > ")
    return [timestamp, institution, description, owner, symbol, asset_or_liability, value, asset_class]


def write_row_to_csv_file(csv_path, row_values):
    filename = open(csv_path, 'a')
    filename.write(",".join(str(x) for x in row_values) + "\n")
    filename.close()


def create_row_data(csv_path, timestamp, value):
    filename = open(csv_path)
    for line_number, line in enumerate(filename):
        if line_number == 1:
            row_data = line.rstrip().split(",")
            row_data[0] = timestamp
            row_data[6] = value
        elif line_number > 1:
            break
    filename.close()
    return row_data


def create_a_new_csv_file(path, timestamp, value):
    print("I did not find any CSV file with a path of " + path)
    create_file = input("Would you like to create one now? > ")
    if create_file.lower() in Constants.YES_RESPONSES:
        write_row_to_csv_file(path, Constants.GENERAL_LEDGER_HEADERS)
        write_row_to_csv_file(path, collect_data_from_terminal(timestamp, value))
    else:
        print("Fine. Be that way. Jerk...")


def timestamp():
    if len(sys.argv) == 4:
        return sys.argv[3]
    else:
        return EpochTimestampConverter().timestamp()


def path():
    return Constants.LEDGERS_DIRECTORY + sys.argv[1] + ".csv"


def value():
    return float(sys.argv[2])


def file_exists():
    return Path(path()).is_file()


if file_exists():
    write_row_to_csv_file(path(), create_row_data(path(), timestamp(), value()))
else:
    create_a_new_csv_file(path(), timestamp(), value())
