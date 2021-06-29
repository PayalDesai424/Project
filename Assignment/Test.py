import Arithmetics
import unittest


class Testing(unittest.TestCase):

    def run_test(self):
        arithmetics = Arithmetics.Arithmetics()

        # assert arithmetics.mod(3, 2) == 1   # PASS
        self.assertEqual(arithmetics.mod(10, 2), 0, "Pass")
