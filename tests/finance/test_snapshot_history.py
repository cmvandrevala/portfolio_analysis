import unittest

from utilities.epoch_converter import EpochConverter
from finance.snapshot import Snapshot
from finance.snapshot_history import SnapshotHistory

class SnapshotHistoryTestCase(unittest.TestCase):

    def setUp(self):
        self.history = SnapshotHistory()

    def test_imports_a_snapshot(self):
        snapshot = Snapshot(EpochConverter.current_epoch(), 1000)
        self.history.import_snapshot(snapshot)
        self.assertEqual(self.history.all(), [snapshot])

    def test_imports_two_snapshots(self):
        snapshot1 = Snapshot(EpochConverter.current_epoch(), 1000)
        snapshot2 = Snapshot(EpochConverter.current_epoch(), 100)
        self.history.import_snapshot(snapshot1)
        self.history.import_snapshot(snapshot2)
        self.assertEqual(self.history.all(), [snapshot1, snapshot2])

    def test_it_has_a_value_of_zero_if_there_are_no_snapshots(self):
        self.assertEqual(self.history.value(), 0)

    def test_it_returns_an_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = EpochConverter.current_epoch()
        query_time = timestamp - 20
        self.history.import_snapshot(Snapshot(timestamp, 100))
        value = self.history.value(query_time)
        self.assertEqual(value, 0)

    def test_it_returns_the_correct_value_when_queried_after_a_snapshot(self):
        timestamp = EpochConverter.current_epoch()
        query_time = timestamp + 20
        self.history.import_snapshot(Snapshot(timestamp, 100))
        value = self.history.value(query_time)
        self.assertEqual(value, 100)

    def test_it_returns_the_correct_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = EpochConverter.current_epoch()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2

        self.history.import_snapshot(Snapshot(earlier_timestamp, 300))
        self.history.import_snapshot(Snapshot(later_timestamp, 250))

        value = self.history.value(query_time)
        self.assertEqual(value, 300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = EpochConverter.current_epoch()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2
        query_time = timestamp1 + 1
        self.history.import_snapshot(Snapshot(timestamp2, 20))
        self.history.import_snapshot(Snapshot(timestamp1, 10))
        self.history.import_snapshot(Snapshot(timestamp3, 30))
        value = self.history.value(query_time)
        self.assertEqual(value, 10)

    def test_it_defaults_to_the_current_epoch_if_no_argument_is_given(self):
        timestamp = EpochConverter.current_epoch()
        self.history.import_snapshot(Snapshot(timestamp - 5, 10))
        self.history.import_snapshot(Snapshot(timestamp - 10, 20))
        value = self.history.value()
        self.assertEqual(value, 10)

    def test_it_returns_the_latest_timestamp_for_one_snapshot(self):
        current_epoch = EpochConverter.current_epoch()
        formatted_date = EpochConverter.epoch_to_date(current_epoch)
        snapshot = Snapshot(current_epoch, 1000)
        self.history.import_snapshot(snapshot)
        self.assertEqual(self.history.last_updated(), formatted_date)

    def test_it_returns_the_latest_timestamp_for_two_snapshots(self):
        current_epoch = EpochConverter.current_epoch()
        formatted_date = EpochConverter.epoch_to_date(current_epoch)
        snapshot = Snapshot(current_epoch, 1000)
        self.history.import_snapshot(snapshot)
        snapshot = Snapshot(current_epoch - 1000000, 2000)
        self.history.import_snapshot(snapshot)
        self.assertEqual(self.history.last_updated(), formatted_date)

    def test_it_returns_the_latest_timestamp_for_three_snapshots(self):
        current_epoch = EpochConverter.current_epoch()
        formatted_date = EpochConverter.epoch_to_date(current_epoch)
        snapshot = Snapshot(current_epoch, 1000)
        self.history.import_snapshot(snapshot)
        snapshot = Snapshot(current_epoch - 1000000, 2000)
        self.history.import_snapshot(snapshot)
        snapshot = Snapshot(current_epoch - 2000000, 2000)
        self.history.import_snapshot(snapshot)
        self.assertEqual(self.history.last_updated(), formatted_date)

if __name__ == '__main__':
    unittest.main()
