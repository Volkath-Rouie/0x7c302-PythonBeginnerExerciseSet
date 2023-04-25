from pydub import AudioSegment
import os; import shutil
import traceback; import sys
import psutil; from time import sleep

wave_Merge_path = 'D:\\Proccess\\TempArea\\'       #音频文件所在目录
print('\nPath Existention:',os.path.exists(wave_Merge_path))
if not (os.path.exists(wave_Merge_path)):
    os.mkdir(wave_Merge_path)
os.chdir(wave_Merge_path)

counter = []
for abpath, dirs, filenames  in os.walk(wave_Merge_path):
    pass

files_num = len(filenames)
print('Find %s mounts of files'%(files_num))

#按时间顺序，
wave_Sequence_filelist = []
for Loop3 in range(files_num):
    wave_Sequence_filelist.append('%s.flac'%(Loop3))    

print('filenamelist:', wave_Sequence_filelist)

MergeAudioSegment = AudioSegment.from_file("烛灵儿Hikari 2023-01.flac_O.flac")

try:
    wave_Sequence_filelist[1]
    try:
        for Temp_Audio_Segment in range(1, files_num):
            MergeAudioSegment += AudioSegment.from_file(str(Temp_Audio_Segment)+'.flac')
    except Exception as Temp:
        Temp.with_traceback()
except:
    pass
finally:
    MergeAudioSegment.export('Merged.flac',format='flac')