#!/usr/bin/python3
import os


def execute_files_in_dir():
    if os.path.isdir("../Tests/" + project_name):
        print(os.path.realpath(os.curdir))
        for path, subdirs, files in os.walk("../Tests/" + project_name):
            for filename in files:
                if filename.endswith('.py'):
                    os.system("python3 " + path + "/" + filename)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.environ["PYTHONPATH"] = os.path.realpath(os.curdir)
    os.system("git pull")
    project_name = os.getenv('PROJECT_NAME', "NO_NAME")
    print(project_name)
    if project_name != "NO_NAME":
        execute_files_in_dir()
