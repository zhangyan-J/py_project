# -*- coding: utf-8 -*-
import keyword
# 查找关键字
# find_keyword_in_cell(df, keyword)
# Time:2022 2024/4/20 23:01
# Author: ZhangYan

import logging

import time
import os

import pandas as pd

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(root_dir, "logs")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

#第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)#log等级总开关

#第二步，创建一个handler，用于写入日志文件
logfile = '%s/autotest.log' % log_dir
fh = logging.FileHandler(logfile,mode='a')
fh.setLevel(logging.DEBUG) #输出到file的log等级的开关

#第三步，在创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)#输出到console的log等级开关

#第四步，定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)


# logging.basicConfig(level=logging.DEBUG,
#                     filename=r"D:\project\py_project\check_words/logs/autotest.log",
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 开始使用log功能
logger.info('这是logging info message')
logger.debug('这是 logging debug message')
logger.warning('这是 logging a warning message')
logger.error('这是 logging an error message')
logger.critical('这是 logging critical message')

#
# def log():
#     # 创建一个日志器
#     logger = logging.getLogger("logger")
#
#     # 设置日志输出的最低等级,低于当前等级则会被忽略
#     logger.setLevel(logging.INFO)
#
#     # 创建处理器：sh为控制台处理器，fh为文件处理器
#     sh = logging.StreamHandler()
#
#     # 创建处理器：sh为控制台处理器，fh为文件处理器,log_file为日志存放的文件夹
#     # log_file = os.path.join(log_dir,"{}_log".format(time.strftime("%Y/%m/%d",time.localtime())))
#     log_file = os.path.join(log_dir, "autotest.log")
#     fh = logging.FileHandler(log_file, encoding="UTF-8")
#
#     # 创建格式器,并将sh，fh设置对应的格式
#     formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
#                                  datefmt="%Y/%m/%d %X")
#     sh.setFormatter(formator)
#     fh.setFormatter(formator)
#
#     # 将处理器，添加至日志器中
#     logger.addHandler(sh)
#     logger.addHandler(fh)
#
#     return logger
#
#
# class DemoLogger:
#     pass
#
#
# if __name__ == '__main__':
#     file_time = '_{}/'.format(time.strftime('%Y%m%d_%H%M%S', time.localtime()))
#     # 读取文件
#     file_path = input(r"请输入文件路径：")
#     try:
#         df = pd.read_excel(file_path)
#     except:
#         print("文件读取失败", file_path)
#
#     excel_file = pd.ExcelFile(file_path)
#     sheet_names = excel_file.sheet_names
#
#     for sheet_name in sheet_names:
#         keyword = input(f"请输入待查找的关键字：")
#         df = pd.read_excel(file_path, sheet_name=sheet_name)
#         # print(df)
#         all_sheets = pd.read_excel(file_path, sheet_name=None)
#         # print(all_sheets)
#         for sheet_name, sheet_data in all_sheets.items():
#             # print(f'sheet name: {sheet_name}')
#             # print(sheet_data)
#             # print('\n')
#             for index, row in sheet_data.iterrows():
#                 # print(index)
#                 for col_index, column_value in row.items():
#                     # print(col_index)
#                     # print(type(column_value))
#                     if str(keyword) in str(column_value):
#                         print(f"找到关键字 '{keyword}' 在第 {index+ 2} 行 {col_index} 列")
#
# ##读取excel每个sheet和每个sheet的每个单元格
# ##打印log
