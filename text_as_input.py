# -*- coding: utf-8 -*-
"""Created on Thu Jun 22 08:24:30 2017
@author: marnold

Creates command line arguments, checks for output filename,
parses input text file to python dictionary and returns
python dictionary and output filename
"""
import argparse

def txt2dictionary ():
    # create parser and add arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help = "must input a .txt file.  see input.txt for example.  Further documentation is in README.md")
    parser.add_argument('-o', '--output',  help = "output file, if not entered will default to 'out' + eventid + '.xml'")
    args = parser.parse_args() # create arguments list
    
    # read in file to python dictionary
    lines = args.file.readlines()
    data = {}
    for line in lines:
        if line[0] == "#" or line[0] == "" or line[0] == "\n":
            pass
        else:
            temp = line.split(":::")
            tmp = temp[1]
            temp[1] = tmp[:-1]
            data[temp[0]] = temp[1]
        output_filename = ""

    # Check for output file argument.
    # If no output file argument, make an output filename.
    if args.output:
        output_filename = args.output
    else:           #
        print ("No output file argument. Default filename will be generated...")
        output_filename = "out_" + data['datasource'].lower() + data['eventid'] + '.xml' # set output filename
    return data , output_filename
