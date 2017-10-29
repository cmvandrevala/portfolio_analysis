import requests

from utilities.constants import Constants


class DataSource:
    def __init__(self):
        pass

    def get(self):
        return requests.get(Constants.DATA_URL).text
