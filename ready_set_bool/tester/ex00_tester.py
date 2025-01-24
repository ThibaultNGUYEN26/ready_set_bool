import sys
import os
import unittest
from test_result_formatter import TestResultFormatter

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex00 import adder

class TestAdderFunction(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(adder(2, 3), 5)
        self.assertEqual(adder(1, 1), 2)
        self.assertEqual(adder(5, 0), 5)
        self.assertEqual(adder(0, 5), 5)

    def test_large_numbers(self):
        self.assertEqual(adder(1234, 5678), 6912)
        self.assertEqual(adder(1000000, 500000), 1500000)
        self.assertEqual(adder(98765, 43210), 141975)

    def test_identity_property(self):
        self.assertEqual(adder(0, 9999), 9999)
        self.assertEqual(adder(9999, 0), 9999)

    def test_commutative_property(self):
        self.assertEqual(adder(7, 8), adder(8, 7))
        self.assertEqual(adder(123, 456), adder(456, 123))

    def test_associative_property(self):
        self.assertEqual(adder(2, adder(3, 4)), adder(adder(2, 3), 4))
        self.assertEqual(adder(10, adder(5, 2)), adder(adder(10, 5), 2))

    def test_edge_cases(self):
        self.assertEqual(adder(0, 0), 0)
        self.assertEqual(adder(1, 0), 1)
        self.assertEqual(adder(0, 1), 1)

    def test_power_of_two(self):
        self.assertEqual(adder(2, 2), 4)
        self.assertEqual(adder(4, 4), 8)
        self.assertEqual(adder(8, 8), 16)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(resultclass=TestResultFormatter, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
