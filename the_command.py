#!/usr/bin/env python3

import datetime
from random import randint
import os
import sys


BASE_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))


def write_file(file_path, data=""):
    true_path = os.path.abspath(os.path.join(BASE_PATH, file_path))
    os.makedirs(os.path.dirname(true_path), exist_ok=True)

    with open(true_path, "w") as fh:
        fh.write(data)


def write_files(paths, data=""):
    for path in paths:
        write_file(path, data)


def ts():
    return datetime.datetime.now()


def random_name(names):

    return names[randint(0, len(names)-1)]


def random_path():
    files = ["fluorescence", "coagulation", "haematocrit"]
    folders = ["single_test", "metrics", "mock"]

    path_components = []

    for _ in range(1,3):
        path_components.append(random_name(folders))

    path_components.append(random_name(files))

    return os.path.sep.join(path_components)


def main():
    # All data is dummy data, of course.
    write_file("test_results.xml", '<?xml encoding="utf-8"><rootTag/>')

    write_files(["logs/general.log", "logs/specific.log"], str(ts())+" Created another file!")

    if randint(1,3) == 1:
        paths = []
        for _ in range(1,5):
            paths.append(random_path()+".csv")

        write_files(paths, str(ts()))

        return 1

    return 0


if __name__ == "__main__":
    code = main()
    print(f"Exit {code}")
    exit(code)
