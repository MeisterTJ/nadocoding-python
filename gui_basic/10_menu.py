# 메뉴
from tkinter import *

root = Tk()

def create_new_file():
    print("Create New File.")


menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()   # 구분줄 추가
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")    # 비활성화된 메뉴
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
# 위에서 만든 menu_file을 File 메뉴에 넣는다.
menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop()