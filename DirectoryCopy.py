# Description :- File Automation Copy all files from first directory into the second directory

######################################################################
# importing requried package 
######################################################################
import os
import time
import shutil
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
# Function name :- CreateDir
# Description :- To create directory
# Input :- Name of directory
# Output :- Create input directory into current directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def CreateDir(DirName):
    try:
        os.mkdir(DirName)
    except:
        pass 

######################################################################
# Function name :- DirectoryTrevel
# Description :- To trevel input directory
# Input :- Name of directory
# Output :- copy all files input directory into output directory
# Author :- Yendhe Anuraj Balasaheb
# Date :- 07/09/2024
######################################################################
def DirectoryTrevel(DirName1,DirName2):
    print("We are going to scan directory : ",DirName1)

    flag = CheckAbs(DirName1)
    if(flag == False):
        DirName1 = AbsolutePath(DirName1)

    exist = CheckDir(DirName1)

    if(exist == True):
        flag = CheckDir(DirName2)
        if(flag == False):
            CreateDir(DirName2)

        for folderName, subfolderName, filesName in os.walk(DirName1):
            print("Current folder name is : ",folderName)
            for file in filesName:
                filepath = os.path.join(folderName,file)
                shutil.copy(filepath,DirName2) # copy all files from first directory into second directory
                
        print("Files are successfully copy from",DirName1,"into",os.path.abspath(DirName2))           
    else:
        print("Error : Invalid path")

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

    if(len(argv) == 2): # validation of arguments 
        if((argv[1] == "-H") or (argv[1] == "-h")): # flag for display help
            print("Help : This automation script is use to copy all files from first directory into second directory")
            exit()

        elif((argv[1] == "-U") or (argv[1] == "-u")): # flag for display usage
            print('Usage : Name_of_script.py "Path_of_First_directory" "Path_of_second_dirctory"')
            print('Example : DirectoryCopy.py "Demo" "Anuraj"')
            exit()

        else:
            print("Error : Invalid Arguments")
            exit()

    elif(len(argv) == 3):
        try:
            startTime = time.time()
            DirectoryTrevel(argv[1],argv[2])
            endTime = time.time()
            print("The script took time for execute as : ",endTime - startTime)

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