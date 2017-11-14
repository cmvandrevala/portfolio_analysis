class InterestRate:

    def __init__(self, nominal_yearly_interest_rate):
        self.__nominal_yearly_interest_rate = nominal_yearly_interest_rate

    def nominal(self, periods=1):
        return self.__per_period_rate(self.__nominal_yearly_interest_rate, periods)

    def real(self, inflation_rate, periods=1):
        real_rate = (1 + self.__nominal_yearly_interest_rate) / (1 + inflation_rate) - 1
        return self.__per_period_rate(real_rate, periods)

    def __per_period_rate(self, rate, periods):
        return (1 + rate)**(1/periods) - 1
