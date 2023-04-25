import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import random

root = tk.Tk()
root.withdraw()

file_paths = filedialog.askopenfilenames(title='选择一个或多个视频文件', filetypes=[('Video files', '*.mp4 *.avi *.mkv')])


if not file_paths:
    print('没有选择任何文件')
    exit()

os.chdir(  (os.path.split(str(file_paths[0])))[0]  )
print(os.getcwd())

if len(file_paths) == 1:
    output_file = file_paths[0]
    print('只选择了一个文件，不进行并行计算')

else:
    input_names = [os.path.splitext(os.path.basename(file_path))[0] for file_path in file_paths]
    input_dockernames = [os.path.split(dockername)[1] for dockername in file_paths]
    random.shuffle(input_names)
    output_name = '_'.join(input_names[:3]) + '.aac'
    with open('concat.txt', 'wt', encoding='utf-8') as File:
        for i in range(len(input_dockernames)):
            file_indicator = f'file \'{input_dockernames[i]}\''
            if i != len(input_dockernames) - 1:
                File.writelines(file_indicator+'\n')
            else:
                File.writelines(file_indicator)

    output_dir = os.path.dirname(file_paths[0])
    output_file = os.path.join(output_dir, output_name)
    cmd = f'ffmpeg -hide_banner -hwaccel vulkan -f concat -safe 0 -i concat.txt -c:a copy -vn -b:a 640k -y -strict -2 {output_name}'
    os.system(cmd)

cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {output_name}'
total_duration = float(subprocess.check_output(cmd, shell=True))

audio_duration = total_duration / 6

cmd2 = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio_0.aac'
if os.path.exists('audio_0.aac'):
    origin_audio_time = float(subprocess.check_output(cmd2, shell=True))
else:
    origin_audio_time = 0

if origin_audio_time != audio_duration:
    for i in range(6):
        start_time = i * audio_duration
        output_file_i = f'audio_{i}.aac'
        cmd1 = f'ffmpeg -hide_banner -hwaccel vulkan -i {output_file} -ss {start_time} -t {audio_duration} -vn -acodec copy -y -safe 0 -strict -2 {output_file_i}'
        os.system(cmd1)

dolby_file = os.path.splitext(output_file)[0] + '_DolbyAtomos.wav'

cmd2 = f'ffmpeg -i audio_0.aac -i audio_1.aac -i audio_2.aac -i audio_3.aac -i audio_4.aac \
-i audio_5.aac -c:a eac3 -ar 48000 \
-b:a 3000k \
-filter_complex \"[0:a][1:a][2:a][3:a][4:a][5:a]join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-LFE|4.0-BL|5.0-BR[a]\" \
-map \"[a]\" {dolby_file}'

os.system(cmd2)

def ask_continue():
    root1 = tk.Tk()
    # 隐藏主窗口
    root1.withdraw()
    answer = tk.messagebox.askyesno("确认", "是否继续导出视频？")
    return answer