import unittest
import time
from finance.asset_history import AssetHistory
from finance.snapshot import Snapshot

class AssetHistoryTestCase(unittest.TestCase):

    def setUp(self):
        self.history = AssetHistory()

    def test_it_returns_an_asset_value_of_zero_if_there_are_no_transactions(self):
        asset_value = self.history.asset_value()
        self.assertEqual(asset_value, 0)

    def test_it_returns_an_asset_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = time.time()
        query_time = timestamp - 20
        snapshot = Snapshot(timestamp, 1, 100)
        self.history.import_snapshot(snapshot)
        asset_value = self.history.asset_value(query_time)
        self.assertEqual(asset_value, 0)

    def test_it_returns_the_correct_asset_value_when_queried_after_a_snapshot(self):
        timestamp = time.time()
        query_time = timestamp + 20
        snapshot = Snapshot(timestamp, 1, 100)
        self.history.import_snapshot(snapshot)
        asset_value = self.history.asset_value(query_time)
        self.assertEqual(asset_value, 100)

    def test_it_returns_the_correct_asset_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = time.time()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2

        earlier_snapshot = Snapshot(earlier_timestamp, 1, 300)
        later_snapshot = Snapshot(later_timestamp, 1, 250)
        self.history.import_snapshot(earlier_snapshot)
        self.history.import_snapshot(later_snapshot)

        asset_value = self.history.asset_value(query_time)
        self.assertEqual(asset_value, 300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = time.time()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2

        query_time = timestamp1 + 1

        snapshot1 = Snapshot(timestamp1, 1, 10)
        snapshot2 = Snapshot(timestamp2, 1, 20)
        snapshot3 = Snapshot(timestamp3, 1, 30)

        self.history.import_snapshot(snapshot2)
        self.history.import_snapshot(snapshot1)
        self.history.import_snapshot(snapshot3)

        asset_value = self.history.asset_value(query_time)
        self.assertEqual(asset_value, 10)

    def test_it_defaults_to_the_current_time_if_no_argument_is_given(self):
        timestamp = time.time()
        snapshot1 = Snapshot(timestamp - 5, 1, 10)
        snapshot2 = Snapshot(timestamp - 10, 1, 20)
        self.history.import_snapshot(snapshot1)
        self.history.import_snapshot(snapshot2)

        asset_value = self.history.asset_value()
        self.assertEqual(asset_value, 10)

if __name__ == '__main__':
    unittest.main()
