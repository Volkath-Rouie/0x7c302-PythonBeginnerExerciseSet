from pydub import AudioSegment
import os; import shutil
import traceback; import sys
import psutil; from time import sleep
import time; from datetime import datetime
import threading

wave_Merge_path = 'E:\\Proccess\\Python\\wave_files\\'       #音频文件所在目录
print('\nPath Existention:',os.path.exists(wave_Merge_path))
if not (os.path.exists(wave_Merge_path)):
    os.mkdir(wave_Merge_path)
os.chdir(wave_Merge_path)

counter = []
for abpath, dirs, filenames  in os.walk(wave_Merge_path):
    if 'Merged' in filenames:
        os.remove(abpath)
        print('%s removed.' % (abpath))
    pass

files_num = len(filenames)
print('Find %s mounts of files'%(files_num))

#按时间顺序，
wave_Sequence_filelist = []
for Loop3 in range(files_num):
    wave_Sequence_filelist.append('%s.mp3'%(Loop3))    

print('filenamelist:', wave_Sequence_filelist)

MergeAudioSegment = AudioSegment.from_mp3('0.mp3')

try:
    wave_Sequence_filelist[1]
    try:
        for Temp_Audio_Segment in range(1, files_num):
            MergeAudioSegment += AudioSegment.from_mp3(str(Temp_Audio_Segment)+'.mp3')
            print('%s.mp3 add to merge list.' % (Temp_Audio_Segment))
    except Exception as Temp:
        Temp.with_traceback()
except:
    pass
finally:
    try:
        Time_info = time.localtime(int('{:.0f}'.format(time.time())))
        MergeAudioSegment.export('Merged %s.mp3' % (time.strftime('%Y-%m-%d %H-%M-%S',Time_info)),format='mp3',bitrate='640k')
    except:
        try:
            MergeAudioSegment.export('Merged.mp3',format='mp3',bitrate='640k')
        except:
            print('Merge failed.')
            pass