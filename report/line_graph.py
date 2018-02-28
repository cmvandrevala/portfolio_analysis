import datetime

from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter


class LineGraph:
    def __init__(self, portfolio):
        self.__portfolio = portfolio

    def net_worth_vs_time(self, start_date, end_date):
        current_epoch = EpochDateConverter().date_to_epoch(start_date)
        output = []
        while current_epoch <= EpochDateConverter().date_to_epoch(end_date):
            formatted_date = EpochDateConverter().epoch_to_date(current_epoch)
            output.append({"x": datetime.datetime.fromtimestamp(current_epoch).strftime("%Y-%m-%d"),
                           "y": self.__portfolio.total_value(formatted_date)})
            current_epoch += Constants.SECONDS_PER_DAY
        return output
