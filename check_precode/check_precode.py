# 一期：通过读取excel文件中的每条用例的适用项目，检查是否每条用例都添加了语音Xpublic，语音Xmax，语音Xpro的precode，
# 二期：检查每个用例的precode是否precode添加正确，是否有缺少的precode
# 实现方式:
# 1. 遍历每行用例，先把precode一列的数据提取处理，转换成一个列表
# 2. 获取每条用例的适用项目，将使用项目生成一个列表，判断该用例的适用项目在此列表中属于哪个元素
# 3. if in xpublic 适用项目应该有语音Xpublic，if in x-public-max适用项目应该有语音Xmax，if inx-public-pro，应有语音Xpro
# # import os
# import pandas as pd
#
# # a = os.getcwd()
# # print(a)
#
# file_path = r'D:\Practice\github\py_project\check_precode\用例列表.xlsx'
# class check:
#     def __init__(self,project_list,precode_list):
#         self.projec
#
# def read_excel(file_path):
#     df = pd.read_excel(file_path,sheet_name='项目用例')
#     # print(df.head())
#     #读取指定的列
#     column_name1 = '*适用项目'
#     cloumn_name2 = 'precode'
#     #逐个取出指定列中的值
#     # for value in df[column_name]:
#     #     print(value)
#
#     #把读取到的指定列的数据生成一个list
#     project_list = df[column_name1].tolist()
#     precode_list = df[cloumn_name2].tolist()
#     print(project_list)
#     print(precode_list)
#     # return project_list
#     # return precode_list
#     for sublist in precode_list:
#         if 'X-Public' == 'X-Public':
#             print('-----------''X-Public' in sublist )
#     #     for item in sublist:
            # print( f"Found {sublist} in the precode_list list!" )
            # print(item)
# read_excel(file_path)
import pandas as pd
class ExcelProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
    def check_rows(self, sheet_name, condition_column,
                   condition_value,
                   condition_value2,
                   condition_value3,
                   target_column,
                   target_field,
                   target_field2,
                   target_field3):
        df = pd.read_excel( self.file_path, sheet_name=sheet_name )
        for index, row in df.iterrows():
            condition = row[condition_column]#遍历列名为“condition”的每行数据
            # print(condition)
            target = row[target_column]#遍历列名为“target”的每行数据
            # print(target,index)
            #
            if condition == condition_value and target_field in str( target ):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column contains '{target_field}'." )
            elif condition != condition_value and target_field in str(target):
            #     print(condition_value+'------------')
            #     print(condition+'=============')
            #     print(target_field+'33333333333')
            #     print(target+'444444444444')
            #     print(index)
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field}', the precode is {target}")
            elif condition == condition_value and target_field not in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field}', the precode is {target}")




            elif condition == condition_value and target_field2 not in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field2}', the precode is {target}")
            elif condition == condition_value and target_field3 not in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field3}', the precode is {target}")
            elif condition != condition_value and target_field2 in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field2}', the precode is {target}")
            elif condition != condition_value and target_field3 in str(target):
                print(
                    f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field3}', the precode is {target}")






            if condition == condition_value2 and target_field2 in str( target ):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column contains '{target_field2}'." )
            elif condition != condition_value2 and target_field2 in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field2}', the precode is {target}")
            elif condition == condition_value2 and target_field2 not in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field2}', the precode is {target}")

            if condition == condition_value3 and target_field3 in str( target ):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column contains '{target_field3}'." )
            elif condition != condition_value3 and target_field3 in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field3}', the precode is {target}")
            elif condition == condition_value3 and target_field3 not in str(target):
                print(f"Condition '{condition}' met in row {index}, and {target_column} column does't contains '{target_field3}', the precode is {target}")
    print( "All rows checked." )
# 创建 ExcelProcessor 类的实例
processor = ExcelProcessor( './check_precode\用例列表.xlsx' )
# 检查 "Sheet1" 中 "Condition" 列是否为 True，同时检查 "Target" 列是否包含 "Content"
# processor.check_rows( "项目用例", "*适用项目", 'X-Public', "precode", "语音Xpublic" )
processor.check_rows( "项目用例", "*适用项目",condition_value='X-Public', condition_value2='X-Public-Max',condition_value3='X-Public-Pro', target_column="precode", target_field="语音Xpublic",target_field2="语音Xmax",target_field3='语音Xpro' )