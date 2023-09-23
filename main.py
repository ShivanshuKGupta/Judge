import os
import sys

import cppTools as cpp

# Folder names
submission_folder = 'submissions'
input_files_folder = 'sample_input'
output_files_folder = 'saved_output'
plagi_check = True
cpp.debug = False
# ------------------------------

file_dir = os.path.dirname(os.path.abspath(__file__))


def clean(dir=None):
    if dir is None:
        dir = f"{folder}/{submission_folder}"
    cpp.dbg(f"Current dir: {os.getcwd()}")
    cpp.dbg(f"Changing dir to: {dir}")
    os.chdir(f"{dir}")
    os.system(f"{file_dir}/clean.bat")


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
    print("\t--clean, -c\t\tcleans the submissions directory of exe files")
    print("\t--no-clean, -nc\t\tdisables cleaning of the submissions directory from exe files")
    print("\t--no-plagi-check, -np\tdisables plagiarism report generation")
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
    elif (arg == '--no-clean' or arg == '-nc'):
        pass
    elif (arg == '--debug' or arg == '-d'):
        cpp.debug = True
    elif (arg == '--plagi-check' or arg == '-p'):
        plagi_check = True
    elif (arg == '--no-plagi-check' or arg == '-np'):
        plagi_check = False
    elif (arg == '.'):
        folder = os.getcwd()
    else:
        if arg.startswith('-'):
            print(f"argument \'{arg}\' is not a valid option")
            print_help()
            exit(1)
        else:
            folder = arg

if (len(folder) == 0):
    folder = input("Enter folder path:")

os.chdir(f'{folder}')

if (not os.path.exists(submission_folder)):
    show_fatal_err('Submissions folder not found')

if (not os.path.exists(input_files_folder)):
    show_fatal_err('Input folder not found')

if (not os.path.exists(output_files_folder)):
    os.mkdir(f"{output_files_folder}")

for each_input_file in os.listdir(input_files_folder):
    newFolder = f"{output_files_folder}/{each_input_file[0:len(each_input_file)-4]}"
    if (not os.path.exists(newFolder)):
        os.mkdir(newFolder)

print(f"Running judge on {folder}...")
if (cpp.debug == False):
    print("Debug messages are disabled. Run judge with -d flag to enable debug messages.")

for each_submission in os.listdir(submission_folder):
    try:
        submission = cpp.srcFile(each_submission, submission_folder)
    except ValueError as err:
        cpp.showErr(err)
        print(f'Skipping {each_submission}')
        continue
    if (submission.compile()):
        for each_input_file in os.listdir(input_files_folder):
            submission.setInputFile(f'{input_files_folder}/{each_input_file}')
            submission.setOutputFile(
                f"{output_files_folder}/{each_input_file[0:len(each_input_file)-4]}/{submission.file_name_without_ext}.txt")
            submission.run()
    else:
        print(f'Skipping {each_submission}')

clean(dir=submission_folder)
if (plagi_check):
    cpp.dbg("Checking Plagiarism...")
    os.system(
        f"python {file_dir}/Plagi_Checker/main.py")
