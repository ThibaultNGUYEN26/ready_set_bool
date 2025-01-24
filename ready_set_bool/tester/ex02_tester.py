import sys
import os
import unittest
from test_result_formatter import TestResultFormatter

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex02 import gray_code

class TestGrayCodeFunction(unittest.TestCase):

    def test_gray_code_basic(self):
        self.assertEqual(gray_code(0), 0)
        self.assertEqual(gray_code(1), 1)
        self.assertEqual(gray_code(2), 3)
        self.assertEqual(gray_code(3), 2)
        self.assertEqual(gray_code(4), 6)
        self.assertEqual(gray_code(5), 7)
        self.assertEqual(gray_code(6), 5)
        self.assertEqual(gray_code(7), 4)
        self.assertEqual(gray_code(8), 12)

    def test_large_numbers(self):
        self.assertEqual(gray_code(15), 8)
        self.assertEqual(gray_code(16), 24)
        self.assertEqual(gray_code(31), 16)
        self.assertEqual(gray_code(32), 48)

    def test_edge_cases(self):
        self.assertEqual(gray_code(0), 0)
        self.assertEqual(gray_code(1), 1)

    def test_power_of_two(self):
        self.assertEqual(gray_code(16), 24)
        self.assertEqual(gray_code(32), 48)
        self.assertEqual(gray_code(64), 96)


if __name__ == "__main__":
    runner = unittest.TextTestRunner(resultclass=TestResultFormatter, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
