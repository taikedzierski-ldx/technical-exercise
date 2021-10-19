# Technical exercise

A short technical exercise.

In this folder, there is a program that mocks up a test runner. When it executes, it:

* produces a `test_results.xml`, always
* a log folder with log files, always
* may return a non-zero exit code
* if it returns non-zero, it will also produce any number of `*.csv` files
    * these will appear along different paths in the working directory.

The task:

* Write a script that calls this program, and produces a zip of the CSV, log and XML files.
* Add a feature to POST the files to a server.
    * The server is supplied at run time, you should mandate how you want that information passed to your script.

The ZIP file should not contain data from previous runs, so a cleanup at some point should be performed.

The ZIP file should be a true ZIP file (not some other format renamed to .zip)

The environment:

* Linux
    * with `coreutils` and/or `busybox` available
* bash 5 is available
* python3 is available
