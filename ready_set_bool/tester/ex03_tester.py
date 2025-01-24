import sys
import os
import unittest
from test_result_formatter import TestResultFormatter

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex03 import eval_formula

class TestEvalFormulaFunction(unittest.TestCase):

    # Basic operator tests
    def test_eval_formula_and(self):
        self.assertFalse(eval_formula("10&"), "10& should evaluate to False")
        self.assertTrue(eval_formula("11&"), "11& should evaluate to True")
        self.assertFalse(eval_formula("00&"), "00& should evaluate to False")
        self.assertFalse(eval_formula("01&"), "01& should evaluate to False")

    def test_eval_formula_or(self):
        self.assertTrue(eval_formula("10|"), "10| should evaluate to True")
        self.assertTrue(eval_formula("11|"), "11| should evaluate to True")
        self.assertFalse(eval_formula("00|"), "00| should evaluate to False")
        self.assertTrue(eval_formula("01|"), "01| should evaluate to True")

    def test_eval_formula_greater_than(self):
        self.assertTrue(eval_formula("11>"), "11> should evaluate to True")
        self.assertFalse(eval_formula("10>"), "10> should evaluate to False")
        self.assertFalse(eval_formula("01>"), "01> should evaluate to False")
        self.assertFalse(eval_formula("00>"), "00> should evaluate to False")

    def test_eval_formula_equal(self):
        self.assertFalse(eval_formula("10="), "10= should evaluate to False")
        self.assertTrue(eval_formula("11="), "11= should evaluate to True")
        self.assertTrue(eval_formula("00="), "00= should evaluate to True")
        self.assertFalse(eval_formula("01="), "01= should evaluate to False")

    # Complex expressions
    def test_eval_formula_complex(self):
        self.assertTrue(eval_formula("1011||="), "1011||= should evaluate to True")
        self.assertFalse(eval_formula("1000&&="), "1000&&= should evaluate to False")
        self.assertTrue(eval_formula("1101||>"), "1101||> should evaluate to True")
        self.assertFalse(eval_formula("1001&&>"), "1001&&> should evaluate to False")

    # Edge cases
    def test_eval_formula_edge_cases(self):
        self.assertFalse(eval_formula(""), "Invalid RPN expression: it must contain at least two operands and one operator, and be well-formed.")
        self.assertTrue(eval_formula("1"), "Single '1' should evaluate to True")
        self.assertFalse(eval_formula("0"), "Single '0' should evaluate to False")
        self.assertFalse(eval_formula("000000&"), "All zeroes should evaluate to False")
        self.assertTrue(eval_formula("111111|"), "All ones should evaluate to True")

    # Invalid input tests
    def test_eval_formula_invalid_input(self):
        with self.assertRaises(ValueError, msg="Invalid character should raise ValueError"):
            eval_formula("102&")  # Non-binary character
        with self.assertRaises(ValueError, msg="Unmatched operators should raise ValueError"):
            eval_formula("10&&")  # Consecutive operators
        with self.assertRaises(ValueError, msg="Unmatched operators should raise ValueError"):
            eval_formula("&10")  # Leading operator
        with self.assertRaises(ValueError, msg="Invalid formula should raise ValueError"):
            eval_formula("11=")  # Extra characters at the end
        with self.assertRaises(ValueError, msg="Odd number of operands should raise ValueError"):
            eval_formula("101")  # Odd operands without operator

    # Long input tests
    def test_eval_formula_large_input(self):
        self.assertTrue(eval_formula("1" * 100 + "0" * 100 + "|"), "Long OR operation should evaluate to True")
        self.assertFalse(eval_formula("0" * 200 + "&"), "Long AND operation with zeroes should evaluate to False")
        self.assertTrue(eval_formula("1" * 200 + "&"), "Long AND operation with ones should evaluate to True")


if __name__ == "__main__":
    runner = unittest.TextTestRunner(resultclass=TestResultFormatter, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
