import SearchFile
import os
import re

#Looking in list to gather data
Path = '/home/fanzhibo/jxpamg_first'
File = re.compile(r'.*\.result')
List = SearchFile.SearchFile(Path,File)
DataBase = open('DataBase.yaml','w')
count = len(List)
s = 'Count: %d\n' %count
DataBase.write(s)
DataBase.write('ResultData: \n')
for file_item in List:
    DataBase.write('    -\n')
    fp = open(file_item,'r')
    data = fp.read()
    #problem
    DataBase.write('     Problem: ')
    DataBase.write('SM\n')
    #processor
    DataBase.write('     Processor: ')
    DataBase.write('N1P2T2\n')
    #parameter
    DataBase.write('     Parameter: ')
    DataBase.write('r1c0i1s22\n')
    #submit time
    DataBase.write('     Submit time: ')
    DataBase.write('202022030303\n')
    #Setup
    DataBase.write('     SetupTime: ')
    need = re.findall(r'Setup.*=.*[(][0-9.]*,.[0-9.]*,.([0-9.]*)[)]',data)
    DataBase.write(need[0]+'\n')
    #Solver
    DataBase.write('     SolveTime: ')
    need = re.findall(r'Solve.*=.*[(][0-9.]*,.[0-9.]*,.([0-9.]*)[)]',data)
    DataBase.write(need[0]+'\n')
    #Total time
    DataBase.write('     TotalSolveTime: ')
    need = re.findall(r'Time.*=.*[(][0-9.]*,.[0-9.]*,.([0-9.]*)[)]',data)
    DataBase.write(need[0]+'\n')
    #Iters
    DataBase.write('     Iters: ')
    ite = re.compile(r'^\s*(\d+)\s+',re.M)
    need = re.findall(ite,data)
    DataBase.write(need[-1]+'\n')
    #end
    fp.close()
