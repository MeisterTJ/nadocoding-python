# 체크박스
from tkinter import *
root = Tk()

# chkvar에 int 형으로 값을 저장한다.
chkvar = IntVar()

# 체크박스는 variable을 설정해야 체크 상태를 가져올 수 있다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select()     # 선택 처리
chkbox.deselect()   # 선택 해제 처리 (default)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())     # 0 또는 1로 출력
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()