import os
import sys
import re
import subprocess
 
rootdir = sys.argv[1]

for file in os.listdir(rootdir):
    dirs = os.path.join(rootdir, file)
    if os.path.isdir(dirs):
        if (len(sys.argv) > 2) :
            if(sys.argv[2] in dirs):
                process = subprocess.Popen("conan create " + dirs + "/src", stdout=subprocess.PIPE, shell=True)
                print(process)
                process.wait()
            
        elif(len(sys.argv) == 2 and "app" in dirs):
            process = subprocess.Popen("conan create " + dirs + "/src", stdout=subprocess.PIPE, shell=True)
            print(process)
            process.wait()
            
        else:
            print(("python3 " + sys.argv[0] + " path to ccp-base"))