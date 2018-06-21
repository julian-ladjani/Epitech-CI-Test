#!/usr/bin/python3

import unittest
import executetest


class TestObjdumpExecutableFile(unittest.TestCase):

    def test_output_diff_hard_test_objdump_exe(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "my_objdump")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("objdump", "-fs my_objdump")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout == self.gnustdout)

    def test_output_diff_hard_test_multiple_file(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "my_objdump my_nm")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("objdump", "-fs my_objdump my_nm")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout == self.gnustdout)

    def test_output_diff_hard_test_nm_exe(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "my_nm")
        self.gnureturn_value, self.gnustdout, self.gnustderr = executetest.execute_program("objdump", "-fs my_nm")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout == self.gnustdout)


if __name__ == '__main__':
    executetest.execute_test()
