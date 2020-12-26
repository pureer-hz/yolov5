import os
import threading
from tkinter import *
from tkinter import filedialog

def choose():
    file= filedialog.askopenfilename(parent=init_window, initialdir="C:/",title='Choose an video.')
    path=os.path.abspath(file)
    print(path)
    if('.mp4' in path):
        cmd = "python detect.py --img-size 320 --source " + path + " --weights ./weights/best.pt"
        t1 = threading.Thread(target=action, kwargs={"cmd": cmd})
        t1.start()


def webcam():
    cmd = "python detect.py --source 0 --weights ./weights/best.pt"
    t1=threading.Thread(target=action,kwargs={"cmd":cmd})
    t1.start()

def action(**kwargs):
    os.system(kwargs.get("cmd"))


init_window = Tk()

init_window.title("火焰识别")
init_window.geometry('700x381+300+200')
bt1=Button(init_window,text='选取视频文件识别',width=15,command=choose,bg='yellow')
bt3=Button(init_window,text="摄像头识别",width=15,command=webcam,bg='yellow')
bt1.place(x=280,y=120)
bt3.place(x=280,y=180)
init_window.mainloop()
