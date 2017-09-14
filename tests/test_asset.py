import unittest
import time

from finance.asset import Asset
from finance.snapshot import Snapshot

class AssetTestCase(unittest.TestCase):

    def setUp(self):
        self.asset = Asset("some asset name", "Bob Bobberson")

    def test_it_has_a_name(self):
        self.assertEqual(self.asset.name, "some asset name")

    def test_it_has_an_owner(self):
        self.assertEqual(self.asset.owner, "Bob Bobberson")

    def test_it_has_a_value_of_zero_if_there_are_no_snapshots(self):
        value = self.asset.value()
        self.assertEqual(value, 0)

    def test_it_returns_an_value_of_zero_when_queried_before_a_snapshot(self):
        timestamp = time.time()
        query_time = timestamp - 20
        snapshot = Snapshot(timestamp, 100)
        self.asset.import_snapshot(snapshot)
        value = self.asset.value(query_time)
        self.assertEqual(value, 0)

    def test_it_returns_the_correct_value_when_queried_after_a_snapshot(self):
        timestamp = time.time()
        query_time = timestamp + 20
        snapshot = Snapshot(timestamp, 100)
        self.asset.import_snapshot(snapshot)
        value = self.asset.value(query_time)
        self.assertEqual(value, 100)

    def test_it_returns_the_correct_value_when_queried_in_between_two_snapshots(self):
        later_timestamp = time.time()
        earlier_timestamp = later_timestamp - 120
        query_time = (earlier_timestamp + later_timestamp) / 2

        earlier_snapshot = Snapshot(earlier_timestamp, 300)
        later_snapshot = Snapshot(later_timestamp, 250)
        self.asset.import_snapshot(earlier_snapshot)
        self.asset.import_snapshot(later_snapshot)

        value = self.asset.value(query_time)
        self.assertEqual(value, 300)

    def test_the_order_in_which_snapshots_are_imported_makes_no_difference(self):
        timestamp1 = time.time()
        timestamp2 = timestamp1 - 1
        timestamp3 = timestamp1 - 2

        query_time = timestamp1 + 1

        snapshot1 = Snapshot(timestamp1, 10)
        snapshot2 = Snapshot(timestamp2, 20)
        snapshot3 = Snapshot(timestamp3, 30)

        self.asset.import_snapshot(snapshot2)
        self.asset.import_snapshot(snapshot1)
        self.asset.import_snapshot(snapshot3)

        value = self.asset.value(query_time)
        self.assertEqual(value, 10)

    def test_it_defaults_to_the_current_time_if_no_argument_is_given(self):
        timestamp = time.time()
        snapshot1 = Snapshot(timestamp - 5, 10)
        snapshot2 = Snapshot(timestamp - 10, 20)
        self.asset.import_snapshot(snapshot1)
        self.asset.import_snapshot(snapshot2)

        value = self.asset.value()
        self.assertEqual(value, 10)

if __name__ == '__main__':
    unittest.main()
