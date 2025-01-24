import unittest
import os

# Define the test folder path
TEST_DIR = os.path.dirname(os.path.abspath(__file__))

def run_tests():
    # Discover and run all test cases in the 'tester' folder
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add individual test files to the test suite
    test_files = [
        "ex00_tester.py",
        "ex01_tester.py",
        "ex02_tester.py"
    ]

    for test_file in test_files:
        if os.path.exists(test_file):
            # Load tests from each test file
            module_name = test_file.replace("/", ".").replace(".py", "")
            tests = loader.loadTestsFromName(module_name)
            suite.addTests(tests)

    # Run the tests with verbosity and custom result formatting
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("\033[1;32mAll tests passed successfully! 🎉\033[0m")
        exit(0)
    else:
        print("\033[1;31mSome tests failed. ❌\033[0m")
        exit(1)

if __name__ == "__main__":
    run_tests()
