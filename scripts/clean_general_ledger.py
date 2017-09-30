import csv
import os
import shutil

from utilities.constants import Constants

if not os.path.isfile(Constants.GENERAL_LEDGER_PATH):
    with open(Constants.GENERAL_LEDGER_PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(Constants.GENERAL_LEDGER_HEADERS)
else:
    shutil.move(Constants.GENERAL_LEDGER_PATH, Constants.GENERAL_LEDGER_PATH + ".old")
    lines_seen = set()
    outfile = open(Constants.GENERAL_LEDGER_PATH, "w")
    for line in open(Constants.GENERAL_LEDGER_PATH + ".old", "r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove(Constants.GENERAL_LEDGER_PATH + ".old")
