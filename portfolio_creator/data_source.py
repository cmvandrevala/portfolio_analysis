import requests

from utilities.constants import Constants


class DataSource:

    def get(self):
        return requests.get(Constants.DATA_URL).text
