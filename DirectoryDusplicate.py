# Description :- File Automation write the name of duplicate files into log file

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
# Function name :- checkDups
# Description :- check files is duplicate or not 
# Input :- dict which is created by FindDups Function
# Output :- return absolute path of file if it's duplicate
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def checkDups(values):
    if(len(values) > 1):
        return values

######################################################################
# Function name :- printResult
# Description :- write the name of duplicates files in the directory
# Input :- dict which is created by FindDups Function
# Output :- generate log file which contain name of duplicate files
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def printResult(dups):
    results = list(filter(checkDups,dups.values()))

    if(len(results) > 0):
        print("Duplicate files found")
        print("Following are duplicate files.")
        seperator = "*" * 80
        fobj = open("Demo.txt",'w')
        fobj.write(seperator + "\n")
        fobj.write("Current date and time is : "+time.ctime()+"\n")
        fobj.write(seperator + "\n")
        counter = 0
        for result in results:
            fobj.write(seperator + "\n")
            for subresult in result:
                fobj.write("%s\n"% subresult) 
                counter = counter + 1         
        fobj.close()
        print("total numbers of duplicate files is : ",counter)

    else:
        print("No duplicates files found.")
######################################################################
# Function name :- FindDups
# Description :- find the duplicates files in the directory
# Input :- Path of directory
# Output :- duplicates files in the directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def FindDups(DirName):
    print("We are going to scan directory : ",DirName)

    flag = CheckAbs(DirName)
    if(flag == False):
        DirName = AbsolutePath(DirName)

    exist = CheckDir(DirName)

    if(exist == True):
        dups = dict()
        for dirName, subdirs, fileList in os.walk(DirName):
            print("Current folder is : ",dirName)
            print("  ")
            for file in fileList:
                filepath = os.path.join(dirName,file)
                checksum = calculateChecksum(filepath)
                
                if checksum in dups:
                    dups[checksum].append(filepath)
                else:
                    dups[checksum] = [filepath]

        printResult(dups)
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
            print("This Script is used to write the name of duplicate files into log file persent in the directory")
            exit()

        elif(argv[1] == "-u") or (argv[1] == "-U"):
            print('usage : Name_of_script.py "Path_of_directory"')
            print('Example: DirectoryDusplicate.py "Anuraj"')
            exit()

        else:
            try:
                startTime = time.time()
                arr = FindDups(argv[1])
                endTime = time.time()
                executionTime = endTime - startTime

                print("the script took time to execute is : ",executionTime)

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