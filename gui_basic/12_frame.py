# 프레임
from tkinter import *

root = Tk()
root.geometry("320x240")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# relief : 테두리, bd : 외곽선
frame_burger = Frame(root, relief="solid", bd=1)
# 왼쪽을 차지하고, both로 왼쪽의 위아래 영역을 다채우고 expand로 다른 프레임을 고려해서 확장
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 제목이 있는 프레임
frame_drink =LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()


root.mainloop()