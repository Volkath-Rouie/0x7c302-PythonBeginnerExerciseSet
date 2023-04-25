import os; from time import sleep
import psutil; import re
from pydub import AudioSegment; import base64
import sys; from cgitb import text
import traceback; from stringprep import map_table_b3
import uuid; import random
import requests; import json
import shutil; from datetime import datetime
import time; from time import *
import tkinter as tk
from tkinter import filedialog
import subprocess
import threading
import time


#更改工作目录
os.chdir((os.getcwd())+'\\Universe\\')
textfilename = 'text.txt'


#去除文本杂项数据
Format_Primary = ''
with open(textfilename,'rt',encoding='utf-8') as File:
    for Loop in File.readlines():
        Format_Primary += Loop.strip()
    Format_Primary = re.sub('\[;\];\';\\n','',str(Format_Primary))
    print('Text Size: {:.2f}KB'.format( os.stat(textfilename).st_size / 1024 ))


#序列化并分段文本
Format_Secondary = str(Format_Primary)
Format_Secondary.replace('\n', '')
Text_Segment_Standard = 320
Text_Segment_Num = len(Format_Secondary) // Text_Segment_Standard + 1
Text_Segments = []
for Loop0 in range(1, Text_Segment_Num + 1):    # [1, Text_Segment] <==> [1, Text_Segment + 1)
    p1 = Text_Segment_Standard * (Loop0 - 1)
    p2 = Text_Segment_Standard * Loop0      #Segment ==> [Primary:End + 1)
    if not (Loop0 == Text_Segment_Num):
        Text_Segments.append(Format_Secondary[p1: p2])
    else:
        Text_Segments.append(Format_Secondary[p1: len(Format_Secondary)])


def openspeech(URL, RE, HD, OF):
    try:
        resp = requests.post(URL, json.dumps(RE), headers = HD)
        # resp = requests.post(api_url, json.dumps(request_json), headers = header)
        # print(f"resp.body: \n{resp.json()}")
        if 'data' in resp.json():
            data = resp.json()['data']
            with open(OF, 'wb') as File_to_Save:
                File_to_Save.write(base64.b64decode(data))
                print('%s created.' % (OF), ' Respone Code: %s' % (resp.status_code), ' Size:{:.2f}MB'.format( (os.stat(OF).st_size) / 1024**2 ))
        else:
            print(f'{resp.json()}')
    except Exception as e:
        traceback.print_exc()

title = input('Output Merge Filename: ')
# SP = [] #准备线程池

for Loop2 in range(Text_Segment_Num):
    print('Proccessing:......{:.2f}%'.format((Loop2 * 100) / Text_Segment_Num))
    wave_path = 'D:/Proccess/Python/wave_files/'   #wave convert path
    wave_filename = wave_path+'%s.mp3' % (Loop2)      #export wave filename
    text = Text_Segments[Loop2]
    #Service Parametre
    appid = '1573034177'
    access_token = 'll1YSVeQ3oPmVy05jBtAIM0u-5WXRrKb'
    cluster = 'volcano_tts'
    voice_type = 'BV405_streaming'                  #Speaker Type
    voice = 'other'
    style_name = 'surprise'
    """
    通用场景	灿灿	参考Q2	BV700_streaming	✔	✔	
    超自然音色-梓梓	other	BV406_streaming		✔	
    超自然音色-燃燃	other	BV407_streaming		✔	
    甜美小源	other	BV405_streaming
    """
    host = 'openspeech.bytedance.com'
    api_url = f'https://{host}/tts_middle_layer/tts'
    header = {'Authorization': f'Bearer;{access_token}'}

    request_json = {
            'app': {
                'appid': appid,
                'token': 'access_token',
                'cluster': cluster
            },
            'user': {
                'uid': '2100181714',
            },
            'audio': {
                'voice': voice,
                'voice_type': voice_type,          #BV405_streaming
                'style_name': style_name,        #语气参数
                'encoding': 'mp3',
                'speed': 10,
                'volume': 10,
                'pitch': 10,
                'bitrate': 320,
                'bits': 32,
                'rate': 48000,
                'silence_duration': 0,
            },
            'request': {
                'reqid': str(uuid.uuid4()),
                'text': text,
                'text_type': 'plain',
                'operation': 'query',
            }
        }
    
    threading.Thread(target=openspeech(URL=api_url, RE=request_json, HD=header, OF=wave_filename), name=f'Speech_Proccess_{Loop2}').start()

print('Speech Service Done.')

root = tk.Tk()
root.withdraw()

def Get_Files_Info(Files = []):
    Selection = filedialog.askopenfilenames(title="Select files you want to add to concat list file", filetypes=[('Same Docker', '*.*')], initialdir=('D:/Entertament/Guider'))
    if Selection:
        Workpath = (os.path.split(Selection[0]))[0]
        Workfiles = [(os.path.split(workfile))[1] for workfile in Selection]
        Workformat = (os.path.splitext(Workfiles[0]))[1]
        return Workpath, Workfiles, Workformat
    else:
        exit(print('Not select any files.'))

def Write_Concat_Info(Path, Dockers):
    with open('concat.txt','wt',encoding='utf-8') as Concat:
        for docker in Dockers[0:-1]:
            textLine = f'file \'{docker}\'\n'
            Concat.writelines(textLine)
        Concat.writelines(f'file \'{Dockers[-1]}\'')

def Check_Result():
    with open('concat.txt','rt',encoding='utf-8') as Concat:
        info = Concat.read()
    print(info)
    return info       

if __name__ == '__main__':
    with open(wave_path+'concat.txt', 'wt', encoding='utf-8') as File:
        for j in range(Text_Segment_Num - 1):
            File.writelines(f'file \'{wave_path}{j}.mp3\'\n')
        File.writelines(f'file \'{wave_path}{Text_Segment_Num - 1}.mp3\'')
    choice = input("""1.merge all audios into a audio you have named and then remove elements of them\n2.pass\n""")
    if choice == '1':
        os.system(f'ffmpeg -hide_banner -f concat -safe 0 -i {wave_path}concat.txt -y -codec copy \"{wave_path}{voice_type}-{title}.mp3\"')
        print('Final result done'.center(100,'*'))
        if input('Whether delete them or not? -y/n') == 'y':
            for n in range(Text_Segment_Num):
                try:
                    os.remove(f'{wave_path}{n}.mp3')
                except:
                    pass
            print('All elements removed.')
        else:
            pass
    elif choice == '2':
        pass
    else:
        pass   












"""
1.【有声阅读音色】支持「7」种情感调用,可以通过style_name来演绎不同情感,不传递默认为neutral。voice传递Narrator(旁白)时,多情感演绎能力不明显。

neutral(无情感)、happy(开心)、sad(悲伤)、angry(生气)、scare(害怕)、hate(厌恶)、surprise(惊讶)
【BV700_streaming灿灿】支持「7」种情感/风格
当「voice」为「BV700Cardrive」时,可以通过style_name来演绎不同情感,neutral(通用_无情感)、happy(开心)、sorry(抱歉)、angry(生气)
当「voice」为「BV700Customer_service」时,可以通过style_name来演绎不同风格,neutral(客服)、professional(专业)、serious(严肃)
【BV001_streaming通用女声】
当「voice」为「other」时,可以通过style_name来演绎不同情感,neutral(无情感)、happy(开心)、sad(悲伤)、angry(生气)、scare(害怕)、hate(厌恶)、surprise(惊讶)
通过配置「voice」来演绎不同风格,assistant(助手)、customer_service(客服)、gentle(鸡汤)、advertising(广告)、child_story(教育)
"""





"""
中文 #
场景	
推荐音色
voice
voice_type
是否有多情感
是否有时间戳功能
落地业务
通用场景	灿灿	参考Q2	BV700_streaming	✔	✔	
超自然音色-梓梓	other	BV406_streaming		✔	
超自然音色-燃燃	other	BV407_streaming		✔	
通用女声

参考Q2

BV001_streaming

✔

剪映、
今日头条

通用男声

other

BV002_streaming

✔

剪映、
今日头条

有声阅读	擎苍	BV701DialogMale	BV701_streaming	✔	✔	
阳光青年	BV123DialogMale	BV123_streaming	✔		番茄小说
反卷青年	BV120DialogMale	BV120_streaming	✔	✔	番茄小说
通用赘婿	BV119DialogMale	BV119_streaming	✔		番茄小说
古风少御	BV115DialogFemale	BV115_streaming	✔		番茄小说
霸气青叔	BV107DialogMale	BV107_streaming	✔	✔	番茄小说
质朴青年	BV100DialogMale	BV100_streaming	✔		番茄小说
温柔淑女	BV104DialogFemale	BV104_streaming	✔	✔	番茄小说
开朗青年	BV004DialogMale	BV004_streaming	✔	✔	番茄小说
甜宠少御	BV113DialogFemale	BV113_streaming	✔		番茄小说
儒雅青年	BV102DialogMale	BV102_streaming	✔	✔	番茄小说
智能助手	甜美小源	other	BV405_streaming		✔	
亲切女声	other	BV007_streaming		✔	火山外呼机器人、懂车帝
知性女声	other	BV009_streaming		✔	剪映
诚诚	other	BV419_streaming		✔	
童童	other	BV415_streaming		✔	
亲切男声	other	BV008_streaming		✔	
视频配音	译制片男声	other	BV408_streaming		✔	剪映
鸡汤女声	other	BV403_streaming		✔	剪映
智慧老者	other	BV158_streaming		✔	
慈爱姥姥	other	BV157_streaming		✔	
说唱小哥	other	BR001_streaming		✔	剪映
活力解说男	other	BV410_streaming		✔	
影视解说小帅	other	BV411_streaming		✔	
影视解说小美	other	BV412_streaming		✔	
反卷青年	BV120DialogMale	BV120_streaming	✔	✔	番茄小说
沉稳解说男	other	BV142_streaming		✔	
潇洒青年	other	BV143_streaming		✔	
阳光男声	other	BV056_streaming		✔	剪映
活泼女声	other	BV005_streaming		✔	剪映
小萝莉	other	BV064_streaming			剪映
特色音色	奶气萌娃	other	BV051_streaming			剪映
动漫海绵	other	BV063_streaming		✔	剪映
动漫海星	other	BV417_streaming		✔	
动漫小新	other	BV050_streaming			剪映
天才童声	other	BV061_streaming		✔	
广告配音

促销男声

other

BV401_streaming

✔

剪映、
巨量引擎

促销女声

other

BV402_streaming

✔

剪映、
巨量引擎

磁性男声

other

BV006_streaming

✔

剪映、
巨量引擎

新闻播报	新闻女声	other	BV011_streaming		✔	今日头条
新闻男声	other	BV012_streaming		✔	今日头条
教育场景	知性姐姐-双语	other	BV034_streaming			瓜瓜龙
温柔小哥	other	BV033_streaming		✔	瓜瓜龙
多语种 #
场景	
推荐音色
voice	
voice_type
是否有时间戳功能
落地业务
英语	慵懒女声-Ava	other	BV511_streaming	✔	
议论女声-Alicia	other	BV505_streaming	✔	
澳洲男声-Henry	other	BV516_streaming	✔	
情感女声-Lawrence	other	BV138_streaming	✔	
美式女声-Amelia	other	BV027_streaming		CapCut
讲述女声-Amanda	other	BV502_streaming		CapCut
活力女声-Ariana	other	BV503_streaming	✔	CapCut
活力男声-Jackson	other	BV504_streaming		CapCut
日语	元气少女	other	BV520_streaming		CapCut
可爱萌娃	other	BV523_streaming		CapCut
萌系少女	other	BV521_streaming		CapCut
气质女声	other	BV522_streaming		CapCut
日语男声	other	BV524_streaming		CapCut
葡萄牙语	活力男声Carlos(巴西地区)	other	BV531_streaming		
葡萄牙语	活力女声(巴西地区)	other	BV530_streaming		
西班牙语	气质御姐(墨西哥地区)	other	BV065_streaming		
方言 #
场景	推荐音色	voice	
voice_type
是否有时间戳功能
落地业务
东北话

东北老铁

other

BV021_streaming

✔

剪映、
番茄小说

广西普通话	广西表哥	other	BV213_streaming	✔	剪映
台湾普通话	甜美台妹	other	BV025_streaming		剪映
粤语	港剧男神	other	BV026_streaming	✔	剪映
天津话

相声演员

other

BV212_streaming

剪映、
番茄小说

重庆话	重庆小伙	other	BV019_streaming	✔	剪映
郑州话	乡村企业家	other	BV214_streaming		剪映
"""