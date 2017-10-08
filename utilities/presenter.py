class Presenter:

    @staticmethod
    def date_slashes_as_dashes(date_str):
        if (date_str.find("/") == -1):
            return date_str
        else:
            mdy = date_str.split("/")
            return mdy[2] + "-" + mdy[0] + "-" + mdy[1]

    @staticmethod
    def value_without_symbols(value_str):
        return value_str.replace("$","").replace(",","").replace(")","").replace("(","-")

    @staticmethod
    def decimal_as_percentage(percent_fraction):
        return str(round(100*percent_fraction, 1)) + "%"
