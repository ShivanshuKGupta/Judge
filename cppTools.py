import os


def showErr(errMsg: str):
    print(errMsg)
    exit(1)


class srcFile:
    def __init__(self, _file_name: str, _folder: str):
        self.folder = _folder
        self.file_name = _file_name
        self.ext = ""
        self.file_name_without_ext = self.file_name[0:len(self.file_name)-2]
        if (self.file_name[len(self.file_name)-2:len(self.file_name)] == '.c'):
            self.ext = ".c"
        elif (self.file_name[len(self.file_name)-4:len(self.file_name)] == '.cpp'):
            self.file_name_without_ext = self.file_name[0:len(
                self.file_name)-4]
            self.ext = ".cpp"
        else:
            showErr(f"Unknown file extension: {self.file_name}")

    def compile(self):
        print(f"Compiling {self.file_name} file...")
        if (self.ext == '.c'):
            if (os.system(f"cd {self.folder} && gcc {self.file_name} -o {self.file_name_without_ext}") != 0):
                showErr("C File Compilation Failed!")
        elif (self.ext == '.cpp'):
            if (os.system(f"cd {self.folder} && g++ {self.file_name} -o {self.file_name_without_ext}") != 0):
                showErr("C++ File Compilation Failed!")

    def setInputFile(self, input_file):
        self.input_file = input_file

    def setOutputFile(self, output_file):
        self.output_file = output_file

    def run(self):
        print(f"Running '{self.file_name}' for input '{self.input_file}'...")
        os.system(
            f"./{self.folder}/{self.file_name_without_ext} <{self.input_file} >{self.output_file}")

    def __del__(self):
        os.system(f"rm {self.folder}/{self.file_name_without_ext}")


def setFile(file_name: str, data: str):
    ip = open(file_name, 'w')
    ip.write(data)
    print(f"Writing '{data}' in {file_name}")
