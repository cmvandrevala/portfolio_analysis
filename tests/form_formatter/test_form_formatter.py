import unittest

import form_formatter.form_formatter as ff


def f(x):
    return x + 1


def g(y):
    return y + 2


def h(z):
    return z + 3


class UpdateFrequencyFormatterTestCase(unittest.TestCase):

    def test_it_does_not_change_the_output_of_one_function(self):
        new_fn = ff.compose(f)
        self.assertEqual(new_fn(1), 2)

    def test_it_composes_two_functions(self):
        new_fn = ff.compose(f, g)
        self.assertEqual(new_fn(1), 4)

    def test_it_composes_three_functions(self):
        new_fn = ff.compose(f, g, h)
        self.assertEqual(new_fn(1), 7)

    def test_it_does_not_change_a_frequency_that_is_an_integer(self):
        input_data = {'frequency': 9}
        self.assertEqual(ff.format_frequency(input_data), input_data)

    def test_it_converts_the_frequency_from_a_string_to_an_integer(self):
        input_data = {'frequency': '7'}
        output_data = {'frequency': 7}
        self.assertEqual(ff.format_frequency(input_data), output_data)

    def test_it_converts_a_floating_point_value_to_an_int(self):
        input_data = {'frequency': 3.28}
        output_data = {'frequency': 3}
        self.assertEqual(ff.format_frequency(input_data), output_data)

    def test_it_sets_asset_to_true(self):
        input_data = {'asset': "ASSET"}
        output_data = {'asset': True}
        self.assertEqual(ff.format_account_type(input_data), output_data)

    def test_it_sets_asset_to_false(self):
        input_data = {'asset': "LIABILITY"}
        output_data = {'asset': False}
        self.assertEqual(ff.format_account_type(input_data), output_data)

    def test_it_does_not_change_asset_if_it_is_already_a_boolean(self):
        input_data = {'asset': False}
        self.assertEqual(ff.format_account_type(input_data), input_data)
