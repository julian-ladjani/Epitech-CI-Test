#!/usr/bin/python3

import unittest
import executetest


class TestObjdumpErrorCheck(unittest.TestCase):

    def test_file_format_not_recognized(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "/var/log/syslog")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("my_objdump: /var/log/syslog: File format not recognized") >= 0)

    def test_file_format_no_arg(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("my_objdump: 'a.out': No such file") >= 0)

    def test_file_format_wrong_file(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "wrong_file")
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("my_objdump: 'wrong_file': No such file") >= 0)

if __name__ == '__main__':
    executetest.execute_test()
