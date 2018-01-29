import datetime
import time


class EpochTimestampConverter:
    def epoch(self, timestamp=None):
        if timestamp is None:
            return time.time()
        else:
            v = self.__split_timestamp(timestamp)
            return self.__calculate_epoch_from_timestamp(v[0], v[1])

    def timestamp(self, epoch=None):
        if epoch is None:
            return self.timestamp(self.epoch())
        else:
            return datetime.datetime.utcfromtimestamp(epoch).strftime('%Y-%m-%d')

    def __split_timestamp(self, timestamp):
        if "T" in timestamp:
            d = self.__split_date_on_dashes(timestamp.split("T")[0])
            t = self.__split_time_on_colons(timestamp.split("T")[1])
        else:
            d = self.__split_date_on_dashes(timestamp)
            t = self.__split_time_on_colons()
        return [d, t]

    def __split_date_on_dashes(self, date_string):
        year = int(date_string.split("-")[0])
        month = int(date_string.split("-")[1])
        day = int(date_string.split("-")[2])
        return {"year": year, "month": month, "day": day}

    def __split_time_on_colons(self, time_string=None):
        if time_string is None:
            return {"hour": 0, "minute": 0, "second": 0}
        else:
            hour = int(time_string.split(":")[0])
            minute = int(time_string.split(":")[1])
            second = int(time_string.split(":")[2].replace("Z", ""))
            return {"hour": hour, "minute": minute, "second": second}

    def __calculate_epoch_from_timestamp(self, date, time):
        return datetime.datetime(year=date["year"],
                                 month=date["month"],
                                 day=date["day"],
                                 hour=time["hour"],
                                 minute=time["minute"],
                                 second=time["second"],
                                 tzinfo=datetime.timezone.utc).timestamp()
