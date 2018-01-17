import functools

from valid_options.account_type import AccountType


class FormFormatter:
    def __init__(self, timestamp_generator):
        self.timestamp_generator = timestamp_generator

    def format(self, form_data):
        format_fn = self.__compose(self.__format_asset_field, self.__format_value, self.__format_timestamp)
        return format_fn(form_data)

    def __format_value(self, form_data):
        if type(form_data["value"]) is str:
            form_data["value"] = form_data["value"].replace(".", "")
            form_data["value"] = int(form_data["value"])
            self.__format_asset_field(form_data)
        return form_data

    def __format_asset_field(self, form_data):
        if form_data["asset"] == AccountType.ASSET.value:
            form_data["asset"] = True
        elif form_data["asset"] == AccountType.LIABILITY.value:
            form_data["asset"] = False
        return form_data

    def __format_timestamp(self, form_data):
        if "timestamp" not in form_data:
            form_data["timestamp"] = self.timestamp_generator.timestamp()
        return form_data

    def __compose(self, *functions):
        return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
