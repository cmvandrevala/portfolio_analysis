import json

import requests
from flask import Flask, jsonify, render_template, redirect, request

from app.form_formatter import FormFormatter
from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from report.balance_sheet import BalanceSheet
from report.line_graph import LineGraph
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter
from valid_options.account_type import AccountType

app = Flask(__name__)
portfolio = PortfolioCreator().create(DataSource())


@app.route("/")
def index():
    account_types = [e.value for e in AccountType]
    return render_template('index.html', account_types=account_types, institutions=portfolio.institutions())


@app.route("/accounts")
def accounts():
    return render_template('accounts.html', portfolio=portfolio)


@app.route("/accounts/<account_uuid>")
def account(account_uuid):
    account = list(filter(lambda x: x.uuid() == account_uuid, portfolio.accounts))[0]
    return render_template('account.html', account=account)


@app.route("/append_snapshot", methods=['POST'])
def append_snapshot():
    global portfolio
    request_body = FormFormatter(EpochDateConverter()).format(request.form.to_dict())
    json_body = json.dumps(request_body)
    requests.post(Constants.DATA_URL + "/append_snapshot", data=json_body)
    portfolio = PortfolioCreator().create(DataSource())
    return redirect("/accounts", code=302)


@app.route("/balance_sheet")
def balance_sheet():
    return render_template('balance_sheet.html', balance_sheet=BalanceSheet(portfolio))


@app.route("/net_worth_vs_time")
def net_worth_vs_time():
    start = request.args.get('start')
    end = request.args.get('end')
    return jsonify(LineGraph(portfolio).net_worth_vs_time(start, end))


if __name__ == "__main__":
    app.run()
