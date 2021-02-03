"""
Test case for main calculator functions
"""

import unittest
from homework import test_simple_calc as calc


class SimpleCalcTestCase(unittest.TestCase):

    def test_add_positive_number(self):
        self.assertEqual(calc.add(8, 2), 10)

    def test_add_negative_number(self):
        self.assertEqual(calc.add(-8, -2), -10)

    def test_add_mix_number(self):
        self.assertEqual(calc.add(-8, 2), -6)

    def test_subtract_positive_number(self):
        self.assertEqual(calc.subtract(4, 2), 2)

    def test_subtract_negative_number(self):
        self.assertEqual(calc.subtract(-10, -2), -8)

    def test_subtract_mix_number(self):
        self.assertEqual(calc.subtract(-10, 2), -12)

    def test_multiply_positive_number(self):
        self.assertEqual(calc.multiply(24, 10000), 240000)

    def test_multiply_negative_number(self):
        self.assertEqual(calc.multiply(-18, -2), 36)

    def test_multiply_mix_number(self):
        self.assertEqual(calc.multiply(-99, 9), -891)

    def test_multiply_positive_divide(self):
        self.assertEqual(calc.divide(24, 10), 2.4)

    def test_multiply_negative_divide(self):
        self.assertEqual(calc.divide(-18, -2), 9)

    def test_multiply_mix_divide(self):
        self.assertEqual(calc.divide(-99, 9), -11)

    def test_multiply_null_divide(self):
        with self.assertRaises(ValueError) as error:
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
