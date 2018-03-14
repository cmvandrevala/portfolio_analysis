import functools

from valid_options.account_type import AccountType


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def format_frequency(form_data):
    form_data['frequency'] = int(form_data['frequency'])
    return form_data


def format_account_type(form_data):
    if form_data["asset"] == AccountType.ASSET.value:
        form_data["asset"] = True
    elif form_data["asset"] == AccountType.LIABILITY.value:
        form_data["asset"] = False
    return form_data
