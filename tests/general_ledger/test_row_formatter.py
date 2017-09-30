import unittest

from general_ledger.row_formatter import RowFormatter

class RowFormatterTestCase(unittest.TestCase):

    def test_it_does_not_alter_a_preformatted_row(self):
        row = ["foo", "bar", "baz", "quo", "foobar", "bazquo"]
        self.assertEqual(RowFormatter.identity(row), row)

    def test_it_formats_a_row_from_consumers_credit_union(self):
        row_input = ["03/24/2017", "TLR:YXH / DRAWER:514", "", "", "$60.00", "$337.89"]
        row_output = ["2017-03-24", "Consumers Credit Union", "Checking", "Family", "CASHX", "ASSET", "337.89"]
        self.assertEqual(RowFormatter.consumers(row_input, "Checking"), row_output)

if __name__ == '__main__':
    unittest.main()
