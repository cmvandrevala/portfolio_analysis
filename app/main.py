import json

import requests
from flask import Flask, render_template, redirect, request

from app.form_formatter import FormFormatter
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/accounts")
def accounts():
    portfolio = PortfolioCreator().create(DataSource())
    return render_template('record.html', portfolio=portfolio)


@app.route("/append_snapshot", methods=['POST'])
def append_snapshot():
    request_body = FormFormatter(EpochDateConverter()).format(request.form.to_dict())
    json_body = json.dumps(request_body)
    requests.post(Constants.DATA_URL + "/append_snapshot", data=json_body)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
