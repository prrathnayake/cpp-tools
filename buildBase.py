import os
import sys
import re
import subprocess

if len(sys.argv) < 2 :
    raise Exception("python3 " + sys.argv[0] + " path to ccp-base")
 
rootdir = sys.argv[1]

for file in os.listdir(rootdir):
    dirs = os.path.join(rootdir, file)
    if os.path.isdir(dirs):
        if ("app" in dirs):
            process = subprocess.Popen("conan create " + dirs + "/src", stdout=subprocess.PIPE, shell=True)
            print(process)
            process.wait()