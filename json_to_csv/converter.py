import json
import os
import sys
import pandas as pd
import csv
# if __name__=='__main__':
#     try:
#         with open('D:\project\py_project\json_to_csv\input.json','r') as f:
#             data = json.loads(f.read())
#
#         output = ','.join([*data[0]])
#         for obj in data:
#             output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
#
#         with open('D:\project\py_project\json_to_csv\output.csv','w') as f:
#             f.write(output)
#     except Exception as ex:
#         print(f'Error:{str(ex)}')
# try:
def read_json_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        data = json.load(f)
    return data
# 获取文件名列表
def list_file_names(dictionary):
    exist_files = os.listdir(dictionary)
    # print(exist_files)
    file_list = []
    for f in exist_files:
        file_list.append(os.path.join(dictionary,f))
    # print(file_list)
    return file_list

# 将指定目录下的json文件合并成一个csv文件
# def merge_json_to_csv_file(folder,csv_file):
#     file_list = list_file_names(folder)
#     pdt = pd.DataFrame()
#     for file in file_list:
#         tb = pd.read_json(file)
#         print(tb)
#         pdt = pd.concat([pdt,tb],ignore_index=True)
#     print(pdt)
#     pdt.to_csv(csv_file,mode='a',encoding='utf-8_sig',header=1,index=0)

def write_to_csv(file_list,csv_file):
    with open(csv_file,'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        header_written = False
        for file in file_list:
            data = read_json_file(file)
            if data:
                if not header_written:
                    writer.writerow(data[0].keys())
                    header_written = True
                for item in data:
                    writer.writerow(item.values())

file_path = 'D:\project\py_project\json_to_csv'
out_csv = 'D:\project\py_project\json_to_csv\merge.csv'
json_files = list_file_names(file_path)

write_to_csv(json_files,out_csv)
# except Exception as ex:
#     print(f'Error:{str(ex)}')

# """
# # 减法计算器
# while True:
#     number1 = int(input("请告诉我两个数字，我来帮你计算差值\nnumber1:"))
#     number2 = int(input("number2:"))
#     results = []
#     gap = int(number2 - number1)
#     print(gap)
# """

