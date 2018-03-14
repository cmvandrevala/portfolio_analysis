import form_formatter.form_formatter as ff


class AppendSnapshotFormatter:
    def __init__(self, timestamp_generator):
        self.timestamp_generator = timestamp_generator

    def format(self, form_data):
        format_fn = ff.compose(ff.format_account_type, self.__format_value, self.__format_timestamp)
        return format_fn(form_data)

    def __format_value(self, form_data):
        if type(form_data["value"]) is str:
            form_data["value"] = form_data["value"].replace(".", "")
            form_data["value"] = int(form_data["value"])
            ff.format_account_type(form_data)
        return form_data

    def __format_timestamp(self, form_data):
        if "timestamp" not in form_data:
            form_data["timestamp"] = self.timestamp_generator.epoch_to_date()
        return form_data
