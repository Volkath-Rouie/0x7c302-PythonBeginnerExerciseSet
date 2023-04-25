import os
import time
import threading
import random

os.chdir('D:\\Init_Program\\AndroidGeneral_Tools\\')
ID = 0

def Tap_Shell():
    x = random.randrange(230,529)
    y = random.randrange(730,820)
    os.system(f"adb.exe shell input tap {x} {y}")
    
while True:
    times_per_second = random.randrange(2, 8)
    time.sleep(1 / times_per_second)
    procs = threading.Thread(target=Tap_Shell, name=f'Proc_id_{ID}').start()
    ID += 1