import unittest
import xmlrunner
import os


def execute_test():
    project_dir = os.getenv('PROJECT_DIR', "NO_DIR")
    print(project_dir)
    if project_dir != "NO_DIR":
        os.chdir(project_dir)
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output='test-result'),
            failfast=False, buffer=False, catchbreak=False)
