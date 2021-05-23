from datetime import datetime
import pathlib
import platform
import time
import logging

windows_extensions = {
    ".bat",
    ".dll",
    ".cmd",
    ".cpl",
    ".exe",
    ".ps1",
    ".inf1",
    ".sct",
    ".vbs",
    ".vb",
    ".hta",
    ".msi",
    ".htm",
    ".wll",
    ".txt",
    ".dotm",
    ".html",
    ".doc",
    ".docx",
    ".docm",
    ".txt",
    ".tgz",
    ".rar",
    ".dotm",
    ".bmp",
    ".jpeg",
    ".img",
}


def check_file_time(ftime):
    """This function adds a date and time to the 'Last Modified' section of any
    identified files from scan_dir_and_files()."""
    dtime = datetime.utcfromtimestamp(ftime)
    return dtime.strftime("%d %b %Y")


def extract_modified_win_files(fpath):
    tree = pathlib.Path(fpath)
    if platform.system() != "Windows":

        return 'Platform Not Yet Supported'

    try:
        print("Windows System Identified, Searching for files...\n")
        print("*" * 100)
        time.sleep(3)
        # tree = pathlib.Path(fpath)

        for entry in tree.iterdir():
            if entry.suffix in windows_extensions:
                file_date = entry.stat()
                dir_and_file_info = f"{entry.name}\t  Last Modified: {check_file_time(file_date.st_ctime)}"
                # print(f'{entry.name}\t last modified: {check_file_time(file_date.st_mtime)}')
                print(dir_and_file_info)

    except FileNotFoundError as err:
        logging.error(f"{err.filename} could not be found")


        
extract_modified_win_files("Provide a Windows Path")
