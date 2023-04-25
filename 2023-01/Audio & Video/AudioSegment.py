import threading; import time
from time import *
from datetime import *; import psutil
import datetime; import shutil
import re; import os; import sys
from pydub import audio_segment
import re; import random as rd
import wave; import contextlib as ct

def PathSelect():
    #PATH LIST
    Pathlist = ['D:/Proccess/TempArea2/elements/',
    'D:/Proccess/TempArea2/','D:/Proccess/TempArea1/','C:/Users/Sanctuary of Pilgrim/Downloads/Video',
    'C:/Users/Sanctuary of Pilgrim/Downloads/Video/elements',
    'D:/Proccess/TempArea/',
    'D:/Proccess/TempArea3/'] 
    #LIST PATH
    for index, PATH in enumerate(Pathlist):
        print('%s. %s' % (index, PATH))
    Pchoice= int(input())
    if not Pchoice:
        os.mkdir(Pchoice)
    #SELECT PATH
    Workdir = Pathlist[Pchoice]
    #CHANGE WORK PATH
    os.chdir(Workdir)

def AudioSegment(Files = []):
    while True:
        for abpath, dirs, filename in os.walk(os.getcwd()):
            if abs(abpath.count(os.sep) - os.getcwd().count(os.sep)) >= 1:
                continue
            Files.extend(filename)
        print()
        for index, count in enumerate(Files): print('%s. %s' % (index, count))
        Fchoice = Files[int(input('\nChoose index to select file. -'))]

        #FFMPEG(Time)
        print('\n');os.system('ffprobe -hide_banner -i %s'%(Fchoice));print('\n')

        PrimarySet = {'StHour':int(input('Start Hour: ')), 
        'StMinute':int(input('Start Minute: ')), 
        'StSecond':int(input('Start Second: ')), 
        'Dhour':int(input('Duration Hour: ')), 
        'Dminute':int(input('Duration Minute: ')), 
        'Dsecond':int(input('Duration Second: ')),
        'Times':int(input('Segments: '))
        }

        StartTime = timedelta(hours=PrimarySet['StHour'], minutes=PrimarySet['StMinute'], seconds=PrimarySet['StSecond'])
        Duration = timedelta(hours=PrimarySet['Dhour'], minutes=PrimarySet['Dminute'], seconds=PrimarySet['Dsecond'])
        NameStructure = Fchoice[0:-4]
        for cycle in range(PrimarySet['Times']):
            if cycle > 0:
                StartTime += Duration
            print(StartTime)

            Shell = ("ffmpeg -hide_banner -hwaccel vulkan -i %s -vn -rf64 auto -c:a copy -strict -2 -y -safe 0 -ss %s -t %s .\elements\%s"
            % (Fchoice, StartTime, Duration, '%sp%s-%s.aac' % (NameStructure ,cycle, rd.randrange(1000,9999))))
            # Shell = ("ffmpeg -hide_banner -hwaccel vulkan -i %s -vn -rf64 auto -c:a aac -ab 720k -ar 96000 -af \"volume=2\" -strict -2 -y -safe 0 -ss %s -t %s .\elements\%s"
            # % (Fchoice, StartTime, Duration, '%sp%s-%s.aac' % (NameStructure ,cycle, rd.randrange(1000,9999))))

            print('\n\n%s\n\n' % (Shell))
            os.system(Shell)
            # os.system("ffmpeg -hide_banner -hwaccel vulkan -i %s -vn -rf64 auto -c:a pcm_f64le -strict -2 -ar 384000 -ab 480k -y -safe 0 -ss %s -t %s .\elements\%s"
            # % (Fchoice, StartTime, Duration, '%sp%s-%s.wav' % (NameStructure ,cycle, rd.randrange(1000,9999))))
        
        Choice = input('Game over? ')
        if Choice == 'y':
            break
        else:
            pass

def DTS():
    #SLECT FILE
    filelist = []
    for abpath, dirs, filename in os.walk(os.getcwd()):filelist.extend(filename); print()
    for findex, name in enumerate(filelist):print('%s. %s' % (findex, name));print()
    a1 = filelist[int(input('a1: '))]
    a2 = filelist[int(input('a2: '))]
    # for findex, name in enumerate(filelist):print('%s. %s' % (findex, name));print()
    a3 = filelist[int(input('a3: '))]
    a4 = filelist[int(input('a4: '))]
    # for findex, name in enumerate(filelist):print('%s. %s' % (findex, name));print()
    a5 = filelist[int(input('a5: '))]
    a6 = filelist[int(input('a6: '))]
    # # for findex, name in enumerate(filelist):print('%s. %s' % (findex, name));print()
    # a7 = filelist[int(input('a7: '))]
    # a8 = filelist[int(input('a8: '))]
    # a1 = filelist[0];a2 = filelist[1];a3 = filelist[2];a4 = filelist[3];a5 = filelist[4];a6 = filelist[5];a7 = filelist[6];a8 = filelist[7]
    # print()

    Cmd0 = ('ffmpeg -hide_banner -hwaccel vulkan -i \"%s\" -i \"%s\" -i \"%s\" -i \"%s\" -i \"%s\" -i \"%s\"' 
    % (a1, a2, a3, a4, a5, a6) + " ")

    # Cmd1 = ('-y -safe 0 -rf64 auto -strict -2 -c:a pcm_f64le -ar 384000 -ac 8 -ab 720k '+' ')
    Cmd1 = ('-y -safe 0 -rf64 auto -strict -2 -c:a eac3 -ar 48000 -ac 6 -ab 3001k'+' ')

    # Cmd2 = ('-filter_complex \"[0:a][1:a][2:a][3:a][4:a][5:a][6:a][7:a]')
    Cmd2 = ('-filter_complex \"[0:a][1:a][2:a][3:a][4:a][5:a]')    

    # Cmd3 = ('join=inputs=8:channel_layout=cube:map=0.0-FL|1.0-FR|2.0-BL|3.0-BR|4.0-TFL|5.0-TFR|6.0-TBL|7.0-TBR[a]\"'+' ')
    Cmd3 = ('join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-LFE|4.0-BL|5.0-BR[a]\"'+' ')

    Cmd4 = ('-map \"[a]\" AudioChannel86.wav')

    print(str(Cmd0+Cmd1+Cmd2+Cmd3+Cmd4))
    os.system(str(Cmd0+Cmd1+Cmd2+Cmd3+Cmd4))

def Info():
    #SLECT FILE
    filelist = []
    for abpath, dirs, filename in os.walk(os.getcwd()):filelist.extend(filename); print()
    for findex, name in enumerate(filelist):print('%s. %s' % (findex, name));print()
    File = filelist[int(input('File: -'))]
    os.system('ffprobe -hide_banner -i \"%s\"' % (File))

def TimeCaculating(CTime=timedelta(0), Collection = [], Counter=0, Temp = []):
    for abpath, dirs, filename in os.walk(os.getcwd()):
        if abpath.count(os.sep) - os.getcwd().count(os.sep) > 1:
            continue
        Temp.extend(filename)
    for index, files in enumerate(Temp):print('%s. %s' % (index + 1, files));print()
    format_name = '.' + input('Docker Format: -')
    for Filter in Temp:
        if format_name in Filter:
            Collection.append(Filter)
    for operator in Collection:
        os.system('ffprobe -hide_banner -i \"%s\"' % (operator))
        # operator = operator
        # with ct.closing(wave.open(operator,'r')) as Docker:
        #     Docker_Frames = Docker.getnframes()
        #     Docker_Sampling_Rate = Docker.getframerate()
        #     Docker_Duration = Docker_Frames / float(Docker_Sampling_Rate)
        #     print('%s\'s Docker Duration' % (operator), Docker_Duration)
        #     CTime += timedelta(seconds=Docker_Duration)
    All_time = input('Please enter the length of all containers: -').split()
    for operator in All_time:
        Hours = int(f'%s'%(operator[0:2]))
        Minutes = int(f'%s'%(operator[3:5]))
        Seconds = int(f'%s'%(operator[6:8]))
        Miliseconds = int(f'%s'%(operator[9:12]))
        CTime += timedelta(hours=Hours, minutes=Minutes, seconds=Seconds, milliseconds=Miliseconds)
    print('Total Duration: ', CTime)
    print('Recommended segment duration: ', CTime / 6)
    input('Waiting for pass....')

# def Concat(Collection = [], Temp = []):
#     format_name = '.' + input('Format: -')
#     for abpath, dirs, filename in os.walk(os.getcwd()):
#         if abs(abpath.count(os.sep) - os.getcwd().count(os.sep)) >= 1:
#             continue
#         Temp.extend(filename)
#     for index, files in enumerate(filename):print('%s. %s' % (index + 1, files));print()
#     for Filter in Temp:
#         if format_name in Filter:
#             Collection.append(Filter)
#     with open('concat.log','wt',encoding='utf-8') as File:
#         for operator in range(len(Collection)):
#             if operator < len(Collection) - 1:
#                 File.writelines("file \'%s\'\n" % (Collection[operator]))
#             else:
#                  File.writelines("file \'%s\'" % (Collection[operator]))
#     print('concat.log created.')
#     input('Enter any keywords pass.')

def Concat(Collection = [], Temp = []):
    format_name = '.' + input('Format: -')
    for abpath, dirs, filename in os.walk(os.getcwd()):
        if abs(abpath.count(os.sep) - os.getcwd().count(os.sep)) >= 1:
            continue
        Temp.extend(filename)
    # 使用列表推导式筛选出符合格式名的文件
    Collection = [Filter for Filter in Temp if format_name in Filter]
    with open('concat.log','wt',encoding='utf-8') as File:
        # 使用join方法将文件名连接成字符串
        File.write("\n".join("file \'%s\'" % file for file in Collection))
    print('concat.log created.')
    input('Enter any keywords pass.')

def AudioSucker():
    format_name = '.' + input('Audio Format: -')
    for abpath, dirs, filename in os.walk(os.getcwd()):pass
    for index, files in enumerate(filename):print('%s. %s' % (index + 1, files))
    print(); sleep(1)
    for operator in filename:
        output_name = operator[0:-4] + format_name
        os.system('ffmpeg -hide_banner -hwaccel vulkan -i \"%s\" -vn -codec copy \"%s\"' % (operator, output_name))
            
    


if __name__ == '__main__':
    while True:
        Decision = input("""
        1.AudioSegment
        2.DTS
        3.Info
        4.Audio Sucker
        5.Duration Caculating
        6.Concat List
        e.Exit
        """)
        if Decision == '1':
            PathSelect()
            AudioSegment()
        elif Decision == '2':
            PathSelect()
            DTS()
        elif Decision == 'e':
            break
        elif Decision == '3':
            PathSelect()
            Info()
        elif Decision == '4':
            PathSelect()
            AudioSucker()
        elif Decision == '5':
            PathSelect()
            TimeCaculating()
        elif Decision == '6':
            PathSelect()
            Concat()
        else:
            print('Invalid Parametre.')