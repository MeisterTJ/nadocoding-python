from tkinter import *

root = Tk()
root.title("Nado GUI")
# root.geometry("640x480")          # 창 크기
root.geometry("640x480+200+200")    # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False)        # x, y 창 크기 변경 불가

root.mainloop()