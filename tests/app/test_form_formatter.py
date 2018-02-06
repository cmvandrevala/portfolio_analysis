import unittest

from app.form_formatter import FormFormatter


class MockTimestampCreator:
    def epoch_to_date(self):
        return "some date"


class FormFormatterTestCase(unittest.TestCase):
    def setUp(self):
        self.formatter = FormFormatter(MockTimestampCreator())

    def test_does_not_change_a_properly_formatted_input(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': True, 'value': 276077, 'timestamp': '2018-01-01'}
        self.assertEqual(self.formatter.format(input_data), input_data)

    def test_it_converts_the_value_to_an_int(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': True, 'value': '123', 'timestamp': '2018-01-01'}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'value': 123, 'timestamp': '2018-01-01'}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_converts_a_floating_point_value_to_an_int(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': True, 'value': '123.45', 'timestamp': '2018-01-01'}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'value': 12345, 'timestamp': '2018-01-01'}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_sets_an_asset_value_to_true(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': "ASSET", 'value': 0, 'timestamp': '2018-01-01'}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': True, 'value': 0, 'timestamp': '2018-01-01'}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_sets_an_asset_value_to_false(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': "LIABILITY", 'value': 0, 'timestamp': '2018-01-01'}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': False, 'value': 0, 'timestamp': '2018-01-01'}
        self.assertEqual(self.formatter.format(input_data), output_data)

    def test_it_adds_a_timestamp_to_the_data_if_one_is_missing(self):
        input_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                      'asset': False, 'value': 0}
        output_data = {'account': 'account', 'institution': 'institution', 'owner': 'owner', 'investment': 'investment',
                       'asset': False, 'value': 0, 'timestamp': 'some date'}
        self.assertEqual(self.formatter.format(input_data), output_data)
