#!/usr/bin/python3

import unittest
import executetest


class TestObjdumpHeaderSimpleExecutableFile(unittest.TestCase):

    def setUp(self):
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./my_objdump", "my_objdump")
        print(self.stdout)

    def test_file_format(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("\nmy_objdump:     file format elf64-x86-64\n") >= 0)

    def test_file_architecture(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("\narchitecture: i386:x86-64, flags 0x00000150:\n"))

    def test_file_flags(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("\nHAS_SYMS, DYNAMIC, D_PAGED\n"))

    def test_start_address(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("\nstart address 0x0000000000000a80\n\n"))


if __name__ == '__main__':
    executetest.execute_test()
