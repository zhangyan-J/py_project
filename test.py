# # print("hello world")
# # polling_active = True
# # while polling_active:
# #     num_1 = int(input("请输入一个数字："))
# #     if num_1 == 'q':
# #         break
# #     num_2 = int(input("请输入第二个数字："))
# #     if num_2 == "q":
# #         break
# #     n_sum = num_1+num_2
# #     print(n_sum)
# #     repeat = input("还想继续输入吗?(yes/no)")
# #     if repeat == "no":
# #         break
# # import matplotlib
# #
# # matplotlib.use('TkAgg')
# # import numpy as np
# # import math
# # import matplotlib.pyplot as plt
#
# # squares = [1,4,9,16,25]
# #
# # plt.plot(squares,linewidth = 5)
# # plt.show()
# # ##设置图表标题，并给坐标轴加上标签
# # plt.title("Square Numbers",fontsize = 24)
# # plt.xlabel("Value",fontsize = 14)
# # plt.ylabel("Square of Value",fontsize = 14)
# #
# # ##设置刻度标记的大小
# # plt.tick_params(axis='both',lablesize = 14)
# # plt.show()
#
# # plt.scatter(2,4,s=200)
# # plt.show()
# # ##设置图标标题并且给左边加上标签
# # plt.title("Square Numbers",fontsize=24)
# # plt.xlabel("Value",fontsize=14)
# # plt.ylabel("Square of Value",fontsize=14)
# #
# # ##设置刻度标记先的大小
# # plt.tick_params(axis='both',which='major',lablesize=14)
# # plt.show()
#
# ## 15.2.4使用scatter()绘制一系列点
#
# # import matplotlib
# # matplotlib.use('TkAgg')
# # import numpy as np
# # import math
# # import matplotlib.pyplot as plt
# #
# # x_values= [1,2,3,4,5]
# # y_values= [1,4,9,16,25]
# #
# # plt.scatter(x_values,y_values,s=100)
# # ##设置图标标题并给坐标轴指定标签
# # plt.title("Square Numbers",fontsize=24)
# # plt.xlabel("Value",fontsize=14)
# # plt.ylabel("Square of Value",fontsize=14)
# # plt.show()
#
# # 15.2.5自动计算数据
# # import matplotlib
# # matplotlib.use('TkAgg')
# # import matplotlib.pyplot as plt
# # x_values= list(range(1,1001))
# # y_values= [x ** 2 for x in x_values]
# #
# # plt.scatter(x_values,y_values,s=40)
# # # ##设置图标标题并给坐标轴指定标签
# # plt.title("Square Numbers",fontsize=12)
# # plt.xlabel("Value",fontsize=12)
# # plt.ylabel("Square of Value",fontsize=12)
# #
# #
# # ##设置每个坐标轴的取值范围
# # plt.axis([0,1100,0,1100000])
# # plt.show()
#
# ## 15.2.6删除数据点的轮廓
# # import matplotlib
# # matplotlib.use('TkAgg')
# # import matplotlib.pyplot as plt
# # x_values= list(range(1,1001))
# # y_values= [x ** 2 for x in x_values]
# #
# # plt.scatter(x_values,y_values,s=40,edgecolors='none',linewidths=5)
# # # ##设置图标标题并给坐标轴指定标签
# # plt.title("Square Numbers",fontsize=12)
# # plt.xlabel("Value",fontsize=12)
# # plt.ylabel("Square of Value",fontsize=12)
# #
# #
# # ##设置每个坐标轴的取值范围
# # plt.axis([0,1100,0,1100000])
# # plt.show()
#
#
# # 导入pandas库
# # import pandas as pd
# # #生成一个Series
# # s=pd.Series([1,3,3,4], index=list('ABCD'))
# #
# # #括号内不指定图表类型，则默认生成直线图
# # s.plot()
# #
# # #条形图
# # # s.plot(kind='bar')
# #
# # #水平条形图
# # s.plot.barh()
#
# ##习题15.1数字的三次方，显示前5000个整数的立方值
# # import matplotlib
# # matplotlib.use('TkAgg')
# # import matplotlib.pyplot as plt
# #
# # x_values = list(range(1,5001))
# # y_values = [x ** 3 for x in x_values]
# #
# # plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
# # plt.show()
#
# # import csv
# # from datetime import datetime
# # first_data = datetime.strptime("2018-07-01","%Y-%m-%d")
# #
# # print(first_data)
# # filename = 'D:\project\py_project\data.csv' ##将要使用的文件名赋值给filename
# #
# # with open(filename) as fin:
# #     reader = csv.reader(fin)
# #     header_row = next(reader)
# #     # print(header_row)
# #
# #     # for index,column_header in enumerate(header_row):
# #     #     print(index,column_header)
# #     #从文件中获取最高温度
# #     dates,highs = [],[]
# #     for row in reader:
# #         current_date = datetime.strptime(row[2],"%Y-%M-%d")
# #         dates.append(current_date)
# #         print(dates.append(current_date))
# #         high = int(row[2])
# #         highs.append(high)
# #         print(highs.append(high))
# # # print(highs)
# # plt.style.use('seaborn')
# # fig ,ax = plt.subplots()
# # ax.plot(dates,highs,c='red')
# #
# # ##设置图形格式
# # ax.set_title("Daily high temperatures - 2018",fontsize=24)
# # ax.set_xlabel('',fontsize=16)
# # fig.autofmt_xdate()
# # ax.set_y_label("Tempeature(F)",fontsize=16)
# # ax.tick_params(axis='both',which='major',labelsize=16)
# #
# # # plt.show()
#
# # import csv  # 导入csv模块
# # import matplotlib.pyplot as plt
# # import matplotlib
# # matplotlib.use('TkAgg')
# # import matplotlib.pyplot as plt
# # from datetime import datetime
# # filename = 'D:\project\py_project\data.csv'  # 将要使用的文件名赋值给filename
# #
# # with open(filename) as f:  # 打开文件，并将返回的文件对象赋值给f
# #     reader = csv.reader(f)  # 调用csv.read()创建一个与文件对象f相关联的阅读器对象，并赋值给reader
# #     header_row = next(reader)  # next()返回文件的下一行，将该行赋值给header_row
# #
# #     # 从文件中获取最高温度
# #     dates, highs = [], []  # 创建空列表
# #     for row in reader:  # 遍历文件中余下各行
# #         try:
# #             current_date = datetime.strptime(row[2], '%Y-%m-%d')  # 将包含日期信息的数据row[2]转化为datetime对象
# #             dates.append(current_date)  # 附加到列表dates末尾
# #             high = int(row[5])
# #             highs.append(high)
# #         except:
# #             print("运行失败")
# #
# # # 绘制最高温度
# # plt.style.use('seaborn')
# # fig, ax = plt.subplots()
# # ax.plot(dates, highs, c='red')
# #
# # # 设置图形格式
# # ax.set_title("Daily high temperatures - 2018", fontsize=24)
# # ax.set_xlabel('', fontsize=16)
# # fig.autofmt_xdate()  # 绘制倾斜的日期，以免重叠
# # ax.set_ylabel("Temperature (F)", fontsize=16)
# # ax.tick_params(axis='both', which='major', labelsize=16)
# #
# # # plt.show()
#
# # import pyttsx3
# #
# # def text_to_speech(text):
# #     # 创建一个语音引擎
# #     engine = pyttsx3.init()
# #     # 将文本转换为语音
# #     engine.say(text)
# #     # 播放语音
# #     engine.runAndWait()
# #
# # # 调用函数进行文字转语音
# # text_to_speech("你好，我是文心一言，很高兴为您服务！")
#
# # #导入selenium模块
# # from selenium import webdriver
# #
# # from time import sleep
# # from selenium.webdriver.common.by import By
# #
# # #启动浏览器驱动
# # driver = webdriver.Chrome()
# #
# # #访问url
# # driver.get('https://www.baidu.com')
# #
# # #定位元素
# # el = driver.find_element(By.ID,'kw')
# #
# # #执行自动化操作
# # el.send_keys('NBA头条')
# # bt = driver.find_element(By.ID,'su').click()
# #
# # #休眠5秒
# # sleep(5)
# #
# # #关闭浏览器并且释放进程资源
# # driver.quit()
# import pyecharts
# # print(pyecharts.__version__)
# from pyecharts.charts import Bar
#
# # bar = Bar()
# # bar.add_xaxis(["衬衫","羊毛衫",'雪纺裤','裤子','高跟鞋','袜子'])
# # bar.add_yaxis("商家A",[5,20,36,10,75,90])
# # # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # # 也可以传入路径参数，如 bar.render("mycharts.html")
# # bar.render('mycharts.html')
# 遍历路径下所有文件夹下的xml文件
# 替换指定内容为新内容，并且生成同样目录结果的新文件夹

# file = 'D:\\tag_rear_8155\list.txt'
# search_term = "语音"
# with open(file,'r',encoding='utf-8') as f,open('output.txt', 'w') as file_out:
#     for line in f:
#         # print(line)
#         if search_term in line:
#             print(line.strip(),end=''+'\r\n')
#             file_out.write(line)
#             # f.write(line.strip()+'\n')
import os
import xml.etree.ElementTree as ET


def replace_xml_values(xml_dir, old_value, new_value):
    """
    批量替换XML文件中特定值
    :param xml_dir: XML文件所在目录
    :param old_value: 旧值
    :param new_value: 新值
    """
    for xml_file in os.listdir(xml_dir):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(xml_dir, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            for elem in root.iter():
                if elem.text == old_value:
                    elem.text = new_value
                for attr_name in elem.attrib:
                    if elem.attrib[attr_name] == old_value:
                        elem.attrib[attr_name] = new_value
            tree.write(xml_path, encoding='utf-8', xml_declaration=True)


# 使用示例
replace_xml_values('D:\\test_resource\script_helper\case_list\Project\platform_X\X-Public-Max\Scripts\Function_Script\语音\网易云音乐', 'old_code_segment', 'new_code_segment')