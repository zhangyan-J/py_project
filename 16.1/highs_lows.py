import csv
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
#从文件中获取最高气温

filename = 'D:\project\py_project\data.csv'  # 将要使用的文件名赋值给filename

with open(filename) as f:  # 打开文件，并将返回的文件对象赋值给f
    reader = csv.reader(f)  # 调用csv.read()创建一个与文件对象f相关联的阅读器对象，并赋值给reader
    header_row = next(reader)  # next()返回文件的下一行，将该行赋值给header_row

    # 从文件中获取最高温度
    dates,highs = [],[] # 创建空列表
    for row in reader:  # 遍历文件中余下各行
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
#设置图形的格式
plt.title("Daily high temperatures,July 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',lablesize=16)

plt.show()