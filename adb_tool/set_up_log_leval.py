# # -*- coding: utf-8 -*-
# import os
# import threading
# import windnd
# import tkinter as tk
# from tkinter import *  # 导入 Tkinter 库
#
#
# class APKInstaller:
#
#     def install_apk(self, device_name, apk_name):
#         # 安装apk
#         os.system("adb -s " + device_name + " install -r " + os.path.join(apk_name))
#
#     def get_device_list(self):
#         os.system("adb devices")
#         res = os.popen("adb devices").readlines()
#         device_list = [sub.split('\t')[0] for sub in res[1:-1]]
#         return device_list
#
#
# # 此类用来制作界面
# class APKTk():
#
#     def dragged_files(self, files):
#         msg = '\n'.join((item.decode('gbk') for item in files))
#         print(msg)
#         self.apk_name.set(msg)
#
#     def __init__(self, APKInstaller):
#         self.root = Tk()
#         self.root.geometry('540x170')
#         self.root.title("Execute_adb_command")
#         self.apk_name = StringVar()
#         self.apkInstaller = APKInstaller
#         self.select_device_list = []
#         self.device_list = self.apkInstaller.get_device_list()
#         self.cb_list = []
#         windnd.hook_dropfiles(self.root, self.dragged_files)
#
#     def mul_check_box(self):
#         for index, item in enumerate(self.device_list):
#             self.select_device_list.append(tk.StringVar())
#             cb = Checkbutton(self.root, text=item, variable=self.select_device_list[-1], onvalue=item, offvalue='')
#             self.cb_list.append(cb)
#             cb.grid(row=index, column=0, sticky='w')
#             cb.select()
#
#     # 刷新设备列表
#     def refresh_data(self):
#         print("refresh")
#         for item in self.cb_list:
#             item.grid_remove()
#         self.cb_list = []
#         self.device_list = self.apkInstaller.get_device_list()
#         self.select_device_list = []
#         self.mul_check_box()
#         print("\n")
#
#     # 全选设备列表
#     def select_all(self):
#         for index, item in enumerate(self.device_list):
#             self.device_list[index].set(item)
#
#     # 安装按钮
#     def install_button(self):
#         button_install = Button(self.root, text="安装", command=self.install)
#         button_install.grid(row=len(self.device_list) + 1, column=1)
#
#     # 刷新设备列表按钮
#     def refresh_button(self):
#         button_install = Button(self.root, text="刷新", command=self.refresh_data)
#         button_install.grid(row=len(self.device_list) + 1, column=2)
#
#     def input_text(self):
#         entry_log = Entry(self.root, width=60, textvariable=self.apk_name)
#         entry_log.grid(row=len(self.device_list) + 1, column=0, sticky='w')
#
#     def get_apk_name(self):
#         return self.apk_name.get()
#
#     def mainloop(self):
#         self.root.mainloop()
#
#     def install(self):
#         selected_device_list = [i.get() for i in self.select_device_list if i.get()]
#         print(selected_device_list)
#         apkName = self.get_apk_name()
#         print(apkName)
#
#         for device in selected_device_list:
#             threading.Thread(target=self.apkInstaller.install_apk, args=(device, apkName)).start()
#             print("启动" + device)
#
#
# if __name__ == '__main__':
#     apkInstaller = APKInstaller()
#     apkTk = APKTk(apkInstaller)
#     apkTk.mul_check_box()
#     apkTk.input_text()
#     apkTk.install_button()
#     apkTk.refresh_button()
#     apkTk.root.mainloop()




# -*- coding: utf-8 -*-

"""

__author__:  @xxx

__datetime__:  xxx

"""

import json

import os

from time import sleep

# 生成导出任务配置

import click

import pandas as pd

import requests
import self as self
from resume.resume import content

# 导出表格地址

EXPORT_OFFICE_URL= "https://doc.weixin.qq.com/v1/export/export_office"

# 查询导出任务配置

QUERY_PROGRESS_URL= "https://doc.weixin.qq.com/v1/export/query_progress"

# 腾讯文档地址

project_excel_url= "https://doc.weixin.qq.com/sheet/xxx"

project_excel_name= "xxx表"

class ProjectRemindRobot:

    """导出腾讯文档到本地"""

    def __init__(self,

uid: str,

uid_key: str,

doc_id: str,

file_name: str,

wedrive_ticket: str,

wedrive_skey: str,

wedrive_sid: str

                ):

        self.uid= uid

        self.uid_key= uid_key

        self.doc_id= doc_id

        self.file_name= file_name

        self.wedrive_ticket= wedrive_ticket

        self.wedrive_skey= wedrive_skey

        self.wedrive_sid= wedrive_sid

        # uid doc_id wedrive_skey wedrive_sid通常不变

    def create_export_office_task(self):

        """

        创建导出文件任务"""

        # 组织请求cookie并赋为全局变量方便后面接口使用

        global cookie_value

        cookie_value= 'uid=%s; uid_key=%s; wedrive_ticket=%s; wedrive_skey=%s; wedrive_sid=%s;' % (

        self.uid,self.uid_key,self.wedrive_ticket,self.wedrive_skey,self.wedrive_sid)

        doc_id_value= '%s' % self.doc_id

        headers= {'content-type': 'application/x-www-form-urlencoded','Cookie': cookie_value}

# 请求体

        body= {'docId': doc_id_value,'version': '2'}

#调用request发送post请求

        response_body= requests.post(url=EXPORT_OFFICE_URL,headers=headers,data=body)
        return response_body

        print("添加导出任务返回内容为：", response_body.text)

    def main(self):
        pass


def query_progress_task(self,operation_id):

        """

        查询导出文件任务进度"""

        # 组织请求cookie

        headers= {'content-type': 'application/x-www-form-urlencoded','Cookie': cookie_value}

# 请求体

        body= {'operationId': operation_id}

#调用request发送get请求

        response_body= requests.get(url=QUERY_PROGRESS_URL,headers=headers,params=body)

        print("查询进度内容为：", response_body.text)

        return response_body

def down_file(self,file_url):

        """

        下载文件"""

        headers= {'Cookie': cookie_value}

        response_body= requests.get(url=file_url,headers=headers)
        
        print("查询进度内容为：", response_body)
        
        return response_body

def read_data(self):

        io= r'C:\Users\user\PycharmProjects\xxx\test.xlsx'

        # 读取表格，只读取sheet_name为xx，以第二行为表头，只读取指定行

        data= pd.read_excel(io,sheet_name='xxx',header=1,usecols=[0,1,2,5,6,7,8])

        return data

def main(self):

        """

        程序入口"""

        # 1、创建任务

        resp_create_export_office= self.create_export_office_task()

        print("添加导出任务返回内容为：%s" % resp_create_export_office.text)
        
        operation_id= resp_create_export_office.json()["operationId"]
        
        print("创建任务成功：%s" % operation_id)

# 2、轮询任务，直到 100% 停止

        while True:

            resp_query_progress= self.query_progress_task(operation_id)

            progress= resp_query_progress.json()["progress"]
            
            print("|" + "#" * progress+ "| " + "%s/100" % progress)
            
            if progress>= 100:
            
                            file_url= resp_query_progress.json()["file_url"]
            
            print("导出任务完成：%s" % resp_query_progress)
            
            break
            
            sleep(1)

# 3、下载文件

        print("开始下载文件。。。")

        content= self.down_file(file_url)
        
        print(type(content))

        file_name= "test.xlsx"
        
                # 若存在则先删除文件
        
        if os.path.exists(file_name):
    
            os.remove(file_name)

# 写入文件

        with open(file_name,"wb")as code:

            code.write(content.content)

            print("下载完成。")
            
            # 读取文件
            
            self.read_data()

if __name__== '__main__':

    # 只需要定时替换uid_key wedrive_ticket

    prr= ProjectRemindRobot(

    uid="xxx",
    
    doc_id="xx",
    
    file_name="export_file.xlsx",
    
    wedrive_skey="xx",
    
    wedrive_sid="xx",
    
    uid_key="xxx",
    
    wedrive_ticket="xxx",
    
    )
    
    prr.main()
