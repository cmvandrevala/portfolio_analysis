import form_formatter.form_formatter as ff


class UpdateFrequencyFormatter:
    def format(self, form_data):
        format_fn = ff.compose(ff.format_account_type, ff.format_frequency)
        return format_fn(form_data)
