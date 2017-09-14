import unittest
import time
from finance.snapshot import Snapshot

class SnapshotTestCase(unittest.TestCase):

    def setUp(self):
        self.timestamp = time.time()
        self.snapshot = Snapshot(self.timestamp, 10235.63)

    def test_it_has_a_timestamp(self):
        self.assertEqual(self.snapshot.timestamp, self.timestamp)

    def test_it_has_a_value(self):
        self.assertEqual(self.snapshot.value, 10235.63)

if __name__ == '__main__':
    unittest.main()
