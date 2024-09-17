# Description :- File Automation display checksum of files in the directory

######################################################################
# importing requried package 
######################################################################
import os
import time
import hashlib
from sys import *

######################################################################
# Function name :- CheckAbs
# Description :- check file path is related or absolute
# Input :- Path of directory
# Output :- True(file path is absolute) / False(file path is not absolute)
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def CheckAbs(DirName):
    result = os.path.isabs(DirName)
    return result

######################################################################
# Function name :- AbsolutePath
# Description :- create absolute path of directory
# Input :- Path of directory
# Output :- Absolute Path of directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def AbsolutePath(DirName):
    path = os.path.abspath(DirName)
    return path 

######################################################################
# Function name :- CheckDir
# Description :- check directory exists or not
# Input :- Absolute path of directory
# Output :- True(file path is exists) / False(file path is not exists)
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def CheckDir(DirName):
    result = os.path.exists(DirName)
    return result
    
######################################################################
# Function name :- calculateChecksum
# Description :- calculate checksum of file
# Input :- Path of file,blocksize(optional)
# Output :- checksum of file
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def calculateChecksum(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

######################################################################
# Function name :- DisplayChecksum
# Description :- print checksum of file
# Input :- Path of directory
# Output :- checksum of file
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def DisplayChecksum(DirName):
    print("We are going to scan directory : ",DirName)
    flag = CheckAbs(DirName)
    if(flag == False):
        DirName1 = AbsolutePath(DirName)

    exist = CheckDir(DirName)

    if(exist == True):
        for dirName, subdirs, fileList in os.walk(DirName):
            print("Current folder is : ",dirName)
            print("  ")
            for file in fileList:
                filepath = os.path.join(dirName,file)
                checksum = calculateChecksum(filepath)
                print("Absolute path of file is : ",filepath)
                print("Checksum of file is : ",checksum)
                print('   ')

    else:
        print("Invalid Path")

######################################################################
# Function name :- main
# Description :- Main function from where execution starts
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def main():
    print("------Automation using Python------")
    print("-----File Subsystems Automation-----")
    print("Automation script Name is : ",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to display checksum of files persent in the directory")
            exit()

        elif(argv[1] == "-u") or (argv[1] == "-U"):
            print('usage : Name_of_script.py "Path_of_directory"')
            print('Example: DirectoryChecksum.py "Anuraj"')
            exit()
        else:
            try:
                arr = DisplayChecksum(argv[1])

            except ValueError as E:
                print("Error : Invalid input",E)

            except Exception as E:
                print("Error : Invalid input",E)
    else:
        print("Error : invalid numbers of arguments.")

######################################################################
# Application stater
######################################################################
if __name__ == "__main__":
    main()