import sys
import os
import unittest
from io import StringIO
from test_result_formatter import TestResultFormatter

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex05 import negation_normal_form

class TestNegationNormalForm(unittest.TestCase):

    def test_and_operator(self):
        self.assertEqual(
            negation_normal_form('AB&!'),
            "A!B!|",
            "Failed: The expression 'AB&!' should transform to 'A!B!|' in NNF"
        )

    def test_or_operator(self):
        self.assertEqual(
            negation_normal_form('AB|!'),
            "A!B!&",
            "Failed: The expression 'AB|!' should transform to 'A!B!&' in NNF"
        )

    def test_not_operator(self):
        self.assertEqual(
            negation_normal_form('A!'),
            "A!",
            "Failed: The expression 'A!' should remain unchanged as 'A!' in NNF"
        )

    def test_xor_operator(self):
        self.assertEqual(
            negation_normal_form('AB^!'),
            "AB&A!B!&|",
            "Failed: The expression 'AB^!' should transform to 'AB&A!B!&|' in NNF"
        )

    def test_implication_operator(self):
        self.assertEqual(
            negation_normal_form('AB>!'),
            "AB!&",
            "Failed: The expression 'AB>!' should transform to 'AB!&' in NNF"
        )

    def test_equivalence_operator(self):
        self.assertEqual(
            negation_normal_form('AB=!'),
            "A!B!|AB|&",
            "Failed: The expression 'AB=!' should transform to 'A!B!|AB|&' in NNF"
        )

    def test_complex_expression(self):
        self.assertEqual(
            negation_normal_form('ABC&|!'),
            "A!B!C!|&",
            "Failed: The expression 'ABC&|!' should transform to 'A!B!C!|&' in NNF"
        )

    def test_nested_expression(self):
        self.assertEqual(
            negation_normal_form('AB&C!&'),
            "AB&C!&",
            "Failed: The expression 'AB&C!&' should remain unchanged in NNF"
        )

    def test_invalid_expression(self):
        with self.assertRaises(ValueError) as context:
            negation_normal_form('')
        self.assertEqual(
            str(context.exception),
            "Invalid RPN expression: it must form exactly one complete expression.",
            "Failed: Empty expression should raise a valid error message"
        )

        with self.assertRaises(ValueError) as context:
            negation_normal_form('A&')
        self.assertEqual(
            str(context.exception),
            "Not enough operands on stack.",
            "Failed: Expression 'A&' should raise an insufficient operands error"
        )

        with self.assertRaises(ValueError) as context:
            negation_normal_form('AA&')
        self.assertEqual(
            str(context.exception),
            "Duplicate letters found in the expression.",
            "Failed: Expression 'AA&' should raise duplicate letters error"
        )

        with self.assertRaises(ValueError) as context:
            negation_normal_form('AB')
        self.assertEqual(
            str(context.exception),
            "Invalid RPN expression: it must form exactly one complete expression.",
            "Failed: Expression 'AB' should raise a valid error message"
        )

if __name__ == "__main__":
    runner = unittest.TextTestRunner(resultclass=TestResultFormatter, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
