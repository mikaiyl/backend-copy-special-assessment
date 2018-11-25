#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
from zipfile import ZipFile
"""Copy Special exercise"""

# change this for a
SPECIAL_RE = re.compile(r'.+__\w+__.+')

def get_special( dirname ):
    #  returns a list of the absolute paths of the special files in the given directory
    global SPECIAL_RE
    sp_list = filter( lambda f: bool( SPECIAL_RE.match( f ) ), os.listdir( dirname ) )
    return map( lambda f: os.path.join( os.getcwd(), f ), sp_list )


def copy_to( files, dest ):
    # given a list of paths, copies those files into the given directory
    for file in files:
        shutil.copyfile( file, os.path.join( dest, file.split('/')[-1] ) )
    return


def zip( files, dest ):
    # given a list of paths, zip those files up into the given zipfile
    with ZipFile( dest, 'w' ) as archive:
        for file in files:
            archive.write( file )


def zip_to( files, dest ):
    """If the "--tozip zipfile" option is present at the start of the command
    line, run this command: "zip -j zipfile <list all the files>". This will
    create a zipfile containing the files. Just for fun/reassurance, also print
    the command line you are going to do first (as shown in lecture). (Windows
    note: windows does not come with a program to produce standard .zip
    archives by default, but you can get download the free and open zip
    program from [www.info-zip.org](http://www.info-zip.org/).)"""
    command = 'zip -j {zipfile} {filez}'.format( zipfile=dest, filez=' '.join( files ) )
    # this became a tuple IDK why?
    # print( 'Command I\'m going to try:' + '\n' + command )
    print 'Command I\'m going to try:' + '\n' + command
    commands.getoutput( command )
    return

# +++your code here+++
# Write functions and modify main() to call them

def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dirname', type=str, help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    #

    if args.todir:
        if not os.path.exists( args.todir ):
            os.mkdir( os.path.join( os.getcwd(), args.todir ) )
        else:
            pass
        copy_to( get_special( args.dirname ), args.todir )
    elif args.tozip:
        if os.path.exists( args.tozip ):
            print( 'Filename already exists' )
            return 1
        else:
            zip_to( get_special( args.dirname ), args.tozip )
    else:
        for file in get_special( args.dirname ):
            print( file )


if __name__ == "__main__":
    main()
