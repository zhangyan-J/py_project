import pandas as pd

# 读取Excel文件
file_path = r"D:\project\py_project\豆瓣电影Top250.xls"  # 替换为你的Excel文件路径
if file_path.endswith('.xls'):
    engine = 'xlrd'

elif file_path.endswith('.xlsx'):
    engine = 'openpyxl'

else:
    raise ValueError("Unsupported file format")

df = pd.read_excel(file_path, engine=engine)

# 输入关键字
keyword = input("请输入关键字：")
# 遍历DataFrame中的每个单元格
for index, row in df.iterrows():
    for col_index, column_value in row.items():
        if keyword in str(column_value):
            print(f"找到关键字 '{keyword}' 在第 {index + 1} 行 {col_index} 列")

# 查找关键字
# find_keyword_in_cell(df, keyword)
