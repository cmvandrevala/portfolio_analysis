import unittest

from form_formatter.update_open_date_formatter import UpdateOpenDateFormatter


class UpdateOpenDateFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.formatter = UpdateOpenDateFormatter()

    def test_it_formats_an_input(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': 'ASSET', 'open_date': '2007-12-13'}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'open_date': '2007-12-13'}
        self.assertEqual(self.formatter.format(input_data), output_data)