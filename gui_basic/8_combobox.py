# 콤보 박스
# tkinter.ttk를 임포트하는데 이름은 ttk로 사용한다.
import tkinter.ttk as ttk   # 콤보 박스를 사용하기 위해서는 이게 필요하다.
from tkinter import *

root = Tk()

values = [str(i) + "일" for i in range(1, 32)]   # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")  # 최초 목록 제목 설정

# 콤보박스 선택만 가능하고, 사용자의 입력이 불가능하다.
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)    # 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())    # 선택된 값 표시
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()