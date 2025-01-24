import sys
import os
import unittest
from test_result_formatter import TestResultFormatter

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex01 import multiplier

class TestMultiplyFunction(unittest.TestCase):

    def test_small_numbers(self):
        self.assertEqual(multiplier(2, 3), 6)
        self.assertEqual(multiplier(1, 1), 1)
        self.assertEqual(multiplier(5, 0), 0)
        self.assertEqual(multiplier(0, 5), 0)

    def test_large_numbers(self):
        self.assertEqual(multiplier(1234, 5678), 7006652)
        self.assertEqual(multiplier(1000, 1000), 1000000)
        self.assertEqual(multiplier(98765, 4321), 426763565)

    def test_identity_property(self):
        self.assertEqual(multiplier(1, 9999), 9999)
        self.assertEqual(multiplier(9999, 1), 9999)

    def test_commutative_property(self):
        self.assertEqual(multiplier(7, 8), multiplier(8, 7))
        self.assertEqual(multiplier(123, 456), multiplier(456, 123))

    def test_associative_property(self):
        self.assertEqual(multiplier(2, multiplier(3, 4)), multiplier(multiplier(2, 3), 4))
        self.assertEqual(multiplier(10, multiplier(5, 2)), multiplier(multiplier(10, 5), 2))

    def test_edge_cases(self):
        self.assertEqual(multiplier(0, 0), 0)
        self.assertEqual(multiplier(1, 0), 0)
        self.assertEqual(multiplier(0, 1), 0)

    def test_power_of_two(self):
        self.assertEqual(multiplier(2, 2), 4)
        self.assertEqual(multiplier(4, 4), 16)
        self.assertEqual(multiplier(8, 8), 64)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(resultclass=TestResultFormatter, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
