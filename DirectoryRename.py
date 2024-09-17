#  Description :- File Automation rename all files with first extension to the second extension in the directory

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
    flag = os.path.exists(DirName)
    return flag

######################################################################
# Function name :- ChangeExtension
# Description :- change the extension of file
# Input :- absolut path of file
# Output :- Rename file with frist extension to the second extension
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def ChangeExtension(filename,new_extesion = argv[3]):
    if '.' in filename:
        name,old_extension = filename.rsplit('.',1)
        new_filename = name + new_extesion
    else:
        new_filename = filename + new_extesion
    return new_filename   

######################################################################
# Function name :- DirectoryTrevel
# Description :- Trevel input directory
# Input :- Path of directory,Extension
# Output :- Rename all files with frist extension to the second extension
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def DirectoryTrevel(DirName,extension1,extension2):
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
                if(filepath.endswith(extension1)): # filter files with first extension
                    new_name = ChangeExtension(filepath,extension2) 
                    os.rename(filepath,new_name) # rename files with second extension

        print("successfully change the files extension")             
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

    if(len(argv) == 2):  # validation of arguments 
        if((argv[1] == "-H") or (argv[1] == "-h")): # flag for display help
            print("Help : This automation script is use to rename of file with first extension to the second extension")
            exit()

        elif((argv[1] == "-U") or (argv[1] == "-u")): # flag for display usage
            print('Usage : DirectoryRename.py "Path_of_directory" "first_Extension" "Second_Extension"')
            print('Example : DirectoryRename.py "Demo" ".py" ".txt"')
            exit()

        else:
            print("Error : Invalid Arguments")
            exit()

    elif(len(argv) == 4):
        try:
            startTime = time.time()
            DirectoryTrevel(argv[1],argv[2],argv[3])
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