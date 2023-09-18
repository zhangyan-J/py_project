# 一期：通过读取excel文件中的每条用例的适用项目，检查是否每条用例都添加了语音Xpublic，语音Xmax，语音Xpro的precode，
# 二期：检查每个用例的precode是否precode添加正确，是否有缺少的precode

# 实现方式:
# 1. 遍历每行用例，先把precode一列的数据提取处理，转换成一个列表
# 2. 获取每条用例的适用项目，将使用项目生成一个列表，判断该用例的适用项目在此列表中属于哪个元素
# 3. if in xpublic 适用项目应该有语音Xpublic，if in x-public-max适用项目应该有语音Xmax，if inx-public-pro，应有语音Xpro

# import os
import pandas as pd

# a = os.getcwd()
# print(a)

file_path = r'D:\Practice\github\py_project\check_precode\用例列表.xlsx'
# def read_excel(file_path):
df = pd.read_excel(file_path,sheet_name='项目用例')
# print(df.head())
#读取指定的列
column_name1 = '*适用项目'
cloumn_name2 = 'precode'
#逐个取出指定列中的值
# for value in df[column_name]:
#     print(value)

#把读取到的指定列的数据生成一个list
project_list = df[column_name1].tolist()
precode_list = df[cloumn_name2].tolist()
print(project_list)
print(precode_list)
    # return project_list
    # return precode_list
for sublist in precode_list:
    for item in sublist:
        # print( f"Found {sublist} in the precode_list list!" )
        print(item)






# read_excel(file_path)

