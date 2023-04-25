import os; import shutil; import psutil
from datetime import datetime
import sys;from pydub import AudioSegment
import chardet; import codecs; import re

Pathlist = ['D:/Proccess/TempArea2/elements/',
'D:/Proccess/TempArea2/'] 
for index, PATH in enumerate(Pathlist):print('%s. %s' % (index, PATH))
Pchoice= int(input())
Workdir = Pathlist[Pchoice]
Fchoice = input('Format: (Default aac): -')
if Fchoice == '':
    SpecifyFormat = '.aac'
else:
    SpecifyFormat = '.'+Fchoice


os.chdir(Workdir)
def Get_Files(FORMAT, counter = 0, COLLECT_FILES = []):
    for abpath, dirs, filename in os.walk(os.getcwd()):pass; COLLECT_FILES.extend(filename); Delindex = []
    for index in range(len(COLLECT_FILES)):
        if not(FORMAT in COLLECT_FILES[index]):Delindex.append(index)
    for cycle in range(len(Delindex)):
        COLLECT_FILES.pop(Delindex[cycle] - counter)
        counter += 1
    # print(COLLECT_FILES)
    return COLLECT_FILES

def Format_Elements(FILES, FILE_STR = []):
    for element in FILES:
        FILE_STR.append('file \''+element+'\'')
    return FILE_STR
    
def Create_CONCAT_FILE(Filelist):
    with open('concat.txt', 'wt',encoding='utf-8') as File:
        for element in range(len(Filelist)):
            if element != len(Filelist) - 1:
                File.write(str(Filelist[element])+'\n')
            else:
                File.write(str(Filelist[element]))

if __name__ == '__main__':
    Filelist = Get_Files(SpecifyFormat)
    Filelist = Format_Elements(Filelist)
    Create_CONCAT_FILE(Filelist=Filelist)
    for index, element in enumerate(Filelist):
        print('%s. %s' % (index + 1, element))