import os; import shutil; import psutil
import re; from time import *
from datetime import *

dirs = []
RootDirectory = 'D:\\Entertament\\Blive\\'; os.chdir(RootDirectory); print('Work Path:',RootDirectory)

"""
Useful Path:

'D:\\Proccess\\TempArea\\'
'D:\\Proccess\\TempArea1\\'
'D:\\Proccess\\TempArea2\\'
'D:\\Proccess\\TempArea3\\'
'D:\\Entertament\\Blive\\'
"""

for abpath, directories, filename in os.walk(RootDirectory):pass; dirs.extend(directories)
for index, dirname in enumerate(dirs):
    print(str(index)+'. '+dirname, end='\n')
print('\n'); LogicalSelection = input('1.Clear all Directory Files.\n2.Choose a single directory to clear.\n3.Pass\n -')
if LogicalSelection == '1':
    for dirReader in dirs:
        try:
            shutil.rmtree(dirReader)
            os.mkdir(dirReader)
        except:
            pass
        finally:
            print('%s\'s files cleared.' % (dirReader))
elif LogicalSelection == '2':
    IndexSelection = int(input('Enter the index: -'))
    try:
        shutil.rmtree(dirs[IndexSelection])
        os.mkdir(dirs[IndexSelection])
    except:
        pass
    finally:
        print('%s\'s files cleared.' % (dirs[IndexSelection]))
elif LogicalSelection == '3':
    print('\n\n');print('Passed'.center(100,'*'))
    pass
else:
    print('Invalid Request.')