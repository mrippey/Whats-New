__author__ = "Michael Rippey @nahamike01"
__date__ = "2020/05/11"
"""
Author: Michael Rippey (c) 2020

Copyright 2020 Michael Rippey

See LICENSE.md for details
"""
#!/usr/bin/python
from datetime import datetime 
from pathlib import Path
import time 
import argparse 
import sys 
import os 



# List of file extensions to look for 
suspect_extension = {'.bat', '.dll', '.cmd', '.bin', '.cpl', '.exe', '.ps1', '.inf1', '.sct', '.vbs', '.vb', '.hta', '.msi', '.htm', '.wll', '.txt','.dotm', '.htm', '.log'}

def check_file_time(ftime):
    """This function adds a date and time to the 'Last Modified' section of any 
    identified files from scan_dir_and_files()."""

    dtime = datetime.utcfromtimestamp(ftime)
    format_date = dtime.strftime('%d %b %Y')
    yield format_date



def scan_dir_and_files(fpath):
    """
    This function utilizes the pathlib module to search through the directory provided as an argument, and extracts any files with the above extension to be 
    printed to a file.

    The check_file_time function is called to append the Windows time of the files that were returned from the search. 

    The created file contains the following naming: 'dir_lookup_todaysdate.txt' 
    """
    tree = Path(fpath)
    print('Scanning...')
    print("*" * 50)
    time.sleep(3)
    for entry in tree.iterdir():        
        if entry.suffix in suspect_extension:
            file_date = entry.stat()
            dir_and_file_info = f'{entry.name}\t Last Modified: {check_file_time(file_date.st_mtime)}'
            #print(f'{entry.name}\t last modified: {check_file_time(file_date.st_mtime)}')
            print(dir_and_file_info)

            with open("C:\\users\\target1\\desktop\\dir_lookup_"+str(datetime.now().strftime("%Y%m%d"))+".txt", 'a') as f:
                f.write(dir_and_file_info+"\n")
        
    print('*' * 50)
    print('Scan Completed')



def main():
    print("""

----------------------------------------------------------------                                                                                                                                                                              
Author: Michael R.   
What's New, A Directory and File Discovery Tool
----------------------------------------------------------------
Purpose: Discover newly added files by time & date based on a set of extension types for the directory of your choosing with '--dir'.
         Get a list of file extensions searched with the '--list' option.
         A file with the date you ran the tool will be created and saved to the current directory, or whatever directory you specify.

Examples:
python block_or_not.py --dir C:\\Users\\Guest\\AppData\\Local\\Temp\\
python block_or_not.py --list
    
    """)


    parser = argparse.ArgumentParser(description="Directory and File Discovery Tool")
    parser.add_argument('--dir', "--d", type=scan_dir_and_files, help='list the directory to scan')
    parser.add_argument('--list', "--l",  action='store_true', help='list extensions being searched')

    args = parser.parse_args()
    #print(args.dir)
    if args.dir:
        return scan_dir_and_files(args.dir)
    if args.list:
        print(suspect_extension)
    else:
        pass
    
        
    
if __name__ == '__main__':
    main()

