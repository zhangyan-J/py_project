import openpyxl
import pandas as pd
df = pd.read_excel(r'D:\zhangyan7\Downloads\P0P1P1常态化自动化用例.xlsx',sheet_name='脚本用例模版')
# keyword = input("请输入要搜索的关键字：")
keyword = '清洁模式'
# #遍历每一列
# for column in df.columns:
#     #遍历该列的每一个元素
#     for value in df[column]:
#         if keyword in str(value):
#             # print(f"找到关键字{keyword}在列{column}中'f'{value}'中找到。")
for index, row in df.iterrows():
    for column_value in row.values:
        if keyword in str(column_value):
            print(f"找到关键字：{keyword} 在第 {index+1} 行，第 {column_value} 列中")



# if __name__ == '__main__':
#     # 示例用法
#     file_path = r'D:\zhangyan7\Downloads\P0P1P1常态化自动化用例.xlsx'  # 替换为你的Excel文件路径
#     keyword = '清洁模式'