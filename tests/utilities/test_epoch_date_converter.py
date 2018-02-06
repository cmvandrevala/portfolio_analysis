import datetime
import time
import unittest

from dateutil.tz import tzlocal

from utilities.epoch_date_converter import EpochDateConverter


class EpochTimestampConverterTestCase(unittest.TestCase):
    def setUp(self):
        self.converter = EpochDateConverter()

    def test_it_returns_the_current_epoch_given_no_date(self):
        self.assertAlmostEqual(self.converter.date_to_epoch(), time.time(), places=1)

    def test_it_returns_the_current_epoch_given_a_date_of_None(self):
        self.assertAlmostEqual(self.converter.date_to_epoch(None), time.time(), places=1)

    def test_it_returns_an_epoch_from_a_date(self):
        self.assertEqual(self.converter.date_to_epoch("2017-01-02"), 1483336800)

    def test_it_extracts_an_epoch_from_another_date(self):
        self.assertEqual(self.converter.date_to_epoch("2011-03-01"), 1298959200)

    def test_it_converts_an_epoch_just_past_midnight_in_central_time(self):
        epoch = 1517464800
        expected_date = "2018-02-01"
        self.assertEqual(self.converter.epoch_to_date(epoch), expected_date)

    def test_it_converts_an_epoch_just_before_midnight_in_central_time(self):
        epoch = 1517551199
        expected_date = "2018-02-01"
        self.assertEqual(self.converter.epoch_to_date(epoch), expected_date)

    def test_it_gracefully_handles_a_decimal_epoch(self):
        epoch = 1107488000.0015
        expected_date = "2005-02-03"
        self.assertEqual(self.converter.epoch_to_date(epoch), expected_date)

    def test_it_returns_the_current_date_given_no_epoch(self):
        epoch = self.converter.date_to_epoch()
        self.assertEqual(self.converter.epoch_to_date(epoch), self.converter.epoch_to_date())

    def test_it_returns_the_current_date_given_an_epoch_of_None(self):
        expected_date = datetime.datetime.fromtimestamp(self.converter.date_to_epoch(), tzlocal()).strftime('%Y-%m-%d')
        self.assertAlmostEqual(self.converter.epoch_to_date(None), expected_date, places=1)

    def test_it_converts_a_date_to_an_epoch_and_back(self):
        date = "2011-02-03"
        epoch = self.converter.date_to_epoch(date)
        self.assertEqual(self.converter.epoch_to_date(epoch), date)

    def test_it_converts_another_date_to_an_epoch_and_back(self):
        date = "2011-01-01"
        epoch = self.converter.date_to_epoch(date)
        self.assertEqual(self.converter.epoch_to_date(epoch), date)


if __name__ == '__main__':
    unittest.main()
