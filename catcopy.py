#!/usr/bin/python3

"""
`cat` but copy the content into clipboard.
you need xclip command to run this script.
for now its only support one file.

sudo mv catcopy.py /usr/bin/catcopy
sudo chmod +x /usrbin/catcopy
"""

import sys
import os 
import subprocess


def copy_file_content(filename: str):
    try:
        filename = os.path.abspath(filename)
        with open(filename, 'r') as file:
            content = file.read()

        p1 = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        p1.communicate(input=content.encode())
        print('Copied!')

    except Exception as e:
        print(f"Something error: {e}")


def usage():
    print("copycat filename.txt ")
    print("Example: ./catcopy.py /etc/passwd")


if __name__ == "__main__":
    if len(sys.argv) !=2:
        usage()
        sys.exit(1)
    else:
        copy_file_content(sys.argv[1])
