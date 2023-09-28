# TODO: create files which will serve the functions of output matching, mapping of files to roll numbers, and question numbers.

import os
import sys
import csv

import cppTools as cpp
from possible_status import *

# Default Values
submission_folder: str = 'submissions'
input_files_folder: str = 'sample_input'
saved_output_files_folder: str = 'saved_output'
output_files_folder: str = 'sample_output'
plagi_check: bool = True
cpp.debug = False
no_checking_output: bool = False
clean_enabled: bool = True
timeout_seconds: float = 10.0
# ------------------------------

file_dir = os.path.dirname(os.path.abspath(__file__))


def clean():
    cpp.dbg(f"Cleaning dir: {os.getcwd()}")
    os.system(f"{file_dir}/clean.bat >nul 2>&1")


def print_help():
    print("usage: judge [<options>] [folder-path]")
    print(
        f"\tfolder-path is the path of the directory containing 2 sub-directories '{submission_folder}' and '{input_files_folder}'")
    print(f"\t{submission_folder} contain the submission files")
    print(f"\t{input_files_folder} contain the input files")

    print("\nDefaults:")
    print(f"\tPlagiarism_check: \t{plagi_check}")
    print(f"\tClean: \t\t\tTrue")
    print()

    print("Possible options:")
    print("\t--help, -h\t\tshow help")
    print("\t-t\t\t\tset timeout in seconds (can be a fractional value)")
    print("\t\t\t\tsyntax: -t=\"seconds\"")
    print("\t\t\t\texample: using -t=\"10.5\" gives a timeout of 10.5 seconds")
    print("\t--clean, -c\t\tcleans the submissions directory of exe & judge files")
    print("\t--no-clean, -nc\t\tdisables cleaning")
    print("\t--no-plagi-check, -np\tdisables plagiarism report generation")
    print("\t--no-output-check, -noc\tdisables output checking feature")
    print("\t--debug, -d\t\tenables debug prints")
    print("\t--plagi-check, -p\tenables plagiarism report generation")
    # print("\nREADME:")
    # with open('readme.md') as helpFile:
    #     print(helpFile.read())
    print("\nVisit this Github Page for more info:\nhttps://github.com/ShivanshuKGupta/Lab_Submissions_Checker")


def show_fatal_err(msg: str, err_code=1):
    print(f"error: {msg}")
    exit(err_code)


folder = ""

for arg in sys.argv[1:]:
    if (arg == '-h' or arg == '--help'):
        print_help()
        exit(0)
    elif (arg == '--clean' or arg == '-c'):
        clean()
        exit(0)
    elif (arg == '--no-clean' or arg == '-nc'):
        clean_enabled = False
    elif (arg == '--debug' or arg == '-d'):
        cpp.debug = True
    elif (arg == '--plagi-check' or arg == '-p'):
        plagi_check = True
    elif (arg == '--no-output-check' or arg == '-noc'):
        no_checking_output = True
    elif (arg == '--no-plagi-check' or arg == '-np'):
        plagi_check = False
    elif (arg == '.'):
        folder = os.getcwd()
    elif (arg.startswith("-t=")):
        timeout_seconds = float(arg[3:])
        cpp.dbg(f"Setting timeout to {timeout_seconds} seconds")
    else:
        if arg.startswith('-'):
            print(f"argument \'{arg}\' is not a valid option")
            print_help()
            exit(1)
        else:
            folder = arg

if (len(folder) == 0):
    folder = input(f"Enter folder path [default={os.getcwd()}]:")

if (len(folder.strip()) == 0):
    folder = os.getcwd()

os.chdir(f'{folder}')

if (not os.path.exists(submission_folder)):
    show_fatal_err('Submissions folder not found')

if (not os.path.exists(input_files_folder) and not no_checking_output):
    show_fatal_err('Input folder not found')

if (not os.path.exists(output_files_folder) and not no_checking_output):
    print(
        'Output files aren\'t found. Continuing without output files')

if (clean_enabled):
    clean()
print(f"Running judge on {folder}...")
if (cpp.debug == False):
    print("Debug messages are disabled. Run judge with -d flag to enable debug messages.")

if not no_checking_output:
    if (not os.path.exists(saved_output_files_folder)):
        os.mkdir(f"{saved_output_files_folder}")

    for each_input_file in os.listdir(input_files_folder):
        newFolder = f"{saved_output_files_folder}/{each_input_file[0:len(each_input_file)-4]}"
        if (not os.path.exists(newFolder)):
            os.mkdir(newFolder)

    output_matching: list[dict[str, str]] = []

    i = -1
    for each_submission in os.listdir(submission_folder):
        try:
            submission = cpp.srcFile(each_submission, submission_folder)
        except ValueError as err:
            cpp.showErr(err)
            print(f'Skipping {each_submission}')
            continue
        i += 1
        output_matching.append({
            'file_name': each_submission,
            'status': possible_status.Unknown
        })
        if (submission.compile()):
            for each_input_file in os.listdir(input_files_folder):
                ip_file = f'{input_files_folder}/{each_input_file}'
                submission.setInputFile(ip_file)
                op_file = f"{saved_output_files_folder}/{each_input_file[0:len(each_input_file)-4]}/{submission.file_name_without_ext}.txt"
                submission.setOutputFile(op_file)
                try:
                    if (not submission.run(timeout_seconds=timeout_seconds)):
                        output_matching[i]['status'] = possible_status.Time_Limit_Exceeded
                        continue
                except:
                    output_matching[i]['status'] = possible_status.RunTime_Error
                    print(
                        f"Runtime error occured when running {each_submission} against {each_input_file}.")
                    continue
                correct_op_file = f"{output_files_folder}/{each_input_file}"
                output_matching[i]['status'] = possible_status.Correct if submission.check_against(
                    correct_op_file) else possible_status.Wrong
        else:
            output_matching[i]['status'] = possible_status.Compile_Error
            print(f'Skipping {each_submission}')
            continue

    cpp.dbg(f"{output_matching=}")
    csv_filename = 'submission_status.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['file_name', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_matching)
    print(f'Data has been written to {csv_filename}')

    # TODO: Make copies based on input files and whether they matched output or not

os.chdir(f'..')
if (plagi_check):
    if (clean_enabled):
        clean()
    cpp.dbg("Checking Plagiarism...")
    os.system(
        f"python {file_dir}/Plagi_Checker/main.py {folder}/{submission_folder}")
