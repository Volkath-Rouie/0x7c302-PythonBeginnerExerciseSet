import os; import sys; import psutil
import shutil; import time; import datetime
import random; import requests; import traceback
import chardet; import codecs; import re

Path = 'D:\\Proccess\\Python\\Video\\'
os.chdir(Path)
# original_ass_File = input('ASS Filename: ') + '.ass'
# output_ass_File = input('Output ASS Filename: ')+'.ass'
original_ass_File = 'a.ass'
output_ass_File = '1.ass'

try:
    with open(original_ass_File,'rb') as F1:
        bin_text = F1.read()
        info = chardet.detect(F1.read())
    # print(info)
    text = bin_text.decode('utf-8')
    # text = text.replace('}','\}')
    # text = text.replace('{','\{')
    # text = text.replace('\\','\\\\')
    text = text.encode('mbcs',errors='ignore')
    print(text)
except:
    print(traceback.print_exc())