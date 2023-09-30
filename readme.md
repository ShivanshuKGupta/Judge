# Submission Checker

A code checker with a plagiarism detector. Currently, it only supports c and cpp files.

## Pre-requisites

1. gcc/g++, python and npm(to enable plagiarism check [optional])

## Installation

1. run install.bat file.

## How to use?

1. Make a new folder say 'Lab2'.
2. Make two new subfolders: submissions (containing the .c/.cpp files) and sample_input(containing all input files)
3. open the command prompt in the folder 'Lab2'.
4. type ```judge .``` to run.

## What it does?

1. It first asks you the location of the folder where the sub-folders were created.
2. Then for every file in submissions, it compiles it and runs it against every input file present in the folder sample_input.
3. And stores the output a new folder saved_output (will be present in the same folder).
4. Finally, runs dolos on the submission files

## Usage

```
usage: judge [<options>] [folder-path]
        folder-path is the path of the directory containing 2 sub-directories 'submissions' and 'sample_input'
        submissions contain the submission files
        sample_input contain the input files

Defaults:
        Plagiarism_check:       True
        Clean:                  True

Possible options:
        --help, -h              show help
        -t                      set timeout in seconds (can be a fractional value)
                                syntax: -t"<seconds>"
                                example: using '-t"10.5"' gives a timeout of 10.5 seconds
        --clean, -c             cleans the submissions directory of exe & judge files
        --no-clean, -nc         disables cleaning
        --no-plagi-check, -np   disables plagiarism report generation
        --no-output-check, -noc disables output checking feature
        --debug, -d             enables debug prints
        --plagi-check, -p       enables plagiarism report generation
```
