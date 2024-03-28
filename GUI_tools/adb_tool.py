import os
from tkinter import *


def create_button(file):
    button = Button(root, text=file)
    button.pack()


# 指定要遍历的文件夹路径
folder_path = "D:\practice\github\py_project\GUI_tools"

# 遍历文件夹下的所有文件
for file in os.listdir(folder_path):
    if file.endswith(".bat"):
        # 调用函数创建按钮
        create_button(file[:-4])

# 创建主窗口
root = Tk()
root.mainloop()
