import unittest

from utilities.constants import Constants

class ConstantsTestCase(unittest.TestCase):

    def test_there_are_86400_seconds_in_a_day(self):
        self.assertEqual(Constants.SECONDS_PER_DAY, 86400)

    def test_there_are_365_days_in_a_year(self):
        self.assertEqual(Constants.DAYS_PER_YEAR, 365)

if __name__ == '__main__':
    unittest.main()
