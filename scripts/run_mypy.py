import os
from os.path import join


def divider():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def file_needs_to_be_checked(file):
    return file.endswith(".py") and file != "__init__.py"


def mypy(file_path):
    os.system("mypy --ignore-missing-imports " + file_path)


for root, dirs, files in os.walk('.'):
    for file in files:
        if file_needs_to_be_checked(file):
            divider()
            full_path = join(root, file)
            print("Analyzing " + full_path)
            mypy(full_path)
divider()
