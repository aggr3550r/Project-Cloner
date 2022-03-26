import argparse
import os
import sys
import shutil

# Create the parser
my_parser = argparse.ArgumentParser(prog='duplicator',
usage='%(prog)s source destination', description='clone a code base from one directory into another')

# Add arguments and configure the parser to have a more user-friendly interface
my_parser.add_argument('v1',
metavar= 'source', help='the path of the source directory', action='store')
my_parser.add_argument('v2', metavar='destination', help='the path of the new destination directory',action='store', default='dst')


# Register the arguments passed via the CLI into the program itself
args = my_parser.parse_args()

input_path = args.v1

output_path = args.v2

# If the folder to be cloned is not within the current directory, exit the program
if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

# Else, perform the actual cloning and exit the program
shutil.copytree(input_path, output_path)
print('Done Cloning!!')
sys.exit(0)


