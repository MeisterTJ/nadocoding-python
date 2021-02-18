# 프로그레스 바
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()

# indeterminate는 결정되지 않았다. 바가 와리가리 한다는 의미
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10)   # 10ms 마다 움직임
progressbar.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(10)   # 10ms 마다 움직임
progressbar2.pack()

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()

def btncmd():
    progressbar.stop()  # 작동 중지
    progressbar2.stop()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01초 대기
        p_var3.set(i)
        progressbar3.update()   # 루프마다 gui를 업데이트 하기 위해서
        print(p_var3.get())     # 1.0 ~ 100.0

btn = Button(root, text="중지", command=btncmd)
btn.pack()

btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop()