# print("hello world")
# polling_active = True
# while polling_active:
#     num_1 = int(input("请输入一个数字："))
#     if num_1 == 'q':
#         break
#     num_2 = int(input("请输入第二个数字："))
#     if num_2 == "q":
#         break
#     n_sum = num_1+num_2
#     print(n_sum)
#     repeat = input("还想继续输入吗?(yes/no)")
#     if repeat == "no":
#         break
# import matplotlib
#
# matplotlib.use('TkAgg')
import datetime
import keyword
import time

# import numpy as np
# import math
# import matplotlib.pyplot as plt

# squares = [1,4,9,16,25]
#
# plt.plot(squares,linewidth = 5)
# plt.show()
# ##设置图表标题，并给坐标轴加上标签
# plt.title("Square Numbers",fontsize = 24)
# plt.xlabel("Value",fontsize = 14)
# plt.ylabel("Square of Value",fontsize = 14)
#
# ##设置刻度标记的大小
# plt.tick_params(axis='both',lablesize = 14)
# plt.show()

# plt.scatter(2,4,s=200)
# plt.show()
# ##设置图标标题并且给左边加上标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
#
# ##设置刻度标记先的大小
# plt.tick_params(axis='both',which='major',lablesize=14)
# plt.show()

## 15.2.4使用scatter()绘制一系列点

# import matplotlib
# matplotlib.use('TkAgg')
# import numpy as np
# import math
# import matplotlib.pyplot as plt
#
# x_values= [1,2,3,4,5]
# y_values= [1,4,9,16,25]
#
# plt.scatter(x_values,y_values,s=100)
# ##设置图标标题并给坐标轴指定标签
# plt.title("Square Numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
# plt.show()

# 15.2.5自动计算数据
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# x_values= list(range(1,1001))
# y_values= [x ** 2 for x in x_values]
#
# plt.scatter(x_values,y_values,s=40)
# # ##设置图标标题并给坐标轴指定标签
# plt.title("Square Numbers",fontsize=12)
# plt.xlabel("Value",fontsize=12)
# plt.ylabel("Square of Value",fontsize=12)
#
#
# ##设置每个坐标轴的取值范围
# plt.axis([0,1100,0,1100000])
# plt.show()

## 15.2.6删除数据点的轮廓
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# x_values= list(range(1,1001))
# y_values= [x ** 2 for x in x_values]
#
# plt.scatter(x_values,y_values,s=40,edgecolors='none',linewidths=5)
# # ##设置图标标题并给坐标轴指定标签
# plt.title("Square Numbers",fontsize=12)
# plt.xlabel("Value",fontsize=12)
# plt.ylabel("Square of Value",fontsize=12)
#
#
# ##设置每个坐标轴的取值范围
# plt.axis([0,1100,0,1100000])
# plt.show()


# 导入pandas库
# import pandas as pd
# #生成一个Series
# s=pd.Series([1,3,3,4], index=list('ABCD'))
#
# #括号内不指定图表类型，则默认生成直线图
# s.plot()
#
# #条形图
# # s.plot(kind='bar')
#
# #水平条形图
# s.plot.barh()

##习题15.1数字的三次方，显示前5000个整数的立方值
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
#
# x_values = list(range(1,5001))
# y_values = [x ** 3 for x in x_values]
#
# plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
# plt.show()

# import csv
# from datetime import datetime
# first_data = datetime.strptime("2018-07-01","%Y-%m-%d")
#
# print(first_data)
# filename = 'D:\project\py_project\data.csv' ##将要使用的文件名赋值给filename
#
# with open(filename) as fin:
#     reader = csv.reader(fin)
#     header_row = next(reader)
#     # print(header_row)
#
#     # for index,column_header in enumerate(header_row):
#     #     print(index,column_header)
#     #从文件中获取最高温度
#     dates,highs = [],[]
#     for row in reader:
#         current_date = datetime.strptime(row[2],"%Y-%M-%d")
#         dates.append(current_date)
#         print(dates.append(current_date))
#         high = int(row[2])
#         highs.append(high)
#         print(highs.append(high))
# # print(highs)
# plt.style.use('seaborn')
# fig ,ax = plt.subplots()
# ax.plot(dates,highs,c='red')
#
# ##设置图形格式
# ax.set_title("Daily high temperatures - 2018",fontsize=24)
# ax.set_xlabel('',fontsize=16)
# fig.autofmt_xdate()
# ax.set_y_label("Tempeature(F)",fontsize=16)
# ax.tick_params(axis='both',which='major',labelsize=16)
#
# # plt.show()

# import csv  # 导入csv模块
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# from datetime import datetime
# filename = 'D:\project\py_project\data.csv'  # 将要使用的文件名赋值给filename
#
# with open(filename) as f:  # 打开文件，并将返回的文件对象赋值给f
#     reader = csv.reader(f)  # 调用csv.read()创建一个与文件对象f相关联的阅读器对象，并赋值给reader
#     header_row = next(reader)  # next()返回文件的下一行，将该行赋值给header_row
#
#     # 从文件中获取最高温度
#     dates, highs = [], []  # 创建空列表
#     for row in reader:  # 遍历文件中余下各行
#         try:
#             current_date = datetime.strptime(row[2], '%Y-%m-%d')  # 将包含日期信息的数据row[2]转化为datetime对象
#             dates.append(current_date)  # 附加到列表dates末尾
#             high = int(row[5])
#             highs.append(high)
#         except:
#             print("运行失败")
#
# # 绘制最高温度
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red')
#
# # 设置图形格式
# ax.set_title("Daily high temperatures - 2018", fontsize=24)
# ax.set_xlabel('', fontsize=16)
# fig.autofmt_xdate()  # 绘制倾斜的日期，以免重叠
# ax.set_ylabel("Temperature (F)", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)
#
# # plt.show()

# import pyttsx3
#
# def text_to_speech(text):
#     # 创建一个语音引擎
#     engine = pyttsx3.init()
#     # 将文本转换为语音
#     engine.say(text)
#     # 播放语音
#     engine.runAndWait()
#
# # 调用函数进行文字转语音
# text_to_speech("你好，我是文心一言，很高兴为您服务！")

# #导入selenium模块
# from selenium import webdriver
#
# from time import sleep
# from selenium.webdriver.common.by import By
#
# #启动浏览器驱动
# driver = webdriver.Chrome()
#
# #访问url
# driver.get('https://www.baidu.com')
#
# #定位元素
# el = driver.find_element(By.ID,'kw')
#
# #执行自动化操作
# el.send_keys('NBA头条')
# bt = driver.find_element(By.ID,'su').click()
#
# #休眠5秒
# sleep(5)
#
# #关闭浏览器并且释放进程资源
# driver.quit()
# import pyecharts
# # print(pyecharts.__version__)
# import pandas as pd

# total_data = pd.read_excel('D:\project\py_project/豆瓣电影Top250.xlsx')
# td = pd.DataFrame(total_data)
# print(td)  # 通常会通过print来检查一下是否顺利读取
# import pandas as pd
# import os
# import xml.etree.ElementTree as ET
#
# def search_xml_files(directory):
#     xml_files = []
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.xml'):
#                 xml_files.append(os.path.join(root, file))
#     return xml_files
#
# def read_code_from_xml(file_path):
#     tree = ET.parse(file_path)
#     root = tree.getroot()
#     code_elements = root.findall('.//Code')
#     code = []
#     for element in code_elements:
#         code.append(element.text)
#     return code
#
# def replace_code_in_xml(file_path, new_code):
#     tree = ET.parse(file_path)
#     root = tree.getroot()
#     code_elements = root.findall('.//Code')
#     for element in code_elements:
#         element.text = new_code
#     tree.write(file_path)
#
# def main():
#     directory = 'D:\project\py_project\\filter_xml_file\\x-public'
#     new_code = '
#     <action name="changeDisplay">
#         <param name="args">sleep 1</param>
#         <param name="secondDisplay">false</param>
#     </action>'
#
#     xml_files = search_xml_files(directory)
#     for file in xml_files:
#         code = read_code_from_xml(file)
#         replace_code_in_xml(file, new_code)
#
# if __name__ == '__main__':
#     main()
# import re
#
# # 读取XML文件
# with open('D:\project\py_project\\filter_xml_file\\x-public\\new.xml', 'r',encoding='utf-8') as file:
#     xml_content = file.read()
#
# # 使用正则表达式替换多行代码
# xml_content = re.sub(r'<action name="changeDisplay">.*?</action>', r'\1', xml_content, flags=re.DOTALL)
#
# # 将替换后的代码写入新的XML文件
# with open('D:\project\py_project\\filter_xml_file\\x-public\\new_file.xml', 'w') as file:
#     file.write(xml_content)

# import re
# import time
#
#
# def replace_text(text):
#     # 定义正则表达式模式
#     pattern = r'<action name="changeDisplay">.*?</action>'
#     pattern1 = r'<param name="args">(.*?)</param>'
#     pattern2 = r'<param name="secondDisplay">(.*?)</param>'
#     pattern3 = r'</action>'
#     repl = r'<action name="changeDisplay">.*?</action>'
#     repl1 = r'\r\n\t\t<param name="args">sleep 1</param>'
#     repl2 = r'\r\n\t\t<param name="secondDisplay">true</param>'
#     repl3 = r'\r\n</action>'
#     # 使用re.sub()函数进行替换
#     new_text = re.sub(pattern, repl, text)
#     # print(new_text)
#     new_text1 = re.sub(pattern1, repl1, text)
#     print(new_text1)
#     new_text2 = re.sub(pattern2, repl2, text)
#     new_text3 = re.sub(pattern3, repl3, text)
#     return new_text + new_text1 + new_text2 + new_text3
#
#
# # def change_display(match, args, second_display):
# #     # 获取匹配到的字符串
# #     matched_str = match.group()
# #
# #     # 解析匹配到的字符串
# #     arg_list = re.findall(r'<param name="args">(.*?)</param>', matched_str)
# #     try:
# #         args = arg_list[0]
# #         second_display = re.search(r'<param name="secondDisplay">(.*?)</param>', matched_str).group(1).lower() == 'true'
# #     except IndexError:
# #         pass
# #
# #     # 显示新的显示
# #     if not second_display:
# #         print(args)
# #     time.sleep(1)
#
# # 示例代码
# xml_text = '<action name="changeDisplay">\r\n\t<param name="args">sleep 1</param>\r\n\t<param name="secondDisplay">false</param></action>'
# new_xml_text = replace_text(xml_text)
# print(new_xml_text)

##创建文件夹
# import os
#
#
# # 创建文件夹
# def mkdir_multi(path):
#     # 判断路径是否存在
#     isExists = os.path.exists(path)
#
#     if not isExists:
#         # 如果不存在，则创建目录（多层）
#         os.makedirs(path)
#         print('目录创建成功！')
#         return True
#     else:
#         # 如果目录存在则不创建，并提示目录已存在
#         print('目录已存在！')
#         return False
#
#
# if __name__ == "__main__":
#     mkdir_multi(r'D:\node_client\li-test-client')
#     mkdir_multi(r'D:\node_client\test_script')
#     mkdir_multi(r'D:\node_client\ZL')
#
#     mkdir_multi(r'D:\liat_studio')
#     mkdir_multi(r'D:\liat_studio\resource')


# 测试函数
#     folder_name = r'D:\node_client\test_script'
# folder_name = r'D:\node_client\ZL'
# folder_name = r'D:\node_client\li-test-client'
# import os
# import requests
# from pandas.io import html
# from requests import head

# res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# #把Response对象的内容已二进制数据形式返回
# pic = res.content
#
# photo = open('ppt.jpg', 'wb')
# photo.write(pic)
# photo.close()

# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# novel = res.text
#
# text = open('sanguo.txt', 'w',encoding='utf-8')
# text.write(novel)
# text.close()

# import requests
# from bs4 import BeautifulSoup

# 获取网页内容
# res = requests.get(
#     'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
#
# soup = BeautifulSoup(res.text, 'html.parser')  # 把网页解析为BeautifulSoup对象
# print(type(soup))
# print(soup)
# item = soup.find('div')#使用find（）方法提取首个<div>元素，并放到变量item里
# print(type(item))
# print(item)
# items = soup.findAll('div')#使用findAll（）方法提取所有<div>元素，并放到变量items里
# print(type(items))
# print(items)
# print(type(items[2]))
# items = soup.findAll(class_='books')
# for item in items:
#     kind = item.find('h2')
#     title = item.find(class_='title')
#     brief = item.find(class_='info')
#     print(type(kind), type(title), type(brief))
#     print(kind.text, '\n', title.text, title.get_text(), '\n', title['href'], '\n', brief.text)  # 打印书籍类型，名字，链接，简介的文字

# res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
# bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
# list_books = bs_bookstore.find_all(class_='product_pod')
# for tag_books in list_books:
#     tag_name = tag_books.find('h3').find('a') # 找到a标签需要提取两次
#     list_star = tag_books.find('p',class_="star-rating")
#     # 这个p标签的class属性有两种："star-rating"，以及具体的几星比如"Two"。我们选择所有书都有的class属性："star-rating"
#     tag_price = tag_books.find('p',class_="price_color") # 价格比较好找，根据属性提取，或者标签与属性一起都可以
#     print(tag_name['title']) # 这里用到了tag['属性名']提取属性值
#     print('star-rating:',list_star['class'][1])
#     # 同样是用属性名提取属性值
#     # 用list_star['class']提取出来之后是一个由两个值组成的列表，如："['star-rating', 'Two']"，我们最终要提取的是这个列表的第1个值："Two"。
#     # 为什么是列表呢？因为这里的class属性有两个值。其实，在这个过程中，我们是使用class属性的第一个值提取出了第二个值。
#     print('Price:',tag_price.text, end='\n'+'------'+'\n')

##拿到前20个歌曲信息的完整代码
# import requests
#
# res_music = requests.get(
#     'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song'
#     '&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC'
#     '%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json'
#     '&needNewCode=0')  # 调用get方法，下载这个字典
# json_music = res_music.json()
# list_music = json_music['data']['song']['list']
# for music in list_music:
#     print(music['name'])
#     print('所属专辑：' + music['album']['name'])
#     print('播放时长：' + str(music['interval']) + '秒')
#     print('播放链接：http://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')
# import json
# a = [1,2,3,4]
# b = json.dumps(a)
# c = json.loads(b)
# print(type(c))
# print(json.dumps(['你','我','他']))
# print(json.dumps(['你','我','他'],ensure_ascii=False))
# import requests
# # 引用requests模块
# url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# for x in range(5):
#     params = {
#         'ct': '24',
#         'qqmusic_ver': '1298',
#         'new_json': '1',
#         'remoteplace': 'sizer.yqq.song_next',
#         'searchid': '64405487069162918',
#         't': '0',
#         'aggr': '1',
#         'cr': '1',
#         'catZhida': '1',
#         'lossless': '0',
#         'flag_qc': '0',
#         'p': str(x+1),
#         'n': '20',
#         'w': '周杰伦',
#         'g_tk': '5381',
#         'loginUin': '0',
#         'hostUin': '0',
#         'format': 'json',
#         'inCharset': 'utf8',
#         'outCharset': 'utf-8',
#         'notice': '0',
#         'platform': 'yqq.json',
#         'needNewCode': '0'
#     }
#     # 将参数封装为字典
#     res_music = requests.get(url, params=params)
#     # 调用get方法，下载这个字典
#     json_music = res_music.json()
#     # 使用json()方法，将response对象，转为列表/字典
#     list_music = json_music['data']['song']['list']
#     # 一层一层地取字典，获取歌单列表
#     for music in list_music:
#         # list_music是一个列表，music是它里面的元素
#         print(music['name'])
#         # 以name为键，查找歌曲名
#         print('所属专辑：'+music['album']['name'])
#         # 查找专辑名
#         print('播放时长：'+str(music['interval'])+'秒')
#         # 查找播放时长
#         print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
#         # 查找播放链接

import csv
#
# csv_file = open(r'D:\project\py_project\demo.csv', 'r+', newline='', encoding='utf-8')
# # writer = csv.writer(csv_file)
# # writer.writerow(['电影','豆瓣评分'])
# # writer.writerow(['银河护卫队','8.0'])
# # writer.writerow(['复仇者联盟','8.1'])
# # csv_file.close()
# reader = csv.reader(csv_file)
# for row in reader:
#     print(row)
# csv_file.close()
# import openpyxl

##利用openpyxl.W欧瑞康book（）函数创建新的workboo(工作簿)对象，创建新的空的excel文件
# wb = openpyxl.Workbook()
# ##wb.active解释获取这个工作簿的活动表，通常是第一个工作表
# sheet = wb.active
# ##可以用.title给工作表重命名，现在第一个工作表的名称就会由原来的sheet1改为：new title
# sheet.title = 'new title'
# ##把漫威宇宙赋值给第一个工作表的A1单元个，就是往A1单元格中写入‘漫威宇宙’
# sheet['A1'] = '漫威宇宙'
# ##把想写入第一行的内容写成列表，赋值给row
# row = ['灭霸', '敲', '响指']
# ##用sheet.appen()就能王表格里添加这一行文字
# sheet.append(row)
# ##把要写入的多行内容写成列表，再放进大列表里，赋值给rows
# rows = [['美国队长', '钢铁侠', '蜘蛛侠'], ['是', '漫威', '宇宙', '经典', '人物']]
# ##通过变量rows。同时把刚遍历的内容添加到表格里 ，实现多行写入
# for i in rows:
#     sheet.append(i)
# wb.save('new excel.xlsx')
# wb = openpyxl.load_workbook(r'D:\project\py_project\new excel.xlsx')
# sheet = wb['new title']
# sheetname = wb.sheetnames
# print(sheetname)
# A1_cell = sheet['A1']
# A1_value = A1_cell.value
# print(A1_value)
# import requests
# import csv
#
# csv_file = open('articles.csv', 'w', newline='', encoding='utf-8')
# writer = csv.writer(csv_file)
# writer.writerow(['标题', '链接', '摘要'])
#
# offset = 0
# while True:
#     url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/80.0.3987.122 Safari/537.36'}
#     params = {
#         'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,'
#                    'comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,'
#                    'voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
#         'offset': str(offset),
#         'limit': '20',
#         'sort_by': 'created'
#     }
#
#     res = requests.get(url, params=params, headers=headers)
#     resjson = res.json()
#     articles = resjson['data']
#     for article in articles:
#         title = article['title']
#         link = article['url']
#         excerpt = article['excerpt']
#         writer.writerow([title, link, excerpt])
#
#     offset += 20
#     if offset > 40:
#         break
#     # if resjson['paging']['is_end'] == True:
#     #     break
# csv_file.close()

##评论博客import requests
# 引入requests
# url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# # 把请求登录的网址赋值给url
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
# }
# # 加请求头，加请求头是为了模拟浏览器正常的访问，避免被反爬虫
# data = {
#     'log': 'spiderman',  # 写入账户
#     'pwd': 'crawler334566',  # 写入密码
#     'wp-submit': '登录',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# # 把有关登录的参数封装成字典，赋值给data
# login_in = requests.post(url, headers=headers, data=data)
# # 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in
# print(login_in)
# # 打印login_in
# # 》》<Response [200]>
# cookies = login_in.cookies
# # 提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies
#
# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# # 想要评论的文章网址
# data_1 = {
#     'comment': 'cookies测试',
#     'submit': '发表评论',
#     'comment_post_ID': '13',
#     'comment_parent': '0'
# }
# # 把有关评论的参数封装成字典
# comment = requests.post(url_1, headers=headers, data=data_1, cookies=cookies)
# # 用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment
# # 调用cookies的方法就是在post请求中传入cookies=cookies的参数
# print(comment.status_code)
# # 打印出comment的状态码，若状态码等于200，则证明评论成功
# # 》》200

# import requests
# # 引用requests
# session = requests.session()
# # 用requests.session()创建session对象，相当于创建了一个特定的会话，自动保持了cookies
# url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# data = {
#     'log': 'spiderman',
#     'pwd': 'crawler334566',
#     'wp-submit': '登录',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# session.post(url, headers=headers, data=data)
# # 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数
#
# url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# # 把想要评论的文章网址赋值给url_1
# data_1 = {
#     'comment': 'session测试',
#     'submit': '发表评论',
#     'comment_post_ID': '13',
#     'comment_parent': '0'
# }
# # 把有关评论的参数封装成字典
# comment = session.post(url_1, headers=headers, data=data_1)
# # 在创建的session下用post发起评论请求，放入参数：文章网址，请求头和评论参数，并赋值给comment
# print(comment)
# # 打印comment
# # 》》<Response [200]>

# import requests,json
# # 引入requests和json模块
# session = requests.session()
# url = ' https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# data = {
#     'log': 'spiderman',
#     'pwd': 'crawler334566',
#     'wp-submit': '登录',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# session.post(url,headers=headers,data=data)
# ##把cookies转化成字典
# cookies_dict= requests.utils.dict_from_cookiejar(session.cookies)
# print(cookies_dict)
# ##调用json模块的dumps函数，把cookies从字典转换成字符串
# cookies_str = json.dumps(cookies_dict)
# print(cookies_str)
# ##创建名为cookies.txt的文件，写入模式写入内容
# f = open('cookies.txt','w')
# f.write(cookies_str)
# f.close()

##fielter用于过滤序列
# id_filter = filter(str.isdigit,'https://www.xslou.com/yuedu/22177/')
# print(type(id_filter))
# id_list = list(id_filter)
# print(id_list)
# id_str = ''.join(id_list)
# print(id_str)

# ##过滤出列表中的所有奇数
# def is_odd(n):
#     return n % 2 ==1
#
# temlist = filter(is_odd,[1,2,3,4,5,6,7,8,9])
# newlist = list(temlist)
# print(newlist)

##自制翻译小程序
# import requests
# from tkinter import Tk, Text, Button, Label, END
#
# def crawl(word):
#     url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
#     data = {'i': word,
#             'from': 'AUTO',
#             'to': 'AUTO',
#             'smartresult': 'dict',
#             'client': 'fanyideskweb',
#             'doctype': 'json',
#             'version': '2.1',
#             'keyfrom': 'fanyi.web',
#             'action': 'FY_BY_REALTIME',
#             'typoResult': 'false'}
#     res = requests.post(url, data=data, headers=headers)
#     try:
#         result = res.json()['translateResult'][0][0]['tgt']
#     except:
#         result = ""
#     return result
#
# def trans():
#     content = text.get(0.0, END).strip().replace("\n", " ")
#     result = crawl(content)
#     result_text.configure(state='normal')
#     result_text.delete(0.0, END)
#     result_text.insert(END, result)
#     result_text.configure(state='disabled')
#
# def clean():
#     text.delete(0.0, END)
#     result_text.configure(state='normal')
#     result_text.delete(0.0, END)
#     result_text.configure(state='disabled')
#
# root = Tk()
# # 生成主窗口
# root.title('翻译器')
# # 修改框体的名字,也可在创建时使用className参数来命名
# root.geometry('380x500')
# # 指定主框体大小，geometry(宽度x高度+左上角水平坐标+左上角垂直坐标）（是英文x不是乘号）
# text = Text(root, bg='gray90')
# # 生成多行文本框，bg指定了背景色
# # 选颜色的链接：http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
# text.place(x=5, y=5, width=370, height=230)
# # 布局控件：pack,grid,place，这里使用的是place。x:组件左上角的x坐标，y:组件右上角的y坐标，width:组件的宽度，heitht:组件的高度
# trans_btn = Button(root, text='翻译', command=trans)
# # 生成“翻译”按钮，调用trans方法
# trans_btn.place(x=278, y=238, width=45, height=24)
# wipe_btn = Button(root, text='清空', command=clean)
# # 生成“清空”按钮，调用clean方法
# wipe_btn.place(x=328, y=238, width=45, height=24)
# title_label = Label(root, text='翻译结果')
# # 生成“翻译结果”标题标签˝
# title_label.place(x=5, y=238)
# result_text = Text(root, bg='gray90')
# # 生成显示结果的多行文本框
# result_text.configure(state='disabled')
# # 为了实现只读效果，将文本框状态设置为disabled
# result_text.place(x=5, y=265, width=370, height=230)
# root.mainloop()
# # 窗口事件主循环

# ##图灵机器人
# import requests
# import json
#
# url = 'http://openapi.tuling123.com/openapi/api/v2'
# # 接口地址
# while True:
#     chat = input('我：')
#     data = {
#         "reqType": 0,
#         "perception": {
#             "inputText": {
#                 "text": chat
#             }
#         },
#         "userInfo": {
#             "apiKey": "...",
#             # apiKey是针对接口访问的授权方式。注册登录后创建机器人，会生成apiKey
#             "userId": "xiaomei"
#             # userId：长度需小于32，是用户的唯一标识
#         }
#     }
#     # perception和userInfo是必须要填写的参数
#     res = requests.post(url, data=json.dumps(data))
#     # 请求参数格式为 json
#     result = res.json()['results'][0]['values']['text']
#     print('图小智：'+result)
##查询python路径
# import sys
#
# for i in sys.path:
#     print(i)
# from selenium import webdriver##从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options##从options模块中调用Opeions类
#
# import time
# ##本地Chrome浏览器设置方法
# driver = webdriver.Chrome()##设置引擎为Chrome，真实地打开一个Chrome
#
# # chrome_options = Options()##实例化Options对象
# # chrome_options.add_argument('--headless')##把Chrome浏览器设置为静默模式
# # driver = webdriver.Chrome(options=chrome_options)##设置引起为Chrom，在后台默默运行
#
# url = 'https://www.cdsn.net/'
# driver.get(url)
# driver.maximize_window()
# driver.refresh()
# time.sleep(1)
# driver.quit()

###获取、解析与提取数据 本关学习以【你好蜘蛛侠！】这个网站为例
# import time
# from selenium.webdriver.common.by import By
#
# # 本地Chrome浏览器设置方法
# from selenium import webdriver  # 从selenium库中调用webdriver模块
#
# driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
#
# # 获取数据
# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')  # 通过实例化的浏览器打开网页
# time.sleep(2)  # 等待2秒，等浏览器加载缓冲数据
#
# # 解析与提取数据
# # 解析数据是由driver自动完成的，提取数据是driver的一个方法
# label = driver.find_element(By.TAG_NAME, 'label')  # 解析网页并提取第一个<lable>标签中的文字
# print(type(label))  # 打印label的数据类型
# # 》》<class 'selenium.webdriver.remote.webelement.WebElement'>
# print(label.text)  # 打印label的文本
# # 》》（提示：吴枫）
# print(label)  # 打印label
# # 》》<selenium.webdriver.remote.webelement.WebElement (session="d776d7492e34a61bc565e755ce082388",
# # element="0.30820374741568446-1")>
# teacher = driver.find_element(By.CLASS_NAME, 'teacher')  # 根据类名找到元素##此处有更新参考：Selenium-定位元素最新定位方法，find_element(By.ID,'元素')
# # print(type(teacher))  # 打印teacher的数据类型
# # 》》<class 'selenium.webdriver.remote.webelement.WebElement'>
# print(teacher.get_attribute('type'))  # 获取type这个属性的值
# # 》》text
# driver.close()  # 关闭浏览器驱动，每次调用了webdriver之后，都要在用完它之后加上一行driver.close()用来关闭它


##获取渲染完整的网页源代码
# import time
# # 本地Chrome浏览器的静默模式设置：
# from selenium import webdriver  # 从selenium库中调用webdriver模块
# from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
#
# chrome_options = Options()  # 实例化Option对象
# chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
# driver = webdriver.Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行
#
# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# time.sleep(2)
#
# pageSource = driver.page_source  # 获取完整渲染的网页源代码
# print(type(pageSource))  # 打印pageSource的类型
# # 》》<class 'str'>
# print(pageSource)  # 打印pageSource
# driver.close()  # 关闭浏览器

##自动操作浏览器
# 本地Chrome浏览器设置方法
# from selenium import webdriver  # 从selenium库中调用webdriver模块
# from bs4 import BeautifulSoup  # 导入BeautifulSoup
# import time  # 调用time模块
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()  # 设置引擎为Chrome，真实地打开一个Chrome浏览器
#
# driver.get(
#     'https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')  # 访问页面
# time.sleep(2)  # 暂停两秒，等待浏览器缓冲
#
# teacher = driver.find_element(By.ID,'teacher')  # 找到【请输入你喜欢的老师】下面的输入框位置
# teacher.send_keys('蜘蛛侠')  # 输入文字
# time.sleep(1)
# teacher.clear()  # 清除文字
# time.sleep(1)
# teacher.send_keys('穿着熊')  # 再次输入文字
# time.sleep(1)
# assistant = driver.find_element(By.NAME,'assistant')  # 找到【请输入你喜欢的助教】下面的输入框位置
# assistant.send_keys('都喜欢')  # 输入文字
# time.sleep(1)
# button = driver.find_element(By.CLASS_NAME,'sub')  # 找到【提交】按钮
# button.click()  # 点击【提交】按钮
# time.sleep(1)
# bs = BeautifulSoup(driver.page_source, 'html.parser')
# content_en = bs.find_all('div', class_='content')[0]
# title_en = content_en.find('h1').text
# zen_en = content_en.find('p').text
# content_ch = bs.find_all('div', class_='content')[1]
# title_ch = content_ch.find('h1').text
# zen_ch = content_ch.find('p').text
# driver.close()  # 关闭浏览器

##定时功能import requests,未跑通
# import smtplib
# import schedule
# import time
# from bs4 import BeautifulSoup
# from email.mime.text import MIMEText
# from email.header import Header
#
# account = '1290897435@qq.com：'
# password = '950208Lmj'
# receiver = 'zhangyantsxy@163.com'
#
#
# def weather_spider():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#     url = 'http://www.weather.com.cn/weather/101280601.shtml'
#     res = requests.get(url, headers=headers)
#     res.encoding = 'utf-8'
#     soup = BeautifulSoup(res.text, 'html.parser')
#     tem1 = soup.find(class_='tem')
#     weather1 = soup.find(class_='wea')
#     tem = tem1.text
#     weather = weather1.text
#     return tem, weather
#
#
# def send_email(tem, weather):
#     mailhost = 'smtp.qq.com'
#     qqmail = smtplib.SMTP()
#     qqmail.connect(mailhost, 25)
#     qqmail.login(account, password)
#     content = tem + weather
#     message = MIMEText(content, 'plain', 'utf-8')
#     subject = '今日天气预报'
#     message['Subject'] = Header(subject, 'utf-8')
#     try:
#         qqmail.sendmail(account, receiver, message.as_string())
#         print('邮件发送成功')
#     except:
#         print('邮件发送失败')
#     qqmail.quit()
#
#
# def job():
#     print('开始一次任务')
#     # tem, weather = weather_spider()
#     # send_email(tem, weather)
#     print('任务完成')
#
#
# schedule.every(2).seconds.do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# from datetime import time
# ##datetime的timedTask()会一直占用CPU，导致后续操作无法执行，谨慎使用
# from threading import Timer
#
# """
# 每10秒打印当前时间
# """
#
#
# def timedTask():
#     # while True:
#     #     print(datetime.now().strftime('%y-%m-%d %h:%M:%S'))
#     #     time.sleep(2)
#     """
#     第一个参数：延迟多长时间执行任务（单位：秒）
#     第二个参数：要执行的任务，及函数
#     第三个参数：要调用的参数(tuple)
#     """
#     Timer(2, task, ()).start()
#
#
# def task():
#     print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# if __name__ == '__main__':
#     timedTask()
#     while True:
#         print(time.time())
#         time.sleep(1)
### 3.使用标准库中的sched模块达到定时执行任务的目的
# from datetime import datetime
# import time
# import sched
#
# """每隔3秒打印当前时间"""
#
#
# def timeTask():
#     ##初始化 sched 模块的 scheduler 类
#     scheduler = sched.scheduler(time.time, time.sleep)
#     ##增加调度任务
#     scheduler.enter(3, 1, task)
#     # 运行任务
#     scheduler.run()
#
#
# def task():
#     print(datetime.now().strftime('%H-%m-%d %H:%M:%S'))
#
#
# if __name__ == '__main__':
#     while True:
#         timeTask()


###APScheduler轻量的python定时任务调度框架，支持三种调度任务：固定时间间隔，固定时间点（日期），Linux下的Crontab命令，同时他还支持异步执行，后台调度任务
# from datetime import datetime
# import datetime
# import time
# # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# from apscheduler.schedulers.background import BackgroundScheduler
#
#
# def timedTask():
#     # cur_time = datetime.datetime.now()
#     # print(cur_time.strftime('%Y-%m-%d %H:%M:%S'))
#     print(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
#
#
# if __name__ == '__main__':
#     # 创建后台执行的scheduler
#     scheduler = BackgroundScheduler()
#     # 添加调度任务
#     # 调度方法未：timedTask，触发器选择interval(间隔性)，间隔时长为2秒
#     scheduler.add_job(timedTask, 'interval', seconds=2)##正确的使用方法
#     # scheduler.add_job(timedTask(), 'interval', seconds=2)##错误的使用方法
#     ##这是python定时器apschedurler的schduler.add_job(iotmain(), “cron”, hour = 7, minute = 00)语句里面，调用的方法iotmain()不能带（），改写为：scheduler.add_job(iotmain, “cron”, hour = 7, minute = 00)，恢复正常，即每天7：00调用方法iotmain()。原因参考此文：https://pdf-lib.org/Home/Details/8447
#     # 启动调度任务
#     scheduler.start()
#
#     while True:
#         print(time.time())
#         time.sleep(3)

##先用同步的爬虫方式爬取百度、新浪、搜狐、腾讯、网易、爱奇艺、天猫、凤凰这个8个网站，看下用了多长时间
# import requests
# import time
# # 导入requests和time
# start = time.time()
# # 记录程序开始时间
#
# url_list = ['https://www.baidu.com/',
#             'https://www.sina.com.cn/',
#             'http://www.sohu.com/',
#             'https://www.qq.com/',
#             'https://www.163.com/',
#             'http://www.iqiyi.com/',
#             'https://www.tmall.com/',
#             'http://www.ifeng.com/']
# # 把8个网站封装成列表
#
# for url in url_list:
# # 遍历url_list
#     r = requests.get(url)
#     # 用requests.get()函数爬取网站
#     print(url, r.status_code)
#     # 打印网址和抓取请求的状态码
#
# end = time.time()
# # 记录程序结束时间
# end_time = end-start
# formatted_time = datetime.datetime.fromtimestamp(end_time)###datetime.datetime.fromtimestamp()方法将时间戳转换为datetime对象，浮点数换成日期并打印
#
# print(formatted_time)
# # end-start是结束时间减去开始时间，就是最终所花时间
# # 最后，把时间打印出来
# # 》》https://www.baidu.com/ 200
# # 》》https://www.sina.com.cn/ 200
# # 》》http://www.sohu.com/ 200
# # 》》https://www.qq.com/ 200
# # 》》https://www.163.com/ 200
# # 》》http://www.iqiyi.com/ 200
# # 》》https://www.tmall.com/ 200
# # 》》http://www.ifeng.com/ 200
# # 》》0.5697987079620361


# 同步的爬虫方式，是依次爬取网站，并等待服务器响应（状态码为200表示正常响应）后，才爬取下一个网站。比如第一个先爬取了百度的网址，等服务器响应后，再去爬取新浪的网址，以此类推，直至全部爬取完毕。再看看用多协程
# from gevent import monkey
# # 从gevent库里导入monkey模块
# monkey.patch_all()
# # monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步
# import gevent,time,requests
# # 导入gevent、time、requests
#
# start = time.time()
# # 记录程序开始时间
#
# url_list = ['https://www.baidu.com/',
#             'https://www.sina.com.cn/',
#             'http://www.sohu.com/',
#             'https://www.qq.com/',
#             'https://www.163.com/',
#             'http://www.iqiyi.com/',
#             'https://www.tmall.com/',
#             'http://www.ifeng.com/']
# # 把8个网站封装成列表。
#
#
# def crawler(url):
# # 定义一个crawler()函数
#     r = requests.get(url)
#     # 用requests.get()函数爬取网站
#     print(url, time.time()-start, r.status_code)
#     # 打印网址、请求运行时间、状态码
#
#
# tasks_list = []
# # 创建空的任务列表
#
# for url in url_list:
# # 遍历url_list
#     task = gevent.spawn(crawler, url)
#     # 用gevent.spawn()函数创建任务
#     tasks_list.append(task)
#     # 往任务列表添加任务
# gevent.joinall(tasks_list)
# # 执行任务列表里的所有任务，就是让爬虫开始爬取网站
# end = time.time()
# # 记录程序结束时间
# print(end-start)
# time_cost = end-start
# formatted_time = datetime.datetime.fromtimestamp(time_cost)
# # 把时间打印出来
# print(formatted_time)
# # 打印程序最终所需时间
# # 》》http://www.ifeng.com/ 0.08891010284423828 200
# # 》》https://www.baidu.com/ 0.1046142578125 200
# # 》》https://www.sina.com.cn/ 0.12417197227478027 200
# # 》》https://www.163.com/ 0.12881922721862793 200
# # 》》https://www.qq.com/ 0.1435079574584961 200
# # 》》http://www.sohu.com/ 0.1657421588897705 200
# # 》》https://www.tmall.com/ 0.18058228492736816 200
# # 》》http://www.iqiyi.com/ 0.18367409706115723 200
# # 》》0.18380022048950195

# from gevent import monkey
#
# monkey.patch_all()
# import gevent, time, requests
# from gevent.queue import Queue
#
# # 从gevent库的queue模块导入Queue类
#
# start = time.time()
#
# url_list = ['https://www.baidu.com/',
#             'https://www.sina.com.cn/',
#             'http://www.sohu.com/',
#             'https://www.qq.com/',
#             'https://www.163.com/',
#             'http://www.iqiyi.com/',
#             'https://www.tmall.com/',
#             'http://www.ifeng.com/']
#
# work = Queue()
# # 创建队列对象，并赋值给work
# for url in url_list:
#     work.put_nowait(url)
#     # 用put_nowait()函数可以把网址都放进队列里
#
#
# def crawler():
#     while not work.empty():
#         # 当队列不是空的时候，就执行下面的程序
#         url = work.get_nowait()
#         # 用get_nowait()函数可以把队列里的网址都取出
#         r = requests.get(url)
#         # 用requests.get()函数抓取网址
#         print(url, work.qsize(), r.status_code)
#         # 打印网址、队列长度、抓取请求的状态码
#
#
# tasks_list = []
#
# for x in range(2):
#     # 相当于创建了2个爬虫
#     task = gevent.spawn(crawler)
#     # 用gevent.spawn()函数创建执行crawler()函数的任务
#     tasks_list.append(task)
#
# gevent.joinall(tasks_list)
#
# end = time.time()
# print(end - start)
# # 》》https://www.baidu.com/ 6 200
# # 》》https://www.sina.com.cn/ 5 200
# # 》》http://www.sohu.com/ 4 200
# # 》》https://www.163.com/ 3 200
# # 》》https://www.qq.com/ 2 200
# # 》》http://www.iqiyi.com/ 1 200
# # 》》http://www.ifeng.com/ 0 200
# # 》》https://www.tmall.com/ 0 200
# # 》》0.3898591995239258

##仅展示前3个常见食物分类的前3页和第11个常见食物分类的前3页的食物信息# 导入所需的库和模块
# from gevent import monkey
#
# monkey.patch_all()
# # 让程序变成异步模式
# import gevent, requests, bs4, csv
# from gevent.queue import Queue
#
# work = Queue()
# # 创建队列对象，并赋值给work
#
# # 前3个常见食物分类的前3页的食物记录的网址
# url_1 = 'http://www.boohee.com/food/group/{type}?page={page}'
# for x in range(1, 4):
#     for y in range(1, 4):
#         real_url = url_1.format(type=x, page=y)
#         work.put_nowait(real_url)
# # 通过两个for循环，能设置分类的数字和页数的数字
# # 然后，把构造好的网址用put_nowait方法添加进队列里
#
# # 第11个常见食物分类的前3页的食物记录的网址
# url_2 = 'http://www.boohee.com/food/view_menu?page={page}'
# for x in range(1, 4):
#     real_url = url_2.format(page=x)
#     work.put_nowait(real_url)
#
#
# # 通过for循环，能设置第11个常见食物分类的食物的页数
# # 然后，把构造好的网址用put_nowait方法添加进队列里
#
# def crawler():
#     # 定义crawler函数
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
#     }
#     # 添加请求头
#     while not work.empty():
#         # 当队列不是空的时候，就执行下面的程序
#         url = work.get_nowait()
#         # 用get_nowait()方法从队列里把刚刚放入的网址提取出来
#         res = requests.get(url, headers=headers)
#         # 用requests.get获取网页源代码
#         bs_res = bs4.BeautifulSoup(res.text, 'html.parser')
#         # 用BeautifulSoup解析网页源代码
#         foods = bs_res.find_all('li', class_='item clearfix')
#         # 用find_all提取出<li class="item clearfix">标签的内容
#         for food in foods:
#             # 遍历foods
#             food_name = food.find_all('a')[1]['title']
#             # 用find_all在<li class="item clearfix">标签下，提取出第2个<a>元素title属性的值，也就是食物名称
#             food_url = 'http://www.boohee.com' + food.find_all('a')[1]['href']
#             # 用find_all在<li class="item clearfix">元素下，提取出第2个<a>元素href属性的值，跟'http://www.boohee.com'组合在一起，就是食物详情页的链接
#             food_calorie = food.find('p').text
#             # 用find在<li class="item clearfix">标签下，提取<p>元素，再用text方法留下纯文本，也提取出了食物的热量
#             writer.writerow([food_name, food_calorie, food_url])
#             # 借助writerow()函数，把提取到的数据：食物名称、食物热量、食物详情链接，写入csv文件
#             print(food_name)
#             # 打印食物的名称
#
#
# csv_file = open('boohee.csv', 'w', newline='')
# # 调用open()函数打开csv文件，传入参数：文件名“boohee.csv”、写入模式“w”、newline=''
# writer = csv.writer(csv_file)
# # 用csv.writer()函数创建一个writer对象
# writer.writerow(['食物', '热量', '链接'])
# # 借助writerow()函数往csv文件里写入文字：食物、热量、链接
#
# tasks_list = []
# # 创建空的任务列表
# for x in range(5):
#     # 相当于创建了5个爬虫
#     task = gevent.spawn(crawler)
#     # 用gevent.spawn()函数创建执行crawler()函数的任务
#     tasks_list.append(task)
#     # 往任务列表添加任务
# gevent.joinall(tasks_list)
# # 用gevent.joinall方法，启动协程，执行任务列表里的所有任务，让爬虫开始爬取网站


##获取豆瓣Top250图书前三页书籍的信息
