import form_formatter.form_formatter as ff


class UpdateOpenDateFormatter:
    def format(self, form_data):
        return ff.format_account_type(form_data)
