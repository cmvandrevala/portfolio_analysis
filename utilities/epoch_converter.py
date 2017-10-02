import datetime
import calendar

class EpochConverter:

    @staticmethod
    def convert(date_string):
        year = int(date_string.split("-")[0])
        month = int(date_string.split("-")[1])
        day = int(date_string.split("-")[2])
        dt = datetime.datetime(year=year, month=month, day=day)
        return calendar.timegm(dt.timetuple())
