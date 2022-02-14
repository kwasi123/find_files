#!/usr/bin/python3
import os
import sys
import re
import subprocess

file_extension = sys.argv[1]
path_to_files = sys.argv[2]

def find_files(file_extension, path_to_files):
	'''
	This function searches for files from a provided path.
	This function takes in two arguments. 
	1. A file extension
	2. The full path to search for files.
	'''
	PATH = []
	DIRS = []
	FILES = []
	found_files = []

	# Check if the path exists and the path is also a directory.
	if os.path.exists(path_to_files) and os.path.isdir(path_to_files):
		for path, dirnames, files in os.walk(path_to_files): # Loop through the path to find all files.
			FILES.append(files)

		for files_ in FILES:
			if len(files_) > 0:
				for files in files_:
					if files.endswith(file_extension):
						found_files.append(files)

		if sys.platform == 'linux':
			with open('file_path.txt', mode='w') as f:
				for file in found_files:
					file_path = subprocess.run(['find', path_to_files, '-name', file], capture_output=True)
					# print(file_path.stdout)
					f.write(file_path.stdout.decode())
					# print(file)
		elif sys.platform == 'win32':
			with open('file_path.txt', mode='w') as f:
				for file in found_files:
					file_path = subprocess.run(['dir', path_to_files, '/s'], shell=True, capture_output=True)
					print(file_path.stdout)


def main():
	global file_extension
	global path_to_files
	find_files(file_extension, path_to_files)


if __name__ == '__main__':
    main()
