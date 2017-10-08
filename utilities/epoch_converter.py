import datetime
import time

class EpochConverter:

    @staticmethod
    def date_to_epoch(date_string):
        year = int(date_string.split("-")[0])
        month = int(date_string.split("-")[1])
        day = int(date_string.split("-")[2])
        return datetime.datetime(year=year, month=month, day=day, hour=12, tzinfo=datetime.timezone.utc).timestamp()

    @staticmethod
    def epoch_to_date(epoch):
        return datetime.datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d')

    @staticmethod
    def current_epoch():
        return time.time()
