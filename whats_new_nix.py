__author__ = "Michael Rippey"
__date__ = "2021/05/23"

"""
Author: Michael Rippey (c) 2021
Copyright 2021 Michael Rippey

"""

from datetime import datetime
import pathlib
import time
import platform
import sys

# List of file extensions to look for 
common_nix_extensions = {
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
	".so",
}


def check_file_time(file_mod_time):
	"""This function adds a date and time to the 'Last Modified' section of any
	identified files from scan_dir_and_files()."""
	mod_time = datetime.utcfromtimestamp(file_mod_time)
	return mod_time.strftime("%d %b %Y")


def extract_files_check(fpath):
	tree = pathlib.PosixPath(fpath)

	if platform.system() != "Darwin":
		print('Platform Not Yet Supported')
		sys.exit()

	try:
		from_new_nix_files(tree)
	except FileNotFoundError as err:
		print()
		print(f' ERROR: Path > {err.filename} may not exist, try again...')

def from_new_nix_files(tree):
	print("\n[+] *nix OS, checking path and files...\n")
	print("*" * 100)
	time.sleep(2)

	for entry in tree.iterdir():
		if entry.suffix in common_nix_extensions:
			file_date = entry.stat()
			dir_and_file_info = f"{entry.name:<25s}\
				 Last Modified: {check_file_time(file_date.st_birthtime):<12s}"
			print(str(dir_and_file_info))
			
		   
	print("*" * 100)
	print("\n[+] Scan complete")


extract_files_check("*nix like path")
