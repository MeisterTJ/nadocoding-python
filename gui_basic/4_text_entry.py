# 텍스트 & 엔트리
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")          # 창 크기

# 글자 입력 위젯을 만든다.
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 엔트리는 한줄만 가능하다.
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")


def btncmd():
    # 1.0 = 1번째 행의 0번째 열부터 시작한다는 뜻
    print(txt.get("1.0", END))
    print(e.get())  # 레이블은 get만 하면 된다.
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()