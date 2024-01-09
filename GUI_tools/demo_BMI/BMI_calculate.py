# -*- coding: utf-8 -*-
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
import os


def run_cmd(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)


def check_adb_devices_ini():
    global devices_list
    import os
    import re

    # 获取所有的安卓设备SN号码
    devices_list = []
    adb_devices_file = 'D:\log\\adb.ini'
    if os.path.exists(adb_devices_file):
        run_cmd('del /f /q ' + adb_devices_file)
    print(run_cmd('adb devices >' + adb_devices_file))

    f = open(adb_devices_file, "r")
    str_list = f.readlines()
    print(str_list)
    if 'device' not in str(str_list[1]):
        print('adb devices:{}。未识别到任何adb设备，请确认安卓设备已正确连接且USB调试已打开...'.format(str_list))
        print("未识别到任何设备，请确认设备已正确连接上...")
        return -1

    count = 1
    for i in str_list:
        if '\tdevice' in i:
            device_name = ''
            device_name = re.sub('\tdevice', '', i).replace('\n', '').strip()
            print("Device_{}_name={}".format(count, device_name))
            devices_list.append(device_name)
            count = count + 1
    print("devices_list={}".format(devices_list))
    return devices_list


def getDevices_hu_Version():
    # 存储所有设备的设备信息，即设备ID，设备版本号，设备的appActivity
    deviceMsgs = []
    # 获取连接设备的版本号、appActivity
    for i in range(0, len(devices_list)):
        id = devices_list[i]
        # 获取连接设备的安卓系统版本
        # versionMsg = list(os.popen('adb -s {} shell getprop ro.build.display.id'.format(id)).readlines())
        # version = str(versionMsg).split("'")[1].split("\\")[0]
        # print("adb命令获取的设备版本号为：", versionMsg)

        hu_versionMsg = list(os.popen('adb -s {} shell getprop ro.build.display.id'.format(id)).readlines())
        hu_command_getVersion = str(hu_versionMsg).split("'")[1].split("\\")[0]
        # 5G_versionMsg = list(os.popen('adb -s {} shell getprop ro.build.display.id'.format(id)).readlines())
        # command_getVersion = str(versionMsg).split("'")[1].split("\\")[0]
        print("处理后获取的设备版本号为：" + hu_command_getVersion)
        versionString = subprocess.Popen(hu_command_getVersion, shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT).stdout.read()
        # versionString.wait()##使用方法待研究
        versionString = versionString.decode('gbk')
        versionString = re.split('\n', versionString)[0].strip('\r')
        s = '%s\n' % versionString
        txt.insert(END, s)


def getDevices_5G_Version():
    # 存储所有设备的设备信息，即设备ID，设备版本号，设备的appActivity
    deviceMsgs = []
    # 获取连接设备的版本号、appActivity
    for i in range(0, len(devices_list)):
        id = devices_list[i]
        # 获取连接设备的安卓系统版本
        # versionMsg = list(os.popen('adb -s {} shell getprop ro.build.display.id'.format(id)).readlines())
        # version = str(versionMsg).split("'")[1].split("\\")[0]
        # print("adb命令获取的设备版本号为：", versionMsg)

        hu_versionMsg = list(os.popen('adb -s {} shell /vendor/bin/get_mcu_version'.format(id)).readlines())
        hu_command_getVersion = str(hu_versionMsg).split("'")[1].split("\\")[0]
        # 5G_versionMsg = list(os.popen('adb -s {} shell getprop ro.build.display.id'.format(id)).readlines())
        # command_getVersion = str(versionMsg).split("'")[1].split("\\")[0]
        print("处理后获取的设备版本号为：" + hu_command_getVersion)
        versionString = subprocess.Popen(hu_command_getVersion, shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT).stdout.read()
        # versionString.wait()##使用方法待研究
        versionString = versionString.decode('gbk')
        versionString = re.split('\n', versionString)[0].strip('\r')
        s = '%s\n' % versionString
        txt.insert(END, s)


def getDevices():
    command_getVersion = 'adb devices'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)


def getApkPackageName():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        command = 'aapt d bading ' + filename + ' | grep package'
        returnStr = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
        returnStr = returnStr.decode('gbk')
    else:
        txt.insert(END, '未选择文件')


def listPackages():
    command_getVersion = 'adb shell pm list packages'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)


def listPackages3():
    command_getVersion = 'adb shell pm list packages -3'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)


def listPackagesSys():
    command_getVersion = 'adb shell pm list packages -s'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)


def localInstall():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        command = 'adb install ' + filename
        versionString = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT).stdout.read()
        versionString = versionString.decode()
        txt.insert(END, '%s\n' % versionString)
    else:
        txt.insert(END, '未选择文件')


def getResolution():
    command_getVersion = 'adb shell  wm size'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)


def getPixelDensity():
    command_getVersion = 'adb shell wm density'
    versionString = subprocess.Popen(command_getVersion, shell=True, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT).stdout.read()
    versionString = versionString.decode()
    txt.insert(END, '%s\n' % versionString)


win = Tk()
win.geometry('620x360')
win.title('adb命令工具箱')

# 在窗体垂直自上而下位置50%处起，布局相对窗体高度50%高的文本框
txt = Text(win)
txt.place(rely=0.5, relheight=0.5)
if __name__ == '__main__':
    check_adb_devices_ini()
btn1 = Button(win, text='hu版本', command=getDevices_hu_Version)
btn1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)
btn2 = Button(win, text='5G版本', command=getDevices_5G_Version)
btn2.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)
btn3 = Button(win, text='获取设备', command=getDevices)
btn3.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
btn4 = Button(win, text='选择apk安装', command=localInstall)
btn4.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.1)
btn5 = Button(win, text='查看安装包名', command=listPackages)
btn5.place(relx=0.3, rely=0.1, relwidth=0.2, relheight=0.1)
btn6 = Button(win, text='查看第三方包名', command=listPackages3)
btn6.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.1)
btn7 = Button(win, text='查看车机系统包名', command=listPackagesSys)
btn7.place(relx=0.3, rely=0.3, relwidth=0.2, relheight=0.1)
# btn7 = Button(win, text='查看手机分辨率', command=getResolution)
# btn7.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.1)
# btn8 = Button(win, text='查看手机像素密度', command=getPixelDensity)
# btn8.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.1)
# btn9 = Button(win, text='查看手机', command=listPackages)
# btn9.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1)

win.mainloop()
