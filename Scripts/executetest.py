#!/usr/bin/python3

import unittest
import xmlrunner
import os
import subprocess



def execute_program_with_input(program_path, args, program_input):
    p = subprocess.Popen(program_path + " " + args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         stdin=program_input,
                         shell=True)
    try:
        stdout, stderr = p.communicate(timeout=10)
        return p.returncode, stdout, stderr
    except subprocess.TimeoutExpired:
        p.kill()
    return -1, "", "Timeout Reached"


def execute_program(program_path, args):
    p = subprocess.Popen(program_path + " " + args,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         universal_newlines=True,
                         shell=True)
    try:
        stdout, stderr = p.communicate(timeout=10)
        return p.returncode, stdout, stderr
    except subprocess.TimeoutExpired:
        p.kill()
    return -1, "", "Timeout Reached"


def execute_test():
    project_dir = os.getenv('PROJECT_DIR', "NO_DIR")
    if project_dir != "NO_DIR":
        os.chdir(project_dir)
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output='test-result'),
            verbosity=False, failfast=False, buffer=False, catchbreak=False)
