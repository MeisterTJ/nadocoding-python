# 리스트 박스
from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480")  # 창 크기

# selectmode : 몇 개 선택 가능한가?
# height : 0이면 다 보여주고, 그 외에는 몇 개 보여줄지를 설정한다.
listbox = Listbox(root, selectmode="extended", height=5)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")   # 맨 뒤에 값을 넣어준다.
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # listbox.delete(END)
    # print("리스트에는 : ", listbox.size())

    # 항목 확인 (str을 반환)
    print("1번째부터 3번째까지의 항목", listbox.get(0, 2))

    #선택된 항목 확인 (인덱스로 반환)
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()