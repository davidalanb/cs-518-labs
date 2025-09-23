import unittest
import sys
import os

'''
Add the src directory to path so that imports will work
this assumes that the src directory is adjacent to this file
'''
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(FILE_PATH, 'src')
sys.path.append(SRC_DIR)

def discover_and_run_tests(directory):
    """
    Discovers all tests in a given directory and runs them.

    Args:
        directory (str): The path to the directory containing test files.
    """
    # Ensure the provided directory exists and is a directory
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)

    # Use TestLoader.discover() to find all tests
    # The 'start_dir' is the directory to start searching from.
    # The 'pattern' is the file name pattern to match for test files.
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir=directory, pattern='test_*.py')

    # Run the discovered test suite
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == '__main__':
    # You can specify the directory to test here.
    # '.' means the current working directory.
    tests_directory = './tests'
    
    # Alternatively, you can take a command-line argument for the directory:
    # if len(sys.argv) > 1:
    #     tests_directory = sys.argv[1]

    discover_and_run_tests(tests_directory)