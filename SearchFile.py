import os
import re

#Search all files that match the string(regular expession) in dir, and then return a list contents all absolute path.
def SearchFile(Path, File):
    allFile=os.listdir(Path)
    temp_list = []
    for eachFile in allFile:
        if os.path.isdir(Path+os.sep+eachFile):
            temp_list.extend(SearchFile(Path+os.sep+eachFile, File))
        elif re.findall(File,eachFile) != []:
            objectFile = re.findall(File,eachFile)
            temp_list.append(Path + os.sep + objectFile[0])
    return temp_list
#usage:******************************* 
#Path = '/home/fanzhibo/MPI_CODE'
#File = re.compile(r'.*\.c')
#res = SearchFile(Path, File)
#print(res)
#***************************************
