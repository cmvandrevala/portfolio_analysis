import datetime

from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter


class LineGraph:
    def __init__(self, portfolio):
        self.__portfolio = portfolio

    def net_worth_vs_time(self, start_date, end_date):
        current_epoch = EpochDateConverter().date_to_epoch(start_date)
        times = []
        values = []
        while current_epoch <= EpochDateConverter().date_to_epoch(end_date):
            formatted_date = EpochDateConverter().epoch_to_date(current_epoch)
            times.append(datetime.datetime.fromtimestamp(current_epoch))
            values.append(self.__portfolio.total_value(formatted_date))
            current_epoch += Constants.SECONDS_PER_DAY
        return {"times": times, "values": values}
