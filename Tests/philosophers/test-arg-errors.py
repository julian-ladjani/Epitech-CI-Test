#!/usr/bin/python3

import unittest
import executetest


class TestExecutableArgumentErrorCases(unittest.TestCase):

    def test_no_philosopher_number_arg_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-e 3")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_no_eat_max_times_number_arg_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-p 3")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_negative_philosopher_number_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-p -3")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_negative_max_eat_times_number_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-e -3")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_zero_philosopher_number_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-p 0")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_zero_max_eat_times_number_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-e 0")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_too_much_arg_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-p 3 -p 4 -e 5")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 84, str(return_value) + "instead of 84")

    def test_wrong_philosopher_number_error(self):
        return_value, stdout, stderr = executetest.execute_program("./philo", "-p 1 -e 5")
        if return_value == -1 and stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(return_value == 0, str(return_value) + "instead of 0")


if __name__ == '__main__':
    executetest.execute_test()
