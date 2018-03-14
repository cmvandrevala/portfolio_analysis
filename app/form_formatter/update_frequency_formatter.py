import functools

from valid_options.account_type import AccountType


class UpdateFrequencyFormatter:
    def format(self, form_data):
        format_fn = self.__compose(self.__format_asset_field, self.__format_frequency)
        return format_fn(form_data)

    def __format_frequency(self, form_data):
        form_data['frequency'] = int(form_data['frequency'])
        return form_data

    def __format_asset_field(self, form_data):
        if form_data["asset"] == AccountType.ASSET.value:
            form_data["asset"] = True
        elif form_data["asset"] == AccountType.LIABILITY.value:
            form_data["asset"] = False
        return form_data

    def __compose(self, *functions):
        return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
