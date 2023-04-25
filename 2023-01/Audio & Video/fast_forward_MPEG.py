import os; import shutil; import psutil
import re; from time import *; from time import sleep
from datetime import *; import traceback

#User Interface
WorkDirectory = 'D:\\Entertament\\Hoyoverse\\GMV\\List\\30'; os.chdir(WorkDirectory)
print('\n\n');print(WorkDirectory.center(100,':'));print('\n\n')
"""
Recent Path:

'D:\\Proccess\\TempArea\\'
'D:\\Proccess\\TempArea1\\'
'D:\\Proccess\\TempArea2\\'
'D:\\Proccess\\TempArea3\\'
'D:\\Entertament\\Blive\\'
'C:\\Users\\Sanctuary of Pilgrim\\Downloads\\Video\\'
'D:\\Entertament\\Hoyoverse\\GMV\\List\\30'
"""

class fast_forward():
    def __init__(self):
        self.files = []; self.object = ''
        self.file_video = ''; self.file_audio = ''
    
    def Refresh(self):
        for abpath, dirs, file in os.walk(os.getcwd()):pass; self.files = file
        print('\n\n');print('Path File List'.center(100,'*'))
        for index, names in enumerate(self.files):print('%s. %s'%(index, names),end='\n')
        print('Path File List'.center(100,'*'));print('\n')

    def Info(self):
        print('\n\n');os.system("ffprobe -hide_banner -i \"%s\"" % (self.object));print('\n\n')

    def Video_Encoding(self):
        Pre_Shell = ('ffmpeg -hide_banner -hwaccel vulkan -i \"%s\" -y -safe 0 -strict -2 -an -c:v h264_qsv -vf \"scale=7680:4320\" -r ' % (self.file_video))
        Full_Shell = Pre_Shell + input('Complete the commands: %s'%(Pre_Shell))
        print('Full command: %s' % (Full_Shell))
        print('Waiting for excuting......\n\n'); sleep(1)
        os.system(Full_Shell);print('\n\nComplete.')
    
    def HiRES(self):
        Pre_Shell = ('ffmpeg -hide_banner -hwaccel vulkan -i \"%s\" -vn -c:v flac -ar 192000 -ac 8 -ab 2400k ' % (self.file_audio))
        Full_Shell = Pre_Shell + input('Full command: %s'%(Pre_Shell))
        print('Full command: %s' % (Full_Shell))
        print('Waiting for excuting......\n\n'); sleep(1)
        os.system(Full_Shell);print('\n\nComplete.')
    
    def av_mux(self):
        Pre_Shell = ('ffmpeg -hide_banner -hwaccel vulkan -i \"%s\" -i \"%s\" -y -safe 0 -strict -2 -codec copy -shortest ' % (self.file_audio, self.file_video))
        Full_Shell = Pre_Shell + input('%s'%(Pre_Shell))
        print('Full command: %s' % (Full_Shell))
        print('Waiting for excuting......\n\n'); sleep(1)
        os.system(Full_Shell);print('\n\nComplete.')    

    def Video_General(self):
        Pre_Shell = ('ffmpeg -hide_banner -hwaccel vulkan -i \"%s\" -y -safe 0 -strict -2 -c:v h264_qsv -r ' % (self.object))  
        Full_Shell = Pre_Shell + input('%s'%(Pre_Shell))
        print('Full command: %s' % (Full_Shell))
        print('Waiting for excuting......\n\n'); sleep(1)
        os.system(Full_Shell);print('\n\nComplete.')
        
    def Active_Manager(self):
        while True:
            self.Refresh()
            Choice = input("""Choose a service:\n
            A. Check Container Info
            B. Video Encoding
            C. HiRES
            D. Exit
            F. Delete a file
            G. AV_Mux
            H. General Video Procces
            """)

            if Choice == 'a':
                while True:
                    self.Refresh(); input('')
                    Choose_Index = int(input('Select a file you need to check info. -'))
                    try:
                        self.object = self.files[Choose_Index]
                    except:
                        pass
                    self.Info()
                    if Choose_Index == 11:
                        break
            elif Choice == 'b':
                self.Refresh();
                Choose_Index = int(input('Select a Video_File you need to check info. -'))
                self.file_video = self.files[Choose_Index]
                self.Video_Encoding()
            elif Choice == 'c':
                self.Refresh();
                Choose_Index = int(input('Select a Audio_File you need to check info. -'))
                self.file_audio = self.files[Choose_Index]
                self.HiRES()
            elif Choice == 'exit':
                break
            elif Choice == 'f':
                self.Refresh();
                Choose_Index = int(input('Select a file you want to delete.'))
                try:
                    os.remove(self.files[Choose_Index])
                except:
                    pass
                finally:
                    print('\n%s%s has removed. \n'%(os.getcwd(), self.files[Choose_Index]))
            elif Choice == 'g':
                self.Refresh();
                self.file_audio = self.files[int(input('Select Audio File'))]; self.file_video = self.files[int(input('Selct Video File'))]
                self.av_mux()
            elif Choice == 'h':
                self.Refresh()
                self.object = self.files[int(input('Select a video you want to proccess'))]
                self.Video_General()
            else:
                print('Unkown Request 501'.center(100,':'));print('\n')
                



if __name__ == '__main__':
    Self = fast_forward()
    Self.Active_Manager()