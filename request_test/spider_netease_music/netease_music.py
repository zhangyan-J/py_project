import requests
import re
import os
import sys

# filename = r'D:\project\py_project\request_test\spider_netease_music\hot_music\\'  ##双斜杠代表在这个目录下创建文件夹
#
# if not os.path.exists(filename):  # 如果没有这个文件夹，则创建
#     os.mkdir(filename)
# #如果想爬取其他榜单的音乐，只需要更改url中的ID即可
# # url = r'https://music.163.com/discover/toplist?id=6886768100'
# url = r'https://music.163.com/playlist?id=8436434272'
# # heads 请求头，
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 '
#                   'Safari/537.36'
# }
# response = requests.get(url=url, headers=headers)
# print(response.text)
# # 正则表达式匹配html中的属性，\d+表示匹配数字，.*?表示匹配任意字符
# html_data = re.findall(r'<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)
# # 正则表达式提取处理的内容返回的是列表，里边的美国元素都是一个元组
# for num_id, title in html_data:
#     music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
#     # 对应音乐播放地址发送请求，获取二进制数据内容
#     music_content = requests.get(url=music_url, headers=headers).content
#     # 将二进制数据写入文件
#     with open(filename + title + '.mp3', 'wb') as f:
#         f.write(music_content)
#
#     print(num_id, title)

import requests
from lxml import etree
import xlrd, xlwt, os
from xlutils.copy import copy


def chucun_excel():
    # if not os.path.exists(f'海口历史天气【2023年11月】.xls'):
    wb = xlwt.Workbook()
    # 创建一个工作表
    sheet = wb.add_sheet('海口历史天气【2023年11月】')
    header = ['日期', '最高气温', '最低气温', '天气', '风向']

    for i in range(len(header)):
        sheet.write(0, i, header[i])

    wb.save(f'海口历史天气【2023年11月】.xls')

    # return f'海口历史天气【2023年11月】.xls'



chucun_excel()
