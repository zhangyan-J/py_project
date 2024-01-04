# from tkinter import *
# from tkinter import messagebox
#
# def get_height():
#     # 获取身高数据(cm)
#     height = float(ENTRY2.get())
#     return height
#
# def get_weight():
#     # 获取体重数据(kg)
#     weight = float(ENTRY1.get())
#     return weight
#
# def calculate_bmi():
#     # 计算BMI系数
#     try:
#         height = get_height()
#         weight = get_weight()
#         height = height / 100.0
#         bmi = weight / (height ** 2)
#     except ZeroDivisionError:
#         messagebox.showinfo("提示", "请输入有效的身高数据!!")
#     except ValueError:
#         messagebox.showinfo("提示", "请输入有效的数据!")
#     else:
#         messagebox.showinfo("你的BMI系数是: ", bmi)
#
# if __name__ == '__main__':
#     # 实例化object，建立窗口TOP
#     TOP = Tk()
#     TOP.bind("<Return>", calculate_bmi)
#     # 设定窗口的大小(长 * 宽)
#     TOP.geometry("400x400")
#     # 窗口背景颜色
#     TOP.configure(background="#8c52ff")
#     # 窗口标题
#     TOP.title("BMI 计算器")
#     TOP.resizable(width=False, height=False)
#     LABLE = Label(TOP, bg="#8c52ff", fg="#ffffff", text="欢迎使用 BMI 计算器", font=("Helvetica", 15, "bold"), pady=10)
#     LABLE.place(x=55, y=0)
#     LABLE1 = Label(TOP, bg="#ffffff", text="输入体重(单位：kg):", bd=6,
#                    font=("Helvetica", 10, "bold"), pady=5)
#     LABLE1.place(x=55, y=60)
#     ENTRY1 = Entry(TOP, bd=8, width=10, font="Roboto 11")
#     ENTRY1.place(x=240, y=60)
#     LABLE2 = Label(TOP, bg="#ffffff", text="输入身高(单位：cm):", bd=6,
#                    font=("Helvetica", 10, "bold"), pady=5)
#     LABLE2.place(x=55, y=121)
#     ENTRY2 = Entry(TOP, bd=8, width=10, font="Roboto 11")
#     ENTRY2.place(x=240, y=121)
#     BUTTON = Button(bg="#000000", fg='#ffffff', bd=12, text="BMI", padx=33, pady=10, command=calculate_bmi,
#                     font=("Helvetica", 20, "bold"))
#     BUTTON.grid(row=5, column=0, sticky=W)
#     BUTTON.place(x=115, y=250)
#     TOP.mainloop()

### python 使用tkinter&subprocess 制作adb工具
# 工具涵盖功能：
# 1.查看车机版本，5G版本，mcu版本
# 2.提供一个同步按钮，点击后同步飞书云文档指定sheet页的数据到本地，且在指定路径生成最新的bat文件，
# 3.执行adb命令集，一般是多个adb shell命令
# 4.执行shell命令集
# 5.提供多个tab页，不同tab页不同功能
##需要调试的点：
# 1.多个设备连接时，获取多个设备devices id，指定device id获取版本信息，安装apk
# 2.
from tkinter import *
import subprocess
import tkinter.filedialog
import re
def getDevicesVersion():
    command_getVersion = 'adb shell getprop ro.build.version.release'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString.wait()
    versionString=versionString.decode()
    versionString = re.split('\n', versionString)[0].strip('\r')
    s='%s\n' % versionString
    txt.insert(END, s)
def getDevices():
    command_getVersion = 'adb devices'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)
def getApkPackageName():
     filename=tkinter.filedialog.askopenfilename()
     if filename != '':
         command = 'aapt d bading '+filename+' | grep package'
         returnStr = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
         returnStr=returnStr.decode('gbk')
     else:
         txt.insert(END, '未选择文件')
def listPackages():
    command_getVersion = 'adb shell pm list packages'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString=versionString.decode()
    txt.insert(END, '%s\n' % versionString)
def listPackages3():
    command_getVersion = 'adb shell pm list packages -3'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString=versionString.decode()
    txt.insert(END, '%s\n' % versionString)
def listPackagesSys():
    command_getVersion = 'adb shell pm list packages -s'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString=versionString.decode()
    txt.insert(END, '%s\n' % versionString)
def localInstall():
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         command = 'adb install '+filename
         versionString = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
         versionString=versionString.decode()
         txt.insert(END, '%s\n' % versionString)
    else:
         txt.insert(END, '未选择文件')
def getResolution():
    command_getVersion = 'adb shell  wm size'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString=versionString.decode()
    txt.insert(END, '%s\n' % versionString)
def getPixelDensity():
    command_getVersion = 'adb shell wm density'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
    versionString=versionString.decode()
    txt.insert(END, '%s\n' % versionString)
win = Tk()
win.geometry('620x360')
win.title('adb命令工具箱')

# 在窗体垂直自上而下位置50%处起，布局相对窗体高度50%高的文本框
txt = Text(win)
txt.place(rely=0.5, relheight=0.5)

btn1 = Button(win, text='hu版本', command=getDevicesVersion)
btn1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
btn2 = Button(win, text='获取设备', command=getDevices)
btn2.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
btn3=Button(win,text='选择apk安装',command=localInstall)
btn3.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
btn4 = Button(win, text='查看安装包名', command=listPackages)
btn4.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.1)
btn5 = Button(win, text='查看第三方包名', command=listPackages3)
btn5.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.1)
btn6 = Button(win, text='查看车机系统包名', command=listPackagesSys)
btn6.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.1)
# btn7 = Button(win, text='查看手机分辨率', command=getResolution)
# btn7.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.1)
# btn8 = Button(win, text='查看手机像素密度', command=getPixelDensity)
# btn8.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.1)
# btn9 = Button(win, text='查看手机', command=listPackages)
# btn9.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1)

win.mainloop()
