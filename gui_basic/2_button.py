from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()  # 생성한 버튼을 포함

# padx, pady는 글자를 완전히 포함한 후 공간을 확보한다.
btn2 = Button(root, padx=5, pady=10, text="버튼22222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# width, height는 고정 크기이다.
btn4 = Button(root, width=10, height=3, text="버튼44444444444")
btn4.pack()

# 노란색 배경에 빨간색 글씨
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지를 읽어온다.
photo = PhotoImage(file="img.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭 되었습니다.")


# 버튼 동작
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()
