import unittest

from utilities.epoch_converter import EpochConverter
from core.liability import Liability

class LiabilityTestCase(unittest.TestCase):

    def setUp(self):
        self.liability = Liability("some liability name", "Carl's Brokerage")

    def test_it_has_a_name(self):
        self.assertEqual(self.liability.name, "some liability name")

    def test_it_has_a_default_symbol_of_CASHX(self):
        self.assertEqual(self.liability.symbol, "CASHX")

    def test_it_has_an_institution(self):
        self.assertEqual(self.liability.institution, "Carl's Brokerage")

    def test_it_has_a_value_of_zero_if_there_are_no_snapshots(self):
        value = self.liability.value()
        self.assertEqual(value, 0)

    def test_it_returns_an_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = EpochConverter.current_epoch()
        query_time = timestamp - 20
        self.liability.import_snapshot(timestamp, 100)
        value = self.liability.value(query_time)
        self.assertEqual(value, 0)

    def test_it_returns_the_correct_value_when_queried_after_a_snapshot(self):
        timestamp = EpochConverter.current_epoch()
        query_time = timestamp + 20
        self.liability.import_snapshot(timestamp, 100)
        value = self.liability.value(query_time)
        self.assertEqual(value, -100)

    def test_it_returns_the_correct_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = EpochConverter.current_epoch()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2
        self.liability.import_snapshot(earlier_timestamp, 300)
        self.liability.import_snapshot(later_timestamp, 250)
        value = self.liability.value(query_time)
        self.assertEqual(value, -300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = EpochConverter.current_epoch()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2
        query_time = timestamp1 + 1
        self.liability.import_snapshot(timestamp2, 20)
        self.liability.import_snapshot(timestamp1, 10)
        self.liability.import_snapshot(timestamp3, 30)
        value = self.liability.value(query_time)
        self.assertEqual(value, -10)

    def test_it_defaults_to_the_current_time_if_no_argument_is_given(self):
        timestamp = EpochConverter.current_epoch()
        self.liability.import_snapshot(timestamp - 5, 10)
        self.liability.import_snapshot(timestamp - 10, 20)
        value = self.liability.value()
        self.assertEqual(value, -10)

    def test_it_returns_the_latest_timestamp(self):
        timestamp = EpochConverter.current_epoch()
        formatted_date = EpochConverter.epoch_to_date(timestamp)
        self.liability.import_snapshot(timestamp, 100)
        updated = self.liability.last_updated()
        self.assertEqual(updated, formatted_date)

if __name__ == '__main__':
    unittest.main()
