import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# 创建一个 tkinter 窗口
root = tk.Tk()
root.withdraw()

def ask_continue():
    root1 = tk.TK()
    root1.withdraw()
    answer = tk.tk.messagebox.askyesno("确认", "还需要导出视频吗？")r

# 打开文件选择对话框
file_path = filedialog.askopenfilename(title='选择音视频对象')
output_dir , filename = os.path.split(file_path)
dockername, dockerformat = os.path.splitext(filename)

if file_path:
    os.chdir(output_dir)

    # 使用 FFmpeg 获取视频文件总时长（单位：秒）
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {file_path}'
    total_duration = float(subprocess.check_output(cmd, shell=True))

    # 计算每个音频文件的时长
    audio_duration = total_duration / 6

    # 删除旧的音频文件
    # for i in range(6):
    #     output_file = f'{output_dir}/audio_{i}.aac'
    #     if os.path.exists(output_file):
    #         os.remove(output_file)

    # 使用 FFmpeg 将视频分割成六个时长为 audio_duration 的音频文件
    cmd2 = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio_0.aac'
    if os.path.exists('audio_0.aac'):
        origin_audio_time = float(subprocess.check_output(cmd2, shell=True))
        if origin_audio_time == audio_duration:
            pass
    else: 
        for i in range(6):
            start_time = i * audio_duration
            output_file = f'{output_dir}/audio_{i}.aac'
            cmd = f'ffmpeg -hide_banner -hwaccel vulkan -i {file_path} -ss {start_time} -t {audio_duration} -vn -acodec copy {output_file}'
            subprocess.call(cmd, shell=True)

    # 删除旧的杜比音频文件
    output_file = f'{dockername}dolby_audio.wav'
    if os.path.exists(output_file):
        os.remove(output_file)

    # 使用 FFmpeg 将六个音频文件编码为杜比音频
    cmd = f'ffmpeg -hide_banner -hwaccel vulkan -i audio_0.aac -i audio_1.aac -i audio_2.aac -i audio_3.aac -i audio_4.aac -i audio_5.aac -strict -2 -safe 0 -c:a eac3 -ar 48000 -b:a 3000k -filter_complex \"[0:a][1:a][2:a][3:a][4:a][5:a]join=inputs=6:channel_layout=5.1:map=0.0-FL|1.0-FR|2.0-FC|3.0-LFE|4.0-BL|5.0-BR[a]\" -map \"[a]\" {output_file}'
    subprocess.call(cmd, shell=True)