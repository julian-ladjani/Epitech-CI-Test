#!/usr/bin/python3

import unittest
import executetest


class TestObjdumpHeaderSimpleExecutableFile(unittest.TestCase):

    def setUp(self):
        print("setup")

    def test_file_format(self):
        exec_return_value, stdout, stderr = executetest.execute_program("./my_objdump", "my_objdump")
        self.assertTrue(stdout.contains("\nmy_objdump:     file format elf64-x86-64\n"))

    def test_file_architecture(self):
        exec_return_value, stdout, stderr = executetest.execute_program("./my_objdump", "my_objdump")
        self.assertTrue(stdout.contains("\narchitecture: i386:x86-64, flags 0x00000150:\n"))

    def test_file_flags(self):
        exec_return_value, stdout, stderr = executetest.execute_program("./my_objdump", "my_objdump")
        self.assertTrue(stdout.contains("\nHAS_SYMS, DYNAMIC, D_PAGED\n"))

    def test_start_address(self):
        exec_return_value, stdout, stderr = executetest.execute_program("./my_objdump", "my_objdump")
        self.assertTrue(stdout.contains("\nstart address 0x0000000000000a80\n\n"))


if __name__ == '__main__':
    executetest.execute_test()
