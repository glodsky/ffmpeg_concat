# -*- coding: utf-8 -*-
 
import argparse
import os
import subprocess
import os.path
 

def process_arguments():
    """Processes CLI arguments

    This function parses all arguments
    This allows users to customize options
    for the output video.
    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # video options
    file_options = parser.add_argument_group('File Options')
    file_options.add_argument('-i', '--input', help='Source video directory \n You can input empty or Set target directory', action='store', required=False)
    file_options.add_argument('-o', '--output', help='Output video directory\n You can input empty ,and Default Output DIR is you input directory', action='store', required=False)
    file_options.add_argument('-n', '--newfile', help='Output video file name\n You can input empty,and Default OutputName is output', action='store', required=False)
    # parse arguments
    return parser.parse_args()

# process arguments
args = process_arguments()
if args.input == None :
    args.input = os.curdir 
sample_f_ext = '' # vidoe file extension 
parts = 'concat:'
for p in os.listdir(args.input):
    if os.path.splitext(p)[1] != '.py':
        parts = parts + os.path.join(args.input,p) + '|'
        sample_f_ext = os.path.splitext(p)[1]        
input_files = parts[:-1]
if args.output == None :
    args.output = args.input
if args.newfile == None :
    args.newfile = 'output%s' % sample_f_ext
output_file = os.path.join(args.output,args.newfile)
execute = [
    'ffmpeg',
    '-i',
    input_files,
    '-c',
    'copy',
     output_file
] 
 
subprocess.run(execute, check=True)



