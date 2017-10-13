import unittest

from general_ledger.row_formatter import RowFormatter

class RowFormatterTestCase(unittest.TestCase):

    def test_it_does_not_alter_a_preformatted_row(self):
        row = ["foo", "bar", "baz", "quo", "foobar", "bazquo", "class"]
        self.assertEqual(RowFormatter.identity(row), row)

if __name__ == '__main__':
    unittest.main()
