import json

import requests
from flask import Flask, render_template, redirect, request

from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.epoch_timestamp_converter import EpochTimestampConverter
from valid_options.account_type import AccountType

app = Flask(__name__)


@app.route("/")
def record():
    portfolio = PortfolioCreator().create(DataSource())
    return render_template('record.html', portfolio=portfolio)


@app.route("/append_snapshot", methods=['POST'])
def append_snapshot():
    request_body = request.form.to_dict()
    request_body["value"] = int(request_body["value"])
    if request_body["asset"] == AccountType.ASSET.value:
        request_body["asset"] = True
    else:
        request_body["asset"] = False
    request_body["timestamp"] = EpochTimestampConverter().timestamp()
    json_body = json.dumps(request_body)
    requests.post(Constants.DATA_URL + "/append_snapshot", data=json_body)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
