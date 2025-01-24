import unittest

class TestResultFormatter(unittest.TextTestResult):
    def startTest(self, test):
        print(f"Running test: \033[1;33m{test}\033[0m")
        # super().startTest(test)

    def addSuccess(self, test):
        print(f"\033[1;32m✓ TEST PASSED! 🎉\033[0m\n")
        # super().addSuccess(test)

    def addFailure(self, test, err):
        print(f"\033[1;31m✗ {test} FAILED ❌\033[0m")
        super().addFailure(test, err)

    def addError(self, test, err):
        print(f"\033[1;31m⚠ {test} ERROR\033[0m")
        super().addError(test, err)
