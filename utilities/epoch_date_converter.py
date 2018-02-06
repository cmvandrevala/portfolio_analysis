import datetime
import time

from dateutil.tz import tzlocal


class EpochDateConverter:
    def __init__(self):
        self.tz = tzlocal()

    def date_to_epoch(self, date=None):
        if date is None:
            return time.time()
        else:
            return self.__calculate_epoch_from_date(date)

    def epoch_to_date(self, epoch=None):
        if epoch is None:
            return self.epoch_to_date(self.date_to_epoch())
        else:
            return datetime.datetime.fromtimestamp(epoch, self.tz).strftime('%Y-%m-%d')

    def __calculate_epoch_from_date(self, date):
        split_date = self.__split_date(date)
        return datetime.datetime(year=split_date["year"],
                                 month=split_date["month"],
                                 day=split_date["day"],
                                 hour=0,
                                 minute=0,
                                 second=0,
                                 tzinfo=self.tz).timestamp()

    def __split_date(self, date_string):
        year = int(date_string.split("-")[0])
        month = int(date_string.split("-")[1])
        day = int(date_string.split("-")[2])
        return {"year": year, "month": month, "day": day}
