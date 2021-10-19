# Technical exercise

A short technical exercise.

In this folder, there is a program that mocks up a test runner. When it executes, it:

* produces a `test_results.xml`, always
* a log folder with log files, always
* may return a non-zero exit code
* if it returns non-zero, it will also produce any number of `*.csv` files
    * these will appear along different paths in the working directory.
    * some files may have the same name as another

## The task

* In a first commit, write a script that
    * calls the program using python3,
    * produces a zip of the CSV, log and XML files
    * Sends ZIP file to a URL via HTTP POST
        * The URL is supplied at run time
        * You can mandate how you want that information passed to your script

* Extra conditions
    * Do not include anything that's under a `.../mock/...` path
    * Files should appear at the root of the archive, not down in subfolders
    * The ZIP file should not contain data from previous runs.
    * The ZIP file should be a true ZIP file (not some other format renamed to .zip)

Finally, pull-request your solution to this project.

## The environment

* Linux with the standard utilities
    * Presume any of Debian, CentOS, SuSE, etc
* bash 5 is available
* python3 is available
