__author__ = "Michael Rippey"
__date__ = "2021/05/23"
"""
Author: Michael Rippey (c) 2021

Copyright 2021 Michael Rippey
"""
#!/usr/bin/python
from datetime import datetime 
from pathlib import Path
import time 
import logging
import platform


# List of file extensions to look for 
nix_mac_extensions = {
    ".app",
    ".sh",
    ".tgz",
    ".plist",
    ".nib",
    ".pkg",
    ".bin",
    ".elf",
    ".dylib",
    ".c",
    ".desktop",
    ".ko",
    ".txt",
}


def check_file_time(file_mod_time):
    """This function adds a date and time to the 'Last Modified' section of any
    identified files from scan_dir_and_files()."""
    mod_time = datetime.utcfromtimestamp(file_mod_time)
    return mod_time.strftime("%d %b %Y")


def extract_new_nix_files(fpath):
    tree = pathlib.PosixPath(fpath)
    if platform.system() != "Darwin":
        return

    try:
        print("\n*Nix System Identified, Searching for files...\n")
        print("*" * 100)
        time.sleep(3)
        # tree = pathlib.Path(fpath)

        for entry in tree.iterdir():
            if entry.suffix in nix_mac_extensions:
                file_date = entry.stat()
                dir_and_file_info = f"{entry.name:<25s} Last Modified: {check_file_time(file_date.st_ctime):<12s}"
                # print(f'{entry.name}\t last modified: {check_file_time(file_date.st_mtime)}')
                print(str(dir_and_file_info))

        print("*" * 100)
        print("\nScan Complete")

    except FileNotFoundError as err:
        logging.error(f"{err.filename} could not be found")


extract_new_nix_files("Provide a *nix like path")
