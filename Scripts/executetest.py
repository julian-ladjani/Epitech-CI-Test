#!/usr/bin/python3

import unittest
import xmlrunner
import os
import subprocess
from time import sleep


def execute_program_with_input(program_path, args, program_input):
    p = subprocess.Popen(program_path + " " + args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=program_input,
                         universal_newlines=True,
                         shell=True)
    while p.poll() is None:
        sleep(.1)
    return p.returncode, p.stdout.read().encode("ascii"), p.stderr.read()


def execute_program(program_path, args):
    p = subprocess.Popen(program_path + " " + args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         shell=True)
    while p.poll() is None:
        sleep(.1)
    return p.returncode, p.stdout.read(), p.stderr.read()


def execute_test():
    project_dir = os.getenv('PROJECT_DIR', "NO_DIR")
    print(project_dir)
    if project_dir != "NO_DIR":
        os.chdir(project_dir)
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output='test-result'),
            verbosity=False, failfast=False, buffer=False, catchbreak=False)
