import re; import shutil
import os; import psutil
import traceback
from time import sleep

sleep(0)
WorkDirecotory = ("D:\\Proccess\\TempArea1\\")
Delete_Object = "[\(\)（）]"

class Filename_Formatter():
    def __init__(self):
        self.Origin_DB = []
        self.Format_DB = []
        # self.Array_DB = []
        self.Workpath = ''
        self.Object = ''

    def Active_Manger(self, path, object):
        os.chdir(path); print('Workpath change to "%s"' % (path))
        self.Workpath=(path); self.Object = object
        self.Get_OriginalFilename()
        self.Format_Pathfilesname()

    def Get_OriginalFilename(self):
        for abpath,dirs,filename in os.walk(self.Workpath):pass
        self.Origin_DB.extend(filename)
        # print(self.Origin_DB+'\n\n')

    def Format_Pathfilesname(self):
        for Reader in range(len(self.Origin_DB)):
            tmp_Reader = re.sub(self.Object, '', self.Origin_DB[Reader])
            self.Format_DB.append(tmp_Reader)
        print('Orirgin'+str(self.Origin_DB)+'\n\n'+'Format:'+str(self.Format_DB))
        for Indicator in range(Reader + 1):
            os.rename(self.Origin_DB[Indicator], self.Format_DB[Indicator])

if __name__ == '__main__':
    Excutor = Filename_Formatter()
    Excutor.Active_Manger(WorkDirecotory, Delete_Object)