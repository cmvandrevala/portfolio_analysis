import json

import requests
from flask import Flask, render_template, redirect, request

from app.form_formatter import FormFormatter
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter
from valid_options.account_type import AccountType

app = Flask(__name__)


@app.route("/")
def index():
    account_types = [e.value for e in AccountType]
    return render_template('index.html', account_types=account_types)


@app.route("/accounts")
def accounts():
    portfolio = PortfolioCreator().create(DataSource())
    return render_template('accounts.html', portfolio=portfolio)


@app.route("/accounts/<int:account_id>")
def account(account_id):
    portfolio = PortfolioCreator().create(DataSource())
    account = portfolio.accounts[account_id]
    return render_template('account.html', account=account)


@app.route("/append_snapshot", methods=['POST'])
def append_snapshot():
    request_body = FormFormatter(EpochDateConverter()).format(request.form.to_dict())
    json_body = json.dumps(request_body)
    requests.post(Constants.DATA_URL + "/append_snapshot", data=json_body)
    return redirect("/accounts", code=302)


if __name__ == "__main__":
    app.run()
