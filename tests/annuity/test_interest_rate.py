import unittest

from annuity.interest_rate import InterestRate


class InterestRateTestCase(unittest.TestCase):

    def setUp(self):
        self.rate = InterestRate(0.07)

    def test_it_has_a_nominal_rate_of_interest(self):
        self.assertAlmostEqual(self.rate.nominal(), 0.07, delta=0.001)

    def test_it_returns_a_monthly_nominal_rate_of_interest(self):
        self.assertAlmostEqual(self.rate.nominal(12), 0.0057, delta=0.001)

    def test_the_real_rate_of_interest_equals_the_nominal_rate_if_inflation_is_zero(self):
        self.assertAlmostEqual(self.rate.real(0.0), 0.07, delta = 0.001)

    def test_the_real_rate_of_interest_decreases_with_nonzero_inflation(self):
        self.assertAlmostEqual(self.rate.real(0.01), 0.06, delta=0.001)

    def test_it_returns_a_daily_real_rate_of_interest(self):
        self.assertAlmostEqual(self.rate.real(0.01, 365), 0.00016, delta=0.001)

if __name__ == '__main__':
    unittest.main()
