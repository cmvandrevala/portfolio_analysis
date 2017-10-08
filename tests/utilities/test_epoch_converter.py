import time
import unittest

from utilities.epoch_converter import EpochConverter

class EpochConverterTestCase(unittest.TestCase):

    def test_it_extracts_an_epoch_from_a_date_string_with_dashes(self):
        self.assertEqual(EpochConverter.date_to_epoch("2017-01-02"), 1483358400)

    def test_it_extracts_an_epoch_from_another_date_string_with_dashes(self):
        self.assertEqual(EpochConverter.date_to_epoch("2011-03-01"), 1298980800)

    def test_it_converts_an_epoch_into_a_utc_date_string(self):
        epoch = 1507488000
        expected_date = "2017-10-08"
        self.assertEqual(EpochConverter.epoch_to_date(epoch), expected_date)

    def test_it_converts_a_different_epoch_into_a_utc_date_string(self):
        epoch = 1107488000
        expected_date = "2005-02-04"
        self.assertEqual(EpochConverter.epoch_to_date(epoch), expected_date)

    def test_it_gracefully_handles_a_decimal_epoch(self):
        epoch = 1107488000.0015
        expected_date = "2005-02-04"
        self.assertEqual(EpochConverter.epoch_to_date(epoch), expected_date)

    def test_it_converts_a_date_to_epoch_and_back(self):
        date = "2011-02-03"
        epoch = EpochConverter.date_to_epoch(date)
        self.assertEqual(EpochConverter.epoch_to_date(epoch), date)

    def test_it_returns_the_current_epoch(self):
        self.assertAlmostEqual(EpochConverter.current_epoch(), time.time(), places=1)

if __name__ == '__main__':
    unittest.main()
