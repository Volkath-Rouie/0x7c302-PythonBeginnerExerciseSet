#ffmpeg concat file generation and merging
#lang='zh_CN.utf-8'

#Requires a ffmpeg command line environment on the system.

import os; import shutil; import psutil
from datetime import datetime
import sys;from pydub import AudioSegment
import chardet; import codecs; import re

def retrieval(path, video_format, file=[],delindex=[], counter=0):
    for abpath, dirs, filename in os.walk(path):
        pass
    for loop0 in range(len(filename)):
        if (video_format in filename[loop0]) and not('merge' in filename[loop0] or 'concat' in filename[loop0]):
            print(filename[loop0],end='\n')
        else:
            delindex.append(loop0)
    print('\n\n')
    for loop1 in delindex:
        print('\'%s\'  elements removed.' % (filename[loop1 - counter]))
        filename.pop(loop1 - counter)
        counter += 1
    print('\n\n')
    Guidice = input('\nAre you sure it\'s properly show? -')
    if Guidice == 'y':
        for loop2 in filename:
            if '\'' in loop2:
                modify_filename = re.sub('\'','',loop2)
                os.rename(loop2,modify_filename)
                file.append(modify_filename)
            else:
                file.append(loop2)
    else:
        for loop3 in reversed(filename):
            if '\'' in loop3:
                rev_modified_filename = re.sub('\'','',loop3)
                os.rename(loop3,rev_modified_filename)
                file.append(rev_modified_filename)
            else:
                file.append(loop3)   
    return file


def ConcatInfoFile(concat_file, concat_object, Reader = ''):
    with open('concat.txt','wt',encoding='utf-8') as File:
        for loop0 in concat_object:
            File.writelines('file \''+loop0+'\'\n')
        print('%s%s write completed.'%(Workdir, concat_file))
    with open('concat.txt','rt',encoding='utf-8') as File:
        Reader = File.read()
    print('Content:\n\n'+Reader+'\n\n')


if __name__ == '__main__':
    print('Starting...\n')
    # Workdir = 'D:/Entertament/Hoyoverse/GMV/List/60'
    Workdir = 'D:\\Proccess\\TempArea1\\'   #Operation Path
    # Workdir = 'D:/Entertament/Hoyoverse/GMV/'   #Hoyoverse
    os.chdir(Workdir)
    Object_format = '.mp4'
    Object = retrieval(Workdir, Object_format)     #Serialized containers
    Output_Filename = '"'+Object[0][0:-17]+'.mp4"'
    # Output_Filename = '"'+'merge.mp4"'
    Output_Sure = input('Are sure Output_Filename:%s it\'s right? -'%(Output_Filename))
    if Output_Sure != 'y':
        # Output_Filename = input('New output filename:  - ')
        Output_Filename = 'merge.mp4'
        # Output_Filename = 'GenshinImpactDemo1.mp4'
    print('Output Name:',Output_Filename)
    ConcatInfoFile(Output_Filename, Object)
    G1 = input('You wether to merge video files? -')
    if G1 == 'y':
        os.system('ffmpeg -i %s -hide_banner' % ('"'+Object[0][0:-17]+'"'))
        # VideoBitrate = input('Video Bitrate (Measurement:kilo bit)?  -') -- error
        VideoBitrate = 25000
        # FrameRate = input('Video Frame Rate: (Measurement: fps? -') -- error        
        os.system('ffmpeg -hwaccel vulkan -f concat -safe 0 -i concat.txt -c:v copy -rf64 auto -strict -2 -c:a copy -ac 8 -b:v %sk -b:a 800k  %s -y'
        % (VideoBitrate, Output_Filename))

        # os.system('ffmpeg -hwaccel vulkan -f concat -safe 0 -i concat.txt -strict -2 -c:v copy -c:a copy -b:v 10000k -b:a 320k %s -y'
        # % (Output_Filename)) -- example
    else:
        pass

print('\n\n');os.system("dir | findstr -i '.flv'")      #Test whether the operating directory generates the corresponding files