import sys
import os
import unittest
from test_result_formatter import TestResultFormatter
from io import StringIO

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex04 import print_truth_table

class TestPrintTruthTable(unittest.TestCase):

    def capture_output(self, expression):
        """Helper function to capture printed output"""
        captured_output = StringIO()
        sys.stdout = captured_output
        print_truth_table(expression)
        sys.stdout = sys.__stdout__  # Reset stdout
        return captured_output.getvalue().strip()

    def test_and_operator(self):
        output = self.capture_output("AB&")
        expected_output = """| A | B | = |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |"""
        self.assertEqual(output, expected_output, "AB& should produce the correct AND truth table")

    def test_or_operator(self):
        output = self.capture_output("AB|")
        expected_output = """| A | B | = |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |"""
        self.assertEqual(output, expected_output, "AB| should produce the correct OR truth table")

    def test_xor_operator(self):
        output = self.capture_output("AB^")
        expected_output = """| A | B | = |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |"""
        self.assertEqual(output, expected_output, "AB^ should produce the correct XOR truth table")

    def test_implication_operator(self):
        output = self.capture_output("AB>")
        expected_output = """| A | B | = |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |"""
        self.assertEqual(output, expected_output, "AB> should produce the correct implication truth table")

    def test_equivalence_operator(self):
        output = self.capture_output("AB=")
        expected_output = """| A | B | = |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |"""
        self.assertEqual(output, expected_output, "AB= should produce the correct equivalence truth table")

    def test_not_operator(self):
        output = self.capture_output('A!')
        expected_output = """| A | = |
|---|---|
| 0 | 1 |
| 1 | 0 |"""
        self.assertEqual(output, expected_output, "A! should produce the correct NOT truth table")

    def test_complex_expression(self):
        output = self.capture_output("AB|C&")
        expected_output = """| A | B | C | = |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |"""
        self.assertEqual(output, expected_output, "AB|C& should produce the correct complex truth table")

    def test_invalid_expression(self):
        output = self.capture_output("")
        self.assertEqual(output, "Invalid RPN expression: it must contain a valid number of operands and operators, and be well-formed.")

        output = self.capture_output("A&")
        self.assertEqual(output, "Invalid RPN expression: it must contain a valid number of operands and operators, and be well-formed.")

        output = self.capture_output("AB&|")
        self.assertEqual(output, "Invalid RPN expression: it must contain a valid number of operands and operators, and be well-formed.")

        output = self.capture_output("AAB&")
        self.assertEqual(output, "Invalid RPN expression: it must contain a valid number of operands and operators, and be well-formed.")

        output = self.capture_output("AA&")
        self.assertEqual(output, "Duplicate letters found in the expression.")

if __name__ == "__main__":
    runner = unittest.TextTestRunner(resultclass=TestResultFormatter, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
