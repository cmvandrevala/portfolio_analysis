import csv
import os
import shutil

if not os.path.isfile("ledger.csv"):
    with open("ledger.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Institution", "Name", "Owner", "Symbol", "Classification", "Value"])
else:
    shutil.move("ledger.csv", "ledger.csv.old")
    lines_seen = set()
    outfile = open("ledger.csv", "w")
    for line in open("ledger.csv.old", "r"):
        if line not in lines_seen:
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove("ledger.csv.old")
