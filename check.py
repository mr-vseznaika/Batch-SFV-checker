#! /usr/bin/env python
import os, fnmatch, string
import subprocess
import shutil

ROOT = "./download"
AIM = "./checked"
PATTERN = "*.sfv"

filepaths = []
for dirpath, dirnames, filenames in os.walk (ROOT):
    filepaths.extend (
        os.path.join (dirpath, f) for f in fnmatch.filter (filenames, PATTERN)
    )

for x in filepaths:
    process = subprocess.Popen(['cksfv','-g',x], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    output = process.communicate()
    retcode = process.poll()

# search for OK
    retcoded = list(output)
    if 0 == retcode:
        print "hooray: " + x
        dir_from = os.path.dirname(x)
        dir_to = dir_from.replace(ROOT,AIM)
        shutil.move(dir_from,dir_to)
        print dir_to
        
# than move OK folders

