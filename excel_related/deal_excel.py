# import pandas as pd
#
# def count_rows_with_test_method(file_path):
#     # 读取 Excel 文件
#     excel_file = pd.ExcelFile(file_path)
#
#     # 获取所有表名
#     sheet_names = excel_file.sheet_names
#
#     # 遍历每个工作表
#     for sheet_name in sheet_names:
#         # 读取当前工作表的数据
#         df = excel_file.parse(sheet_name)
#
#         # 筛选第二列值为“测试方法”的行
#         filtered_df = df[df.iloc[:, 1] == '测试方法']
#
#         # 统计筛选后的数据行数
#         row_count = len(filtered_df)
#
#         print(f"工作表 '{sheet_name}' 中第二列是 '测试方法' 的行数为: {row_count}")
#
# # 使用示例
# file_path = '5.0适配func.xlsx'  # 替换为实际的 Excel 文件路径
# count_rows_with_test_method(file_path)
# # 输出结果
#
import pandas as pd

def count_rows_with_test_method(file_path):
    # 用于累加所有工作表中符合条件的总行数
    total_row_count = 0

    # 读取 Excel 文件
    excel_file = pd.ExcelFile(file_path)

    # 获取所有表名
    sheet_names = excel_file.sheet_names

    # 遍历每个工作表
    for sheet_name in sheet_names:
        # 读取当前工作表的数据
        df = excel_file.parse(sheet_name)

        # 筛选第二列值为“测试方法”的行
        filtered_df = df[df.iloc[:, 1] == '测试方法']

        # 统计筛选后的数据行数
        row_count = len(filtered_df)
        total_row_count += row_count

        print(f"工作表 '{sheet_name}' 中第二列是 '测试方法' 的行数为: {row_count}")

    # 输出所有工作表的总行数
    print(f"所有工作表中第二列是 '测试方法' 的总行数为: {total_row_count}")

# 使用示例
file_path = '5.0适配func.xlsx'  # 替换为实际的 Excel 文件路径
count_rows_with_test_method(file_path)