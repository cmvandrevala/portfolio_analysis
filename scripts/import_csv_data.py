import os
import requests
import json
import csv

from utilities.constants import Constants

resp = requests.get(Constants.DATA_URL)
data = json.loads(resp.text)

with open(Constants.LOCAL_LEDGER_PATH, 'a') as f:
    writer = csv.writer(f)
    for item in data:
        writer.writerow([ item["timestamp"],
                          item["institution"],
                          item["description"],
                          item["owner"],
                          item["symbol"],
                          item["asset_or_liability"],
                          item["value"],
                          item["asset_class"] ])
