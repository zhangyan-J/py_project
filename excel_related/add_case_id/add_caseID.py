import pandas
import pandas as pd

##读取excel
file_path = r'D:\project\py_project\excel_related\add_case_id\豆瓣电影Top250.xlsx'
df = pd.read_excel(file_path)

#指定要检查的列
column_name = '影片外国名'
##检查指定列是否包含第X列的内容
def check_and_add(row):
    if not row[column_name].startswith(row['影片中文名']):
        row[column_name] = row['影片中文名'] + "_" + row[column_name].strip()
    return row
    # if not str(df[column_name][0]).startswith(df['影片中文名'][0]):
    #     df[column_name] = df[column_name].apply(lambda x: df['影片中文名'][0] + x)
df = df.apply(check_and_add,axis=1)
##保存修改后的excel
output_file_path = r'D:\project\py_project\excel_related\add_case_id\modified_豆瓣电影Top250_new.xlsx'
df.to_excel(output_file_path,index=False)