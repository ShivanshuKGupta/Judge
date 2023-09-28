import os
import subprocess
from timeout_decorator import timeout


debug = False


def showErr(errMsg: str):
    print(errMsg)


def dbg(msg):
    global debug
    if debug:
        print(msg)


class srcFile:
    def __init__(self, _file_name: str, _folder: str):
        self.folder = _folder
        self.file_name = _file_name
        self.ext = ""
        self.file_name_without_ext = self.file_name[0:len(self.file_name)-2]
        if (self.file_name[len(self.file_name)-2:len(self.file_name)].lower() == '.c'):
            self.ext = ".c"
        elif (self.file_name[len(self.file_name)-4:len(self.file_name)].lower() == '.cpp'):
            self.file_name_without_ext = self.file_name[0:len(
                self.file_name)-4]
            self.ext = ".cpp"
        else:
            raise ValueError(f"Unknown file extension: {self.file_name}")

    def compile(self):
        dbg(f"Compiling {self.file_name} file...")
        try:
            if (self.ext == '.c'):
                if (os.system(f"cd \"{self.folder}\" && gcc \"{self.file_name}\" -o \"{self.file_name_without_ext}\"") != 0):
                    showErr("C File Compilation Failed!")
                    return False
            elif (self.ext == '.cpp'):
                if (os.system(f"cd \"{self.folder}\" && g++ \"{self.file_name}\" -o \"{self.file_name_without_ext}\"") != 0):
                    showErr("C++ File Compilation Failed!")
                    return False
            return True
        except:
            return False

    def setInputFile(self, input_file):
        self.input_file = input_file

    def setOutputFile(self, output_file):
        self.output_file = output_file

    def run(self, timeout_seconds: float = 10) -> bool:
        dbg(f"Running '{self.file_name_without_ext}' for input '{self.input_file}'...")
        try:
            output_file = open(self.output_file, "wb")
            input_file = open(self.input_file, 'r')
            subprocess.run(
                f"{self.folder}\\{self.file_name_without_ext}.exe",
                stdin=input_file,
                stdout=output_file,
                check=True, shell=False, timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            print(
                f"{self.file_name_without_ext}.exe exceeded the time limit of {timeout_seconds} seconds and was terminated.")
            return False
        return True

    def __del__(self):
        try:
            os.system(f"del {self.folder}\\{self.file_name_without_ext}.exe")
        except:
            dbg(
                f"Something went wrong while deleting the file: {self.folder}\\{self.file_name_without_ext}.exe")

    @classmethod
    def compare_outputs(cls, str1: str, str2: str) -> bool:
        str1 = str1.replace('\n', '').split(' ')
        str2 = str2.replace('\n', '').split(' ')
        i = 0
        j = 0
        while (i < len(str1) and j < len(str2)):
            while (len(str1[i]) == 0):
                i += 1
            while (len(str2[j]) == 0):
                j += 1
            if (str1[i] != str2[j]):
                return False
            i += 1
            j += 1
        return True

    def check_against(self, correct_output_file_path: str) -> bool:
        try:
            output_generated = open(self.output_file, "r").read()
        except:
            showErr(f"Cannot open file {self.output_file} with read access.")
            return None
        try:
            correct_output = open(correct_output_file_path, "r").read()
        except:
            showErr(
                f"Cannot open file {correct_output_file_path} with read access.")
            return None
        return srcFile.compare_outputs(output_generated, correct_output)


def setFile(file_name: str, data: str):
    ip = open(file_name, 'w')
    ip.write(data)
    dbg(f"Writing '{data}' in {file_name}")
