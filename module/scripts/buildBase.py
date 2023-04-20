import os
import sys
import re
import subprocess
import argparse

def createConanPackage(dirs):
    process = subprocess.Popen("conan create " + dirs + "/src", stdout=subprocess.PIPE, shell=True)
    print(process)
    process.wait()
    
def main(args):
    for file in os.listdir(args.path):
        dirs = os.path.join(args.path, file)
        if("app" in dirs):
            if os.path.isdir(dirs):
                if (args.package == None):
                    createConanPackage(dirs)             
                else:
                    if(args.package == file):
                        createConanPackage(dirs)
         
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create Conan Packages.')
    parser.add_argument("path")
    parser.add_argument("-p", "--package", help="package name")
    args = parser.parse_args()
    
    main(args)