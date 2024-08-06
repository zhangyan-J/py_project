import os
import requests  # 数据请求
from lxml import etree  # 进行数据预处理
import csv

# /html/body/div[7]/div[1]/div[4]/ul/li
def getWeather(url):
    weather_info = []  # 新建一个列表，将爬取的每个月的数据放进去
    # 请求头信息：浏览器版本型号，接受数据的编码格式
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    # 请求
    resp = requests.get(url, headers=headers)
    # 数据预处理
    resp_html = etree.HTML(resp.text)
    # xpath提取所有数据
    resp_list = resp_html.xpath("//ul[@class='thrui']/li")
    print(resp_list)

    # for循环迭代遍历
    for li in resp_list:
        # 每天的数据放到一个字典里
        day_weather_info = {}
        # 日期 日期格式是：例如：2019-12-12 星期二 但是我们不需要星期二这个数据，所以要筛选下
        day_weather_info['data_time'] = li.xpath("./div[1]/text()")[0].split(' ')[0]
        # 最高气温 （包含摄氏度符号）
        high = li.xpath("./div[2]/text()")[0]
        # 最高温度：做一个字符串的切割处理，切割到”°C“的所有位置（包头不包尾）
        day_weather_info['high'] = high[:high.find('°C')]
        # 最低气温
        low = li.xpath("./div[3]/text()")[0]
        # 最低气温：做一个字符串切割处理，切割刀“°C“的所有位置（包头不包尾）
        day_weather_info['low'] = low[:low.find('°C')]
        # 天气
        day_weather_info['weather'] = li.xpath("./div[4]/text()")[0]
        # 再将每天的数据字典写入数据列表中
        weather_info.append(day_weather_info)
    return weather_info


# 全年的天气数据列表 大概这样：：[ [ {},{},{}..],[{},{},{}..],[{},{},{}],..]
weathers = []

# for循环生成有顺序的1-12
for month in range(1, 13):
    # 获取某一月的天气信息
    # 三元表达式：如果月份小于10，前面补0，否则不补
    wether_time = '2023' + ('0' + str(month) if month < 10 else str(month))
    # 写成if else判断
    # if month < 10:
    #     wether_time = '2023' + ('0' + str(month))
    # else:
    #     wether_time = '2023' + str(month)
    # 找url规律， 进行拼接 -- 拿到是某一月的所有数据
    url = f'https://lishi.tianqi.com/changsha/{wether_time}.html'
    # 爬虫获取这个月的历史天气
    weather = getWeather(url)
    # 存到列表里
    weathers.append(weather)
# print(weathers)

# 数据写入（一次性写入）
with open(r'D:\project\py_project\request_test\spider_weather\weather.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 先写入列名：columns_name
    writer.writerow(["日期", "最高气温", "最低气温", '天气'])
    # 一次性写入多行用writerows(写入的数据类型是列表，一个列表对应一行)
    # writer.writerows(
    #     [list(day_weather_dict.values()) for month_weather in weathers for day_weather_dict in month_weather])
    #
    list_year = []
    for month_weather in weathers:
        for day_weather_dict in month_weather:
            list_year.append(list(day_weather_dict.values()))
    writer.writerows(list_year)

