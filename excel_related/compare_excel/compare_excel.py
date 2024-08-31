# import pandas
#
#
# def compare_excel(file1, file2):
#     # 读取两个Excel文件
#     df1 = pandas.read_excel(file1)
#     df2 = pandas.read_excel(file2)
#
#     # 比较两个Excel文件中的数据
#     diff = pandas.concat([df1, df2]).drop_duplicates(keep=False)
#
#     # 输出结果
#     if diff.empty:
#         print("两个Excel文件中的数据完全相同")
#     else:
#         print("两个Excel文件中的数据有差异：")
#         # print(type(diff))
#         # print("差异数量：", len(diff))
#         #测试结果均为fail的行
#         diff_both = diff[(diff['测试结果'] == 'fail') & (diff['测试结果'] == 'fail')]
#
#         #file1测试结果fail的
#         # diff_1 = diff[diff['测试结果'] == 'fail']
#
#         #file2测试结果fail的
#         # diff_2 = diff[diff['测试结果'] == 'fail']
#
#         #将结果保存到新的Excel文件中
#         diff_both.to_excel("D:\practice\github\py_project\excel_related\compare_excel\compare_result.xlsx", index=False)
#         # diff_1.to_excel("D:\practice\github\py_project\excel_related\compare_excel\compare_result_1.xlsx", index=False)
#         # diff_2.to_excel("D:\practice\github\py_project\excel_related\compare_excel\compare_result_2.xlsx", index=False)
#
#
# # 示例用法
# compare_excel(
#     "D:\practice\github\py_project\excel_related\compare_excel\SS2.0_6.2.0_内测3-1_X03Pro_理想同学冒烟测试_0D11_RC3_0806_2024-08-06-19-29-18.xlsx",
#     "D:\practice\github\py_project\excel_related\compare_excel\SS3_6.2.0_内测3-1_W01Ultra&X01B_Ultra_0C20_BR10_RC3_理想同学冒烟测试_0806_2024-08-06-19-30-05.xlsx")
import pandas as pd



#读入文件
# data = pd.read_excel('D:\project\py_project\豆瓣电影Top250.xls')
data = pd.read_excel(r'D:\project\py_project\temp.xlsx')
# data['年国型'] = data['相关信息'].apply(lambda x:x.split('/')[-1].strip())
# data['链接值'] = data['电影详情链接'].apply(lambda x:x.split('.')[4])
# data['http'] = data['图片链接'].apply(lambda x:x.split('//')[1])
# print(data['年国型'] )
# writer = pd.ExcelWriter('temp2.xlsx')
# data.to_excel(writer,sheet_name='首版数据')
# writer.close()
data['year'] = data['年国型'].apply(lambda x:x.split('/')[0].strip())
data['c'] = data['年国型'].apply(lambda x:x.split('/')[1].strip())
data['type'] = data['年国型'].apply(lambda x:x.split('/')[-1].strip())
writer = pd.ExcelWriter('temp2.xlsx')

# print(data['year'])
# print(data[data['c']=='美国'])
# print(data['c'].unique())
# print(data['year'].unique())


# for i in data['year'].unique(): #获取一共有多少year
#     i = i.split('(')[0]
#     print(i)
#     data[data['year'] == i].to_excel(writer,sheet_name=i)
# writer.close()
# print(data[data['type'].str.contains('科幻')])

# type_list = set(z for i in data['type'] for z in i.split(' ')) #获取共有多少type并且给list去重
# 等同于：
# type_list = []
# for i in data['type']:
#     for z in i.split(' '):
#         type_list.append(z)
#
# print(set(type_list))
# for ty in type_list:
#     data[data['type'].str.contains(ty)].to_excel(writer,sheet_name=ty)
coun_list = set(z for i in data['c'] for z in i.split(' '))
print(coun_list)

for coun in coun_list:
    if coun:
        data[data['c'].str.contains(coun)].to_excel(writer,sheet_name=coun)
# writer = pd.ExcelWriter('temp.xlsx')
# data.to_excel(writer,sheet_name='原始数据',index=False)
writer.close()
print("...........拆分结束........")
