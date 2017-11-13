class InterestRate:

    def __init__(self, nominal_interest_rate):
        self.__nominal_interest_rate = nominal_interest_rate

    def nominal(self):
        return self.__nominal_interest_rate

    def real(self, inflation_rate):
        return (1 + self.__nominal_interest_rate) / (1 + inflation_rate) - 1
