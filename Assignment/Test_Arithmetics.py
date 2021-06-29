import Arithmetics

class Test_Arithmetics:
    # Default module basic Unit Testing
    def run_test(self):
        arithmetics = Arithmetics.Arithmetics()

        assert arithmetics.mod(2016, 4) == 0    # PASS