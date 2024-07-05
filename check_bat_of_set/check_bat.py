# -*- coding: utf-8 -*-
import os
from openpyxl import Workbook



def get_bat_files(folder_path):
    bat_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.bat'):
                bat_files.append(os.path.join(root, file))
    return bat_files


def read_bat_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def write_to_excel(bat_files, excel_path):
    wb = Workbook()
    ws = wb.active
    ws.append(['Bat文件名称', 'Bat文件内容'])

    for file in bat_files:
        name = os.path.basename(file)
        content = read_bat_file(file)
        ws.append([name, content])

    wb.save(excel_path)


folder_path = r'D:\practice\other_py_file\check_bat_of_set\bat_set'  # 请将此路径替换为包含.bat文件的文件夹路径
excel_path = r'D:\practice\other_py_file\check_bat_of_set/file.xlsx'  # 请将此路径替换为要保存Excel文件的路径
# if not os.path.exists(excel_path):
#     os.makedirs(os.path.dirname(excel_path))
#     print('文件夹不存在，已创建')
bat_files = get_bat_files(folder_path)
write_to_excel(bat_files, excel_path)
