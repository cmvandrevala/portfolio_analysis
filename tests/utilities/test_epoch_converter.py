import unittest

from utilities.epoch_converter import EpochConverter

class EpochConverterTestCase(unittest.TestCase):

    def test_it_extracts_an_epoch_from_a_date_string_with_dashes(self):
        self.assertEqual(EpochConverter.convert("2017-01-02"), 1483336800.0)

    def test_it_extracts_an_epoch_from_another_date_string_with_dashes(self):
        self.assertEqual(EpochConverter.convert("2011-03-01"), 1298959200.0)

if __name__ == '__main__':
    unittest.main()
