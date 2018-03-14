import unittest

from app.form_formatter.update_frequency_formatter import UpdateFrequencyFormatter


class UpdateFrequencyFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.formatter = UpdateFrequencyFormatter()

    def test_does_not_change_a_properly_formatted_input(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': True, 'frequency': 7}
        self.assertEqual(self.formatter.format(input_data), input_data)

    def test_it_converts_the_frequency_to_an_int(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': True, 'frequency': '7'}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'frequency': 7}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_converts_a_floating_point_value_to_an_int(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': True, 'frequency': 2.25}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'frequency': 2}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_sets_an_asset_value_to_true(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': "ASSET", 'frequency': 6}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'frequency': 6}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_sets_an_asset_value_to_false(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': "LIABILITY", 'frequency': 30}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': False, 'frequency': 30}
        self.assertEqual(self.formatter.format(input_data), output_data)