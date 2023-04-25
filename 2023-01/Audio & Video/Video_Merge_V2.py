#encoding=utf-8
import tkinter as tk
import traceback as tr

try:
    Windows = tk.Tk()
    Windows.title('Video Merge')
    Windows.geometry('960x540+300+120')
    Windows.attributes('-alpha',0.9)
    Windows['background'] = '#ffffff'
    Message = tk.Label(Windows, text='Video Files:', width=10,height=2, font=('Microsoft Yahei',20), justify='left', 
    background='green', anchor='e'); Message.grid() 
    

    #Permanentative Windows
    Windows.mainloop()
except Exception as e:
    print(tr.print_exc())