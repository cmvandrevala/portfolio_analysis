class Presenter:

    @staticmethod
    def date(date_str):
        if (date_str.find("/") == -1):
            return date_str
        else:
            mdy = date_str.split("/")
            return mdy[2] + "-" + mdy[0] + "-" + mdy[1]

    @staticmethod
    def value(value_str):
        return value_str.replace("$","").replace(",","").replace(")","").replace("(","-")
