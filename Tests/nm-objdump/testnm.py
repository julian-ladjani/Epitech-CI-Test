#!/usr/bin/python3

import random
import unittest
import executetest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_fail(self):
        return_value, stdout, stderr = executetest.execute_program("/bin/ls", "-l")
        error_message = "test stdout with program execution\n"
        error_message += "stdout:\n"
        error_message += stdout
        error_message += "stderr:\n"
        error_message += stderr
        error_message += "return value:\n"
        error_message += str(return_value)
        self.fail(error_message)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


if __name__ == '__main__':
    executetest.execute_test()
