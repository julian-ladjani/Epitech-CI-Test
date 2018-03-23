#!/usr/bin/python3

import unittest
import executetest


class TestTwoPhilosophersOneEatCycleCase(unittest.TestCase):
    def setUp(self):
        self.eat_cycle = "1"
        self.philosophers = "2"
        self.total_eat_time = str(int(self.eat_cycle) * int(self.philosophers))
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./philo",
                                                                                  "-p " + self.philosophers + " -e " + self.eat_cycle)

    def test_played_game_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Played game: 1/1") != -1, self.stdout)

    def test_philosophers_used_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Philos used: " + self.philosophers + "/" + self.philosophers) != -1)

    def test_eat_cycle_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Eat Cycles: " + self.eat_cycle + "/" + self.eat_cycle) != -1)

    def test_system_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("System Inconsistences found: 0") != -1)

    def test_logical_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Logical Inconsistences found: 0") != -1)

    def test_philosophers_total_eat_cycle(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Total Philos: \n\tEaten " + self.total_eat_time + " times") != -1)


class TestTenPhilosophersTenEatCycleCase(unittest.TestCase):
    def setUp(self):
        self.eat_cycle = "10"
        self.philosophers = "10"
        self.total_eat_time = str(int(self.eat_cycle) * int(self.philosophers))
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./philo",
                                                                                  "-p " + self.philosophers + " -e " + self.eat_cycle)

    def test_played_game_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Played game: 1/1") != -1, self.stdout)

    def test_philosophers_used_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Philos used: " + self.philosophers + "/" + self.philosophers) != -1)

    def test_eat_cycle_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Eat Cycles: " + self.eat_cycle + "/" + self.eat_cycle) != -1)

    def test_system_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("System Inconsistences found: 0") != -1)

    def test_logical_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Logical Inconsistences found: 0") != -1)

    def test_philosophers_total_eat_cycle(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Total Philos: \n\tEaten " + self.total_eat_time + " times") != -1)


class TestFortyPhilosophersOneHundredEatCycleCase(unittest.TestCase):
    def setUp(self):
        self.eat_cycle = "100"
        self.philosophers = "40"
        self.total_eat_time = str(int(self.eat_cycle) * int(self.philosophers))
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./philo",
                                                                                  "-p " + self.philosophers + " -e " + self.eat_cycle)

    def test_played_game_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Played game: 1/1") != -1)

    def test_philosophers_used_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Philos used: " + self.philosophers + "/" + self.philosophers) != -1)

    def test_eat_cycle_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Eat Cycles: " + self.eat_cycle + "/" + self.eat_cycle) != -1)

    def test_system_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("System Inconsistences found: 0") != -1)

    def test_logical_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Logical Inconsistences found: 0") != -1)

    def test_philosophers_total_eat_cycle(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Total Philos: \n\tEaten " + self.total_eat_time + " times") != -1)


class TestOneHundredPhilosophersFortyEatCycleCase(unittest.TestCase):
    def setUp(self):
        self.eat_cycle = "40"
        self.philosophers = "100"
        self.total_eat_time = str(int(self.eat_cycle) * int(self.philosophers))
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./philo",
                                                                                  "-p " + self.philosophers + " -e " + self.eat_cycle)

    def test_played_game_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Played game: 1/1") != -1)

    def test_philosophers_used_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Philos used: " + self.philosophers + "/" + self.philosophers) != -1)

    def test_eat_cycle_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Eat Cycles: " + self.eat_cycle + "/" + self.eat_cycle) != -1)

    def test_system_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("System Inconsistences found: 0") != -1)

    def test_logical_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Logical Inconsistences found: 0") != -1)

    def test_philosophers_total_eat_cycle(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Total Philos: \n\tEaten " + self.total_eat_time + " times") != -1)


class TestOneHundredPhilosophersOneHundredEatCycleCase(unittest.TestCase):
    def setUp(self):
        self.eat_cycle = "100"
        self.philosophers = "100"
        self.total_eat_time = str(int(self.eat_cycle) * int(self.philosophers))
        self.return_value, self.stdout, self.stderr = executetest.execute_program("./philo",
                                                                                  "-p " + self.philosophers + " -e " + self.eat_cycle)

    def test_played_game_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Played game: 1/1") != -1)

    def test_philosophers_used_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Philos used: " + self.philosophers + "/" + self.philosophers) != -1)

    def test_eat_cycle_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Eat Cycles: " + self.eat_cycle + "/" + self.eat_cycle) != -1)

    def test_system_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("System Inconsistences found: 0") != -1)

    def test_logical_inconsistences_number(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Logical Inconsistences found: 0") != -1)

    def test_philosophers_total_eat_cycle(self):
        if self.return_value == -1 and self.stderr == "Timeout Reached":
            self.fail("Timeout Reached")
        self.assertTrue(self.stdout.find("Total Philos: \n\tEaten " + self.total_eat_time + " times") != -1)


if __name__ == '__main__':
    executetest.execute_test()
