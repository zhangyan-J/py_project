import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#读取excel
file_path = "/Users/zhangyan_laptop/python_project/py_project/check_words/豆瓣电影Top250.xls"
df = pd.read_excel(file_path)
# print(df)

#按照评分降序排序
sorted_df = df.sort_values(by='评分',ascending=False)

#选择评分前20的数据
top_20_df = sorted_df.head(5)

#设置支持中文的字体
font_path = fm.FontProperties(fname='/System/Library/Fonts/STHeiti Medium.ttc')
plt.rcParams['font.family'] = font_path.get_name()

#计算
# df['平均分'] = df['评分'] / 100

#计算自动化率
# total_automation_rate = df['平均分'].mean()
# print(f"平均分:{total_automation_rate * 100:.2f}%")

#将总自动化率添加到DataFrame最后一行
# total_row = pd.DataFrame(
#     {'影片中文名':'影片中文名',
#      '评分':df['评分'].sum(),
#      '平均分':total_automation_rate},
#      index=[len(df)]
# )
# df = pd.concat([df,total_row])


#保存修改后的DataFrame 到新的Excel 文件
# output_file_path = 'out.xlsx'
# df.to_excel(output_file_path,index=False)

#生成柱状图
plt.figure(figsize=(10,6))
bars = plt.bar(top_20_df['影片中文名'], top_20_df['评分'])
plt.xlabel('影片中文名')
plt.ylabel('评分')
plt.title('评分前 20 的用例编码柱状图')
plt.xticks(rotation=45,fontproperties=font_path)

#在柱状图上显示具体数量
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height,f'{height}',ha='center',va='bottom')

plt.tight_layout()
plt.show()