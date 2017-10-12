import csv
import os
import shutil

from utilities.constants import Constants

if not os.path.isfile(Constants.LOCAL_LEDGER_PATH):
    with open(Constants.LOCAL_LEDGER_PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(Constants.GENERAL_LEDGER_HEADERS)
else:
    shutil.move(Constants.LOCAL_LEDGER_PATH, Constants.LOCAL_LEDGER_PATH + ".old")
    lines_seen = set()
    outfile = open(Constants.LOCAL_LEDGER_PATH, "w")
    for line in open(Constants.LOCAL_LEDGER_PATH + ".old", "r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove(Constants.LOCAL_LEDGER_PATH + ".old")
