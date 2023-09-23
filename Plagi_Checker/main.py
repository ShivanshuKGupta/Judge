import shutil
import os
import sys
from DolosAPI.dolos import dolos


if (shutil.which("npm") is None):  # npm is not installed then
    print("npm is not installed. Please install node from https://nodejs.org/ then run this script.")
    exit(0)


if (shutil.which("dolos") is None):  # dolos is not installed then
    if (input("Dolos is not installed. Would you like to install it now? (y/n)").lower() == 'y'):
        os.system("npm install -g @dodona/dolos")
    else:
        print("Exiting...")
        exit(0)

path = None

if (len(sys.argv) > 1):
    path = sys.argv[1]

if (path is None):
    path = os.getcwd()

# if (len(path) == 0):
#     print("How to use?")
#     print("Create a folder let us say 'submissions' copy all .c/.cpp files there.")
#     print("Finally just enter that folder path down here.")

#     path = input("Enter the submissions folder path:")

os.chdir(path)

with open("inputFiles.csv", "w") as file:
    file.write("filename"+'\n')
    for each_input_file in os.listdir(path):
        if (not each_input_file.endswith('.csv')):
            file.write(path + "\\"+each_input_file+'\n')

dolos.output_format = "web"
dolos.port = "8080"
dolos.output_destination = f"Dolos_Reports"
dolos.path = f"inputFiles.csv"
dolos.language = "cpp"
dolos.min_similarity = 0.5
dolos.sort_by = "similarity"
print(f"See generated report here: {path}\\Dolos_Reports\\pairs.csv")
try:
    errCode = dolos.run()
    if (errCode != 0):
        print("Plagiarism Check Failed with error code: ", errCode)
except KeyboardInterrupt:
    pass

try:
    os.remove('inputFiles.csv')
except:
    print("Error removing inputFile.csv")
