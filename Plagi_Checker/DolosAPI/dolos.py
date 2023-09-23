"""Dolos API _ provides a dolos class for easy and effective usage of dolos"""

import os


class dolos:
    language: str = ""
    """ <language> Programming language used in the submitted files. Or 'chars' to do a character by character comparison. Detect automatically if not given. Currently Supported Languages JavaScript, Java, Python, C, C#, Bash, cpp"""

    max_fingerprint_count: int = -1
    """ <integer> The _m option sets the maximum number of times a given fingerprint may appear before it is ignored. A code fragment that appears in many programs is probably legitimate sharing and not the result of plagiarism. With _m N any fingerprint appearing in more than N programs is filtered out. This option has precedence over the _M option, which is set to 0.9 by default. """

    max_fingerprint_percentage: float = -1
    """ <fraction>  _M option sets how many percent of the files the fingerprint may appear in before it is ignored. A fingerprint that appears in many programs is probably a legitimate fingerprint and not the result of plagiarism. With _M N any fingerprint appearing in more than N percent of the files is filtered out. Must be a value between 0 and 1. This option is ignored when comparing only two files, because each match appear in 100% of the files"""

    limit_results: int = -1
    """ <integer> Specifies how many matching file pairs are shown in the result. All pairs are shown when this option is omitted.   """

    min_fragment_length: int = -1
    """ <integer> The minimum amount of kgrams a fragment should contain. Every fragment with less kgrams then the specified amount is filtered out. (default: 0)"""

    compare: str = ""
    """ Print a comparison of the matching fragments even if analysing more than two files. Only valid when the output is set to 'terminal' or 'console'. """

    min_similarity: float = -1
    """ <fraction> The minimum similarity between two files. Must be a value between 0 and 1  """

    output_format: str = ""
    """ <format> Specifies what format the output should be in, current options are: terminal/console, csv, html/web. (default:"terminal")  """

    port: str = ""
    """ <port> Specifies on which port the webserver should be served."""

    host: str = ""
    """ <host> Specifies on which host output_format=web should be served."""

    output_destination: str = ""
    """ <path> Path where to write the output report to. This has no effect when the output format is set to 'terminal'.  """

    no_open: bool = False
    """ True - Do not open the web page in your browser once it is ready."""

    sort_by: str = ""
    """ <field> Which field to sort the pairs by. Options are: similarity, total overlap, and longest fragment (default: "total overlap")"""

    fragment_sort_by: str = ""
    """ <sort> How to sort the fragments by the amount of matches, only applicable in terminal comparison output. The options are: 'kgrams ascending', 'kgrams descending' and 'file order' (default: "file order")"""

    kgram_length: int = -1
    """ <integer> The length of each kgram fragment. (default: 23)"""

    kgrams_in_window: int = -1
    """ <integer> The size of the window that will be used (in kgrams). (default: 17)"""

    path: str = ""
    """ <file_names_separated_by_spaces> Input file(s) for the analysis. Can be a list of source code files, a CSV-file, or a zip-file with a top level info.csv file."""

    @classmethod
    def run(cls):
        cmd = "dolos run"

        if (len(cls.language) != 0):
            cmd += f" -l {cls.language}"

        if (cls.max_fingerprint_count != -1):
            cmd += f" -m {cls.max_fingerprint_count}"

        if (cls.max_fingerprint_percentage != -1):
            cmd += f" -M {cls.max_fingerprint_percentage}"

        if (cls.limit_results != -1):
            cmd += f" -L {cls.limit_results}"

        if (cls.min_fragment_length != -1):
            cmd += f" -s {cls.min_fragment_length}"

        if (len(cls.compare) != 0):
            cmd += f" -c {cls.compare}"

        if (cls.min_similarity != -1):
            cmd += f" -S {cls.min_similarity}"

        if (len(cls.output_format) != 0):
            cmd += f" -f {cls.output_format}"

        if (len(cls.port) != 0):
            cmd += f" -p {cls.port}"

        if (len(cls.host) != 0):
            cmd += f" -H {cls.host}"

        if (len(cls.output_destination) != 0):
            cmd += f" -o {cls.output_destination}"

        if (cls.no_open != False):
            cmd += f" --no-open {cls.no_open}"

        if (len(cls.sort_by) != 0):
            cmd += f" --sort-by {cls.sort_by}"

        if (len(cls.fragment_sort_by) != 0):
            cmd += f" -b {cls.fragment_sort_by}"

        if (cls.kgram_length != -1):
            cmd += f" -k {cls.kgram_length}"

        if (cls.kgrams_in_window != -1):
            cmd += f" -w {cls.kgrams_in_window}"
        cmd += " " + cls.path

        print(f"cwd: ", os.getcwd())

        print(f"Running command: '{cmd}'")
        errCode = os.system(cmd)

        if (errCode != 0):
            print(f"error code: {errCode}")

        return errCode
