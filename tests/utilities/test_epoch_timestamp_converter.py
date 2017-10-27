import time
import unittest

from utilities.epoch_timestamp_converter import EpochTimestampConverter

class EpochTimestampConverterTestCase(unittest.TestCase):

    def setUp(self):
        self.converter = EpochTimestampConverter()

    def test_it_returns_the_current_epoch_given_no_date(self):
        self.assertAlmostEqual(self.converter.epoch(), time.time(), places=1)

    def test_it_returns_an_epoch_from_a_partial_timestamp(self):
        self.assertEqual(self.converter.epoch("2017-01-02"), 1483358400)

    def test_it_extracts_an_epoch_from_another_partial_timestamp(self):
        self.assertEqual(self.converter.epoch("2011-03-01"), 1298980800)

    def test_it_extracts_an_epoch_from_a_full_timestamp(self):
        self.assertEqual(self.converter.epoch("2012-02-11T13:14:15Z"), 1328966055)

    def test_it_returns_the_current_epoch_if_the_date_has_a_value_of_None(self):
        current_epoch = self.converter.epoch()
        self.assertAlmostEqual(self.converter.epoch(None), current_epoch, places=1)

    def test_it_returns_the_current_epoch_if_no_date_is_passed_in(self):
        current_epoch = self.converter.epoch()
        self.assertAlmostEqual(self.converter.epoch(), current_epoch, places=1)

    def test_it_returns_the_current_date_given_no_epoch(self):
        epoch = self.converter.epoch()
        self.assertEqual(self.converter.timestamp(epoch), self.converter.timestamp())

    def test_it_converts_an_epoch_into_a_utc_date_string(self):
        epoch = 1507488000
        expected_date = "2017-10-08"
        self.assertEqual(self.converter.timestamp(epoch), expected_date)

    def test_it_converts_a_different_epoch_into_a_utc_date_string(self):
        epoch = 1107488000
        expected_date = "2005-02-04"
        self.assertEqual(self.converter.timestamp(epoch), expected_date)

    def test_it_gracefully_handles_a_decimal_epoch(self):
        epoch = 1107488000.0015
        expected_date = "2005-02-04"
        self.assertEqual(self.converter.timestamp(epoch), expected_date)

    def test_it_converts_a_epoch_and_back(self):
        date = "2011-02-03"
        epoch = self.converter.epoch(date)
        self.assertEqual(self.converter.timestamp(epoch), date)

if __name__ == '__main__':
    unittest.main()
