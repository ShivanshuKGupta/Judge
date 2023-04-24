import os
import sys

import cppTools as cpp

# Folder names
submission_folder = 'submissions'
input_files_folder = 'sample_input'
# ------------------------------

if (len(sys.argv) > 1):
    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        with open('readme.md') as helpFile:
            print(helpFile.readlines())
        print('Contact shivanshukgupta (linkedin/github) for help')
    exit(0)

folder = input("Enter folder path:")
os.chdir(f'{folder}')

output_files_folder = 'saved_output'

if (not os.path.exists(submission_folder)):
    print('Submissions folder not found')
    exit(1)

if (not os.path.exists(input_files_folder)):
    print('Input folder not found')
    exit(1)

if (not os.path.exists(output_files_folder)):
    os.mkdir(f"{output_files_folder}")

for each_input_file in os.listdir(input_files_folder):
    newFolder = f"{output_files_folder}/{each_input_file[0:len(each_input_file)-4]}"
    if (not os.path.exists(newFolder)):
        os.mkdir(newFolder)

for each_submission in os.listdir(submission_folder):
    submission = cpp.srcFile(each_submission, submission_folder)
    submission.compile()
    for each_input_file in os.listdir(input_files_folder):
        submission.setInputFile(f'{input_files_folder}/{each_input_file}')
        submission.setOutputFile(
            f"{output_files_folder}/{each_input_file[0:len(each_input_file)-4]}/{submission.file_name_without_ext}.txt")
        submission.run()
