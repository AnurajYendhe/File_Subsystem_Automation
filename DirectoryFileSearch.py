# Description :- File Automation Display  all files with specific extension in the directory

######################################################################
# importing requried package 
######################################################################
import os
import time
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
    flag = False
    flag = os.path.isabs(DirName)
    return flag

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
    flag = os.path.exists(DirName)
    return flag

######################################################################
# Function name :- DirectoryTrevel
# Description :- Trevel input directory
# Input :- Path of directory,Extension
# Output :- Print all files with input extension
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def DirectoryTrevel(DirName,extension):
    print("We are going to scan directory : ",DirName)

    flag = CheckAbs(DirName)
    if(flag == False):
        DirName = AbsolutePath(DirName)

    exist = CheckDir(DirName)
    if(exist == True):
        for folderName, subfolderName, filesName in os.walk(DirName):
            print("Current folder name is : ",folderName)
            for file in filesName:
                filepath = os.path.join(folderName,file)
                if(filepath.endswith(extension)):
                    print(filepath)
    else:
        print("Error : Invalid path")

######################################################################
# Function name :- main
# Description :- Main function from where execution starts
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def main():
    print("------Automation using Python-----")
    print("Automation script Name is : ",argv[0]) # Display name of script

    if(len(argv) == 2): # validation of arguments 
        if((argv[1] == "-H") or (argv[1] == "-h")): # flag for display help
            print("Help : This automation script is use to display all files with specific extension in the directory")
            exit()

        elif((argv[1] == "-U") or (argv[1] == "-u")): # flag for display usage
            print('Usage : Name_of_script.py "Path_of_directory" "File_Extension"')
            print('Example : DirectoryFileSearch.py "Demo" ".py"')
            exit()

        else:
            print("Error : Invalid Arguments")
            exit()

    elif(len(argv) == 3):
        try:
            startTime = time.time()
            DirectoryTrevel(argv[1],argv[2])
            endTime = time.time()
            executionTime = endTime - startTime

            print("The script took time to execute as : ",executionTime)

        except ValueError:
            print("Invalid input type")

        except Exception as Err:
            print("Invalid input",Err)

    else:
        print("Error : Invalid Numbers of Arguments.")
        exit()

######################################################################
# Application stater
######################################################################
if __name__ == "__main__":
    main()