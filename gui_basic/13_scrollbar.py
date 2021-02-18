# 스크롤 바
from tkinter import *

root = Tk()
root.geometry("320x240")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
# 오른쪽으로, y 방향으로 쭈욱 늘어난 스크롤바
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라온다.
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):  # 1 ~ 31일
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# 스크롤바 조작 시 리스트박스 스크롤 되도록 연결
scrollbar.config(command=listbox.yview)

root.mainloop()