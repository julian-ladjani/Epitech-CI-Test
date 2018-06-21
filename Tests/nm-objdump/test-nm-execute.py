#!/usr/bin/python3

import unittest
import string
import executetest


class TestNmExecutableFile(unittest.TestCase):

    def test_output_diff_hard_test_objdump_exe(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_nm", "my_objdump")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("nm", "my_objdump")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.stdout_list = str.split(self.stdout, '\n')
        self.gnustdout_list = str.split(self.gnustdout, '\n')
        self.gnustdout_list.sort()
        self.stdout_list.sort()
        self.assertTrue(self.stdout_list == self.gnustdout_list)

    def test_output_diff_hard_test_multiple_files(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_nm", "my_objdump my_nm")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("nm", "my_objdump my_nm")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.stdout_list = str.split(self.stdout, '\n')
        self.gnustdout_list = str.split(self.gnustdout, '\n')
        self.gnustdout_list.sort()
        self.stdout_list.sort()
        self.assertTrue(self.stdout_list == self.gnustdout_list)

    def test_output_diff_hard_test_nm_exe(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_nm", "my_objdump")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("nm", "my_objdump")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.stdout_list = str.split(self.stdout, '\n')
        self.gnustdout_list = str.split(self.gnustdout, '\n')
        self.gnustdout_list.sort()
        self.stdout_list.sort()
        self.assertTrue(self.stdout_list == self.gnustdout_list)

if __name__ == '__main__':
    executetest.execute_test()
