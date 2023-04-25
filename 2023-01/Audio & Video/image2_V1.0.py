import subprocess
import os
from tkinter import filedialog
import tkinter as tk
import time

window = tk.Tk()
window.withdraw()

def get_audio_entries():
    audio_path = filedialog.askopenfilename(title='Select matched audio.', filetypes=[('Audio','*.mp3 *.wav, *.flac')], initialdir=(os.getcwd()))
    audio_name = (os.path.split(audio_path))[1]
    audio_duration = float(subprocess.check_output(f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 \"{audio_name}\"', shell=True))
    return audio_duration, audio_name

def single_image_video(duration, audio_name):
    image_path = filedialog.askopenfilename(title='Select matched image or video.', filetypes=[('Image & video','*.jpg *.png *.mp4 *.flv')], initialdir=(os.getcwd()))
    image_name = (os.path.split(image_path))[1]
    image_format = (os.path.splitext(image_name))[1]
    resulution = subprocess.check_output(f'ffprobe -v error -show_entries stream=width,height -of csv=p=0 \"{image_name}\"', shell=True)
    output1, output2 = resulution.decode().split(',')
    width = int(output1)
    height = int(output2)
    ratio = width / height
    standard_width = 7680
    standard_height = int((standard_width / ratio) // 1)

    print(f'\n\nwidth:{width}\nheight:{height}\nratio:{ratio}\nnew_width:{standard_width}\nnew_height:{standard_height}\nnew resulution:{standard_width}:{standard_height}\n\n')
    if image_format == '.png' or image_format == '.jpg':
        os.system(f'ffmpeg -hwaccel vulkan -f image2 -stream_loop -1 -i \"{image_name}\" -c:v h264_qsv -t 00:00:01 -y -r 1 -vf \"scale={standard_width}:{standard_height}\" -b:v 1500k 1s-video.mp4')

        os.system(f'ffmpeg -stream_loop -1 -i 1s-video.mp4 -y -codec copy -t {duration} full-video.mp4')

    else:
        os.system(f'ffmpeg -stream_loop -1 -i \"{image_name}\" -t {duration} -codec copy full-video.mp4')
    
    os.system(f'ffmpeg -i {audio_name} -i full-video.mp4 -codec copy -y Complete_Video.mp4')
    os.remove('full-video.mp4')
    if not os.path.exists('full-video.mp4'):
        print('Removed Redundant Element.')


if __name__ == '__main__':
    Workpath = filedialog.askdirectory(initialdir=('D:/Proccess/') )
    if Workpath:
        os.chdir(Workpath)
        Audio_Duration, Audio_Name = get_audio_entries()
        Exact_Audio_Duration = time
        single_image_video(duration=Audio_Duration, audio_name=Audio_Name)
    else:
        print('Not selectinf Work Directory.')
        exit()

























# if metavideo:
#     metavideo = '{:.2f}MB'.format(os.stat('1s-video.mp4').st_size / 1024**2)
#     print(f'1s-video.mp4\t{metavideo}')
# elif fullvideo:
#     fullvideo = '{:.2f}MB'.format(os.stat('full-video.mp4').st_size / 1024**2)
#     print(f'full-video\t{fullvideo}')
# elif video:
#     video = '{:.2f}MB'.format(os.stat('Complete_Video.mp4').st_size / 1024**2)
#     print(f'Video\t{video}')        