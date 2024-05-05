# Judge

A cli tool for code checking with a plagiarism detector. Currently, it only supports c, cpp and python files, but can be easily extended to allow checking for multiple types.

## Pre-requisites

1. python (to run the app)
2. gcc/g++ (to compile C/C++ submission files)
3. npm and visual studio build tools [optional] (to enable plagiarism check)

## Installation

1. run install_judge.bat file with admin privileges.

## How to use?

1. Make a new folder say 'Lab2'.
2. Make 3 new subfolders, ```submissions``` (containing the .c/.cpp files), ```sample_input``` (containing all input files) and ```sample_output``` (containing output files with the same name as the input files).
3. having output files is optional, and is only used to enable output checking.
4. open the command prompt in the folder 'Lab2'.
5. type ```judge .``` to run.

## What it does?

1. It first asks you the location of the folder where the sub-folders were created (if not given as an command line argument).
2. Then for every file in submissions, it compiles it and runs it against every input file present in the folder ```sample_input```.
3. And stores the output a new folder ```saved_output``` (will be present in the same folder).
4. Finally, runs dolos on the submission files (if chosen to run to).
5. You can customize the judge to only run plagiarism check or just to run output checking on files using the command line arguments as instructed below.

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
