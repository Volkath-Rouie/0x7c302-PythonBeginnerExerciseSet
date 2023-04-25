import os
import datetime

#
Path = 'D:\\Proccess\\TempArea1\\'
os.chdir(Path)

for abpath,root,dirs in os.walk(Path):
    pass

filename_list = []
for loop1 in (dirs):
    if '.flv' in loop1:
        filename_list.append('\''+loop1+'\'')


#Info
output_filename = filename_list[0][0:-15] + '.mp4\"'
output_filename = output_filename.replace('\'','"')
video_bitrate = 500


with open(Path+'concat.txt','wt',encoding='utf-8') as File:
    for loop2 in filename_list:
        File.writelines('file '+loop2+'\n')

os.system('ffmpeg -hwaccel cuda -hwaccel qsv -hwaccel dxva2 -hwaccel d3dllva -hwaccel opencl -hwaccel vulkan -safe 0 -f concat -i concat.txt -strict -2 -codec copy -b:a 320k -b:v %dk %s -y'%(video_bitrate,output_filename))