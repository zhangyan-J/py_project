# import pandas as pd
#
#
# # 读取Excel文件
# # file_path = r"D:\zhangyan7\Downloads\P0P1P1常态化自动化用例.xlsx"  # 替换为你的Excel文件路径
# file_path = input("请输入文件路径：")
# if file_path.endswith('.xls'):
#     engine = 'xlrd'
#
# elif file_path.endswith('.xlsx'):
#     engine = 'openpyxl'
#
# else:
#     raise ValueError("Unsupported file format")
#
# df = pd.read_excel(file_path, engine=engine)
#
# # 输入关键字
# keyword = input("请输入关键字：")
# # 遍历DataFrame中的每个单元格
# for index, row in df.iterrows():
#     # print(f"正在检查第 {index} 行")
#     for col_index, column_value in row.items():
#         if keyword in str(column_value):
#             # print(index)
#             print(f"找到关键字 '{keyword}' 在第 {index+ 2} 行 {col_index} 列")

# 查找关键字
# find_keyword_in_cell(df, keyword)
# Time:2022 2022/3/2 10:21
# Author: Jasmay
# -*- coding: utf-8 -*-
import logging

import time
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(root_dir, "logs")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)


class DemoLogger():
    def log(self):

        # 创建一个日志器
        logger = logging.getLogger("logger")

        # 设置日志输出的最低等级,低于当前等级则会被忽略
        logger.setLevel(logging.INFO)

        # 创建处理器：sh为控制台处理器，fh为文件处理器
        sh = logging.StreamHandler()

        # 创建处理器：sh为控制台处理器，fh为文件处理器,log_file为日志存放的文件夹
        # log_file = os.path.join(log_dir,"{}_log".format(time.strftime("%Y/%m/%d",time.localtime())))
        log_file = os.path.join(log_dir, "autotest.log")
        fh = logging.FileHandler(log_file, encoding="UTF-8")

        # 创建格式器,并将sh，fh设置对应的格式
        formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                     datefmt="%Y/%m/%d %X")
        sh.setFormatter(formator)
        fh.setFormatter(formator)

        # 将处理器，添加至日志器中
        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger

    def sum(self, a, b):
        try:
            sum = a + b
            self.log().info("{}+{}={}加法运算正确".format(a, b, sum))
            return sum
        except Exception as error:
            self.log().error("{}+{}加法运算计算错误".format(a, b, error))


result = DemoLogger().sum(2, "a")
result1 = DemoLogger().sum(2, 3)
result2 = DemoLogger().sum(2, 8)

if __name__ == '__main__':
    print(result)
    print(result1)
    print(result2)

