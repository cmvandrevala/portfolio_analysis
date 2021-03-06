import unittest

from utilities.presenter import Presenter


class PresenterTestCase(unittest.TestCase):
    def test_it_formats_a_date_with_slashes(self):
        self.assertEqual(Presenter.date_slashes_as_dashes("12/02/2017"), "2017-12-02")

    def test_it_does_nothing_to_a_correctly_formatted_date(self):
        self.assertEqual(Presenter.date_slashes_as_dashes("1999-06-07"), "1999-06-07")

    def test_it_formats_a_positive_value_with_no_commas(self):
        self.assertEqual(Presenter.value_without_symbols("$500"), "500")

    def test_it_formats_a_positive_value_with_one_comma(self):
        self.assertEqual(Presenter.value_without_symbols("$5,000"), "5000")

    def test_it_formats_a_positive_value_with_many_commas(self):
        self.assertEqual(Presenter.value_without_symbols("$5,000,125"), "5000125")

    def test_it_formats_a_negative_value_with_no_commas(self):
        self.assertEqual(Presenter.value_without_symbols("($500)"), "-500")

    def test_it_formats_a_negative_value_with_one_comma(self):
        self.assertEqual(Presenter.value_without_symbols("($5,000)"), "-5000")

    def test_it_formats_a_negative_value_with_many_commas(self):
        self.assertEqual(Presenter.value_without_symbols("($5,000,125)"), "-5000125")

    def test_it_does_nothing_to_a_correctly_formatted_value(self):
        self.assertEqual(Presenter.value_without_symbols("5102.25"), "5102.25")

    def test_it_formats_0_into_a_percentage(self):
        self.assertEqual(Presenter.decimal_as_percentage(0.0), "0.0%")

    def test_it_formats_one_half_into_a_percentage(self):
        self.assertEqual(Presenter.decimal_as_percentage(0.5), "50.0%")

    def test_it_formats_one_into_a_percentage(self):
        self.assertEqual(Presenter.decimal_as_percentage(1.0), "100.0%")

    def test_it_rounds_a_repeating_decimal_to_one_place(self):
        self.assertEqual(Presenter.decimal_as_percentage(0.777777777778), "77.8%")


if __name__ == '__main__':
    unittest.main()
