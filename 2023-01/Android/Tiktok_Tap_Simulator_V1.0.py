import os
import threading
import random
import tkinter 

os.chdir('D:\\Init_Program\\AndroidGeneral_Tools\\')
ID = 0

def Tap_Shell():
    x = random.randrange(230,440)
    y = random.randrange(680,700)       #730,820
    os.system(f"adb.exe shell input tap {x} {y}")

def control_thread():
    global running 
    if running: 
        running = False
        button.config(text="Resume")
    else: 
        running = True
        button.config(text="Pause")
        start_thread() 

def start_thread():
    global time_interval_a, time_interval_b
    global ID 
    global running 
    if running: 
        procs = threading.Thread(target=Tap_Shell, name=f'Proc_id_{ID}')
        procs.start()
        ID += 1
        root.after(random.randrange(int(time_interval_a), int(time_interval_b)), start_thread)
def get_input():
    global time_interval 
    global time_interval_a, time_interval_b
    try: 
        time_interval = entry.get()
        time_interval_a, time_interval_b = time_interval.split('-')
    except: 
        tkinter.messagebox.showerror("Error", "Invalid input. Please enter a positive number.")
        time_interval_a, time_interval_b = '20-100'.split('-')

root = tkinter.Tk()
root.title("CN-Tiktok Tap Simulator")
root.geometry("400x300+{}+{}".format((root.winfo_screenwidth() - 300) // 2, (root.winfo_screenheight() - 200) // 2))
root.protocol("WM_DELETE_WINDOW", root.quit)

label = tkinter.Label(root, text="CN-Tiktok Tap Simulator", font=("# Arial", 16))
label.pack(pady=20)

entry = tkinter.Entry(root)
entry.pack()
entry.insert(0, "20-100")
time_interval = '20-100'
time_interval_a, time_interval_b = time_interval.split('-')

button_input = tkinter.Button(root, text="Set", command=get_input)
button_input.pack(pady=10)

button = tkinter.Button(root, text="Start", command=control_thread)
button.pack(pady=10)

running = False

root.mainloop()