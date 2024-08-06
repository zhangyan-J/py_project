# import os
# import requests  # 数据请求
# from lxml import etree  # 进行数据预处理
# import csv
#
# # /html/body/div[7]/div[1]/div[4]/ul/li
# def getWeather(url):
#     weather_info = []  # 新建一个列表，将爬取的每个月的数据放进去
#     # 请求头信息：浏览器版本型号，接受数据的编码格式
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
#     }
#     # 请求
#     resp = requests.get(url, headers=headers)
#     # 数据预处理
#     resp_html = etree.HTML(resp.text)
#     # xpath提取所有数据
#     resp_list = resp_html.xpath("//ul[@class='thrui']/li")
#     print(resp_list)
#
#     # for循环迭代遍历
#     for li in resp_list:
#         # 每天的数据放到一个字典里
#         day_weather_info = {}
#         # 日期 日期格式是：例如：2019-12-12 星期二 但是我们不需要星期二这个数据，所以要筛选下
#         day_weather_info['data_time'] = li.xpah("./div[1]/text()")[0].split(' ')[0]
#         # 最高气温 （包含摄氏度符号）
#         high = li.xpah(".div[2]/text()")[0]
#         # 最高温度：做一个字符串的切割处理，切割到”°C“的所有位置（包头不包尾）
#         day_weather_info['high'] = high[:high.find('°C')]
#         # 最低气温
#         low = li.xpah("./div[3]/text()")[0]
#         # 最低气温：做一个字符串切割处理，切割刀“°C“的所有位置（包头不包尾）
#         day_weather_info['low'] = low[:low.find('°C')]
#         # 天气
#         day_weather_info['weather'] = li.xpath("./div[4]/text()")[0]
#         # 再将每天的数据字典写入数据列表中
#         weather_info.append(day_weather_info)
#     return weather_info
#
#
# # 全年的天气数据列表 大概这样：：[ [ {},{},{}..],[{},{},{}..],[{},{},{}],..]
# weathers = []
#
# # for循环生成有顺序的1-12
# for month in range(1, 13):
#     # 获取某一月的天气信息
#     # 三元表达式：如果月份小于10，前面补0，否则不补
#     wether_time = '2023' + ('0' + str(month) if month < 10 else str(month))
#     # 写成if else判断
#     # if month < 10:
#     #     wether_time = '2023' + ('0' + str(month))
#     # else:
#     #     wether_time = '2023' + str(month)
#     # 找url规律， 进行拼接 -- 拿到是某一月的所有数据
#     url = f'https://lishi.tianqi.com/changsha/{wether_time}.html'
#     # 爬虫获取这个月的历史天气
#     weather = getWeather(url)
#     # 存到列表里
#     weathers.append(weather)
# print(weathers)
#
# # 数据写入（一次性写入）
# with open(r'D:\project\py_project\request_test\spider_weather\weather.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#
#     # 先写入列名：columns_name
#     writer.writerow(["日期", "最高气温", "最低气温", '天气'])
#     # 一次性写入多行用writerows(写入的数据类型是列表，一个列表对应一行)
#     # writer.writerows(
#     #     [list(day_weather_dict.values()) for month_weather in weathers for day_weather_dict in month_weather])
#     #
#     list_year = []
#     for month_weather in weathers:
#         for day_weather_dict in month_weather:
#             list_year.append(list(day_weather_dict.values()))
#     writer.writerows(list_year)


# weather.py
import requests
from lxml import etree
import xlrd, xlwt, os
from xlutils.copy import copy


class TianQi():
    def __init__(self):
        pass

    # 爬虫部分
    def spider(self):
        city_dict = {"海口": "haikou"
                     }
        city = '海口'
        city = city_dict[f'{city}']
        year = '2023'
        month = '11'
        start_url = f'https://lishi.tianqi.com/{city}/{year}{month}.html'
        headers = {'authority': 'lishi.tianqi.com',
                   'accept': 'text_html,application_xhtml+xml,application_xml;q=0.9,image_avif,image_webp,image_apng,**;q=0.8,application_signed-exchange;v=b3;q=0.7',
                   'accept-language': 'zh-CN,zh;q=0.9',
                   'cache-control': 'no-cache',
                   # Requests sorts cookies= alphabetically
                   'cookie': 'Hm_lvt_7c50c7060f1f743bccf8c150a646e90a=1701184759; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1701184793; Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1701184932; Hm_lpvt_7c50c7060f1f743bccf8c150a646e90a=1701185017',
                   'pragma': 'no-cache',
                   'referer': 'https://lishi.tianqi.com/ankang/202309.html',
                   'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                   'sec-ch-ua-mobile': '?0',
                   'sec-ch-ua-platform': '"Windows"',
                   'sec-fetch-dest': 'document',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-site': 'same-origin',
                   'sec-fetch-user': '?1',
                   'upgrade-insecure-requests': '1',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
                   }
        response = requests.get(start_url, headers=headers).text
        tree = etree.HTML(response)
        datas = tree.xpath(
            "/html/body/div[@class='main clearfix']/div[@class='main_left inleft']/div[@class='tian_three']/ul[@class='thrui']/li")
        weizhi = tree.xpath(
            "/html/body/div[@class='main clearfix']/div[@class='main_left inleft']/div[@class='inleft_tian']/div[@class='tian_one']/div[@class='flex'][1]/h3/text()")[
            0]
        self.parase(datas, weizhi, year, month)

    # 解析部分
    def parase(self, datas, weizhi, year, month):
        for data in datas:
            # 1、日期
            datetime = data.xpath("./div[@class='th200']/text()")[0]
            # 2、最高气温
            max_qiwen = data.xpath("./div[@class='th140'][1]/text()")[0]
            # 3、最低气温
            min_qiwen = data.xpath("./div[@class='th140'][2]/text()")[0]
            # 4、天气
            tianqi = data.xpath("./div[@class='th140'][3]/text()")[0]
            # 5、风向
            fengxiang = data.xpath("./div[@class='th140'][4]/text()")[0]
            dict_tianqi = {'日期': datetime,
                           '最高气温': max_qiwen,
                           '最低气温': min_qiwen,
                           '天气': tianqi,
                           '风向': fengxiang
                           }
            data_excel = {f'{weizhi}【{year}年{month}月】': [datetime, max_qiwen, min_qiwen, tianqi, fengxiang]
                          }
            self.chucun_excel(data_excel, weizhi, year, month)
            print(dict_tianqi)

    # 储存部分
    def chucun_excel(self, data, weizhi, year, month):
        if not os.path.exists(f'{weizhi}【{year}年{month}月】.xls'):
            # 1、创建 Excel 文件
            wb = xlwt.Workbook(encoding='utf-8')
            # 2、创建新的 Sheet 表
            sheet = wb.add_sheet(f'{weizhi}【{year}年{month}月】', cell_overwrite_ok=True)
            # 3、设置 Borders边框样式
            borders = xlwt.Borders()
            borders.left = xlwt.Borders.THIN
            borders.right = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            borders.left_colour = 0x40
            borders.right_colour = 0x40
            borders.top_colour = 0x40
            borders.bottom_colour = 0x40
            style = xlwt.XFStyle()  # Create Style
            style.borders = borders  # Add Borders to Style
            # 4、写入时居中设置
            align = xlwt.Alignment()
            align.horz = 0x02  # 水平居中
            align.vert = 0x01  # 垂直居中
            style.alignment = align
            # 5、设置表头信息, 遍历写入数据， 保存数据
            header = ('日期', '最高气温', '最低气温', '天气', '风向')
            for i in range(0, len(header)):
                sheet.col(i).width = 2560 * 3
            # 行，列， 内容，   样式
                sheet.write(0, i, header[i], style)
            wb.save(f'{weizhi}【{year}年{month}月】.xls')
            # 判断工作表是否存在
        if os.path.exists(f'{weizhi}【{year}年{month}月】.xls'):
            # 打开工作薄
            wb = xlrd.open_workbook(f'{weizhi}【{year}年{month}月】.xls')
            # 获取工作薄中所有表的个数
            sheets = wb.sheet_names()
            for i in range(len(sheets)):
                for name in data.keys():
                    worksheet = wb.sheet_by_name(sheets[i])
                    # 获取工作薄中所有表中的表名与数据名对比
                    if worksheet.name == name:
                        # 获取表中已存在的行数
                        rows_old = worksheet.nrows
                        # 将xlrd对象拷贝转化为xlwt对象
                        new_workbook = copy(wb)
                        # 获取转化后的工作薄中的第i张表
                        new_worksheet = new_workbook.get_sheet(i)
                        for num in range(0, len(data[name])):
                            new_worksheet.write(rows_old, num, data[name][num])
                            new_workbook.save(f'{weizhi}【{year}年{month}月】.xls')


if __name__ == '__main__':
    t = TianQi()
    t.spider()

# import pandas as pd
# import jieba
# from pyecharts.charts import Scatter
# from pyecharts import options as opts
#
# from scipy import stats

# 读取数据
# df = pd.read_excel('海口历史天气【2023年11月】.xls')
#
# # 使用 jieba 处理数据，去除 "C"
# df['最高气温'] = df['最高气温'].apply(lambda x: ''.join(jieba.cut(x))).str.replace('℃', '').astype(float)
# df['最低气温'] = df['最低气温'].apply(lambda x: ''.join(jieba.cut(x))).str.replace('℃', '').astype(float)
#
# # 创建散点图
# scatter = Scatter()
# scatter.add_xaxis(df['最低气温'].tolist())
# scatter.add_yaxis("最高气温", df['最高气温'].tolist())
# scatter.set_global_opts(title_opts=opts.TitleOpts(title="最低气温与最高气温的散点图"))
# html_content = scatter.render_embed()
#
# # 计算回归方程
# slope, intercept, r_value, p_value, std_err = stats.linregress(df['最低气温'], df['最高气温'])
#
# print(f"回归方程为：y = {slope}x + {intercept}")
#
# analysis_text = f"回归方程为：y = {slope}x + {intercept}"
# # 生成HTML文件
# complete_html = f"""
# <html>
# <head>
#     <title>天气数据分析</title>
# </head>
# <body style="background-color: #e87f7f">
#     <div style='margin-top: 20px;background-color='#e87f7f''>
#         <div>{html_content}</div>
#         <p>{analysis_text}</p>
#     </div>
# </body>
# </html>
# """
# # 保存到HTML文件
# with open("海口历史天气【2023年11月】散点可视化.html", "w", encoding="utf-8") as file:
#     file.write(complete_html)

import pandas as pd
from flatbuffers.builder import np
from matplotlib import pyplot as plt
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType


def on(gender_counts):
    total = gender_counts.sum()
    percentages = {gender: count / total * 100 for gender, count in gender_counts.items()}
    analysis_parts = []
    for gender, percentage in percentages.items():
        analysis_parts.append(f"{gender}天气占比为{percentage:.2f}%，")
    analysis_report = "天气比例饼状图显示，" + ''.join(analysis_parts)
    return analysis_report


df = pd.read_excel("海口历史天气【2023年11月】.xls")
gender_counts = df['天气'].value_counts()
analysis_text = on(gender_counts)
pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS, bg_color='#e4cf8e'))
pie.add(
    series_name="海口市天气分布",
    data_pair=[list(z) for z in zip(gender_counts.index.tolist(), gender_counts.values.tolist())],
    radius=["40%", "70%"],
    rosetype="radius",
    label_opts=opts.LabelOpts(is_show=True, position="outside", font_size=14,
                              formatter="{a}<br/>{b}: {c} ({d}%)")
)
pie.set_global_opts(
    title_opts=opts.TitleOpts(title="海口市11月份天气分布", pos_right="50%"),
    legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    toolbox_opts=opts.ToolboxOpts(is_show=True)
)
pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
html_content = pie.render_embed()

# 生成HTML文件
complete_html = f"""
<html>
<head>
    <title>天气数据分析</title>

</head>
<body style="background-color: #e87f7f">
    <div style='margin-top: 20px;background-color='#e87f7f''>
        <div>{html_content}</div>
        <h3>分析报告：</h3>
        <p>{analysis_text}</p>
    </div>
</body>
</html>
"""

import pandas as pd
from matplotlib import font_manager
import jieba

# 中文字体
font_CN = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\STKAITI.TTF")

# 读取数据
df = pd.read_excel('海口历史天气【2023年11月】.xls')

# 使用 jieba 处理数据，去除 "C"
df['最高气温'] = df['最高气温'].apply(lambda x: ''.join(jieba.cut(x))).str.replace('℃', '').astype(float)
df['最低气温'] = df['最低气温'].apply(lambda x: ''.join(jieba.cut(x))).str.replace('℃', '').astype(float)
# 开始绘图
plt.figure(figsize=(20, 8), dpi=80)
max_tp = df['最高气温'].tolist()
min_tp = df['最低气温'].tolist()
x_day = range(1, 31)
# 绘制30天最高气温
plt.plot(x_day, max_tp, label="最高气温", color="red")
# 绘制30天最低气温
plt.plot(x_day, min_tp, label="最低气温", color="skyblue")
# 增加x轴刻度
_xtick_label = ["11月{}日".format(i) for i in x_day]
plt.xticks(x_day, _xtick_label, fontproperties=font_CN, rotation=45)
# 添加标题
plt.title("2023年11月最高气温与最低气温趋势", fontproperties=font_CN)
plt.xlabel("日期", fontproperties=font_CN)
plt.ylabel("温度（单位°C）", fontproperties=font_CN)
plt.legend(prop=font_CN)
plt.show()

from pyecharts.charts import WordCloud
from pyecharts import options as opts
from pyecharts.globals import SymbolType
import jieba
import pandas as pd
from collections import Counter

# 读取Excel文件
df = pd.read_excel('海口历史天气【2023年11月】.xls')
# 提取商品名
word_names = df["风向"].tolist() + df["天气"].tolist()
# 提取关键字
seg_list = [jieba.lcut(text) for text in word_names]
words = [word for seg in seg_list for word in seg if len(word) > 1]
word_counts = Counter(words)
word_cloud_data = [(word, count) for word, count in word_counts.items()]

# 创建词云图
wordcloud = (
    WordCloud(init_opts=opts.InitOpts(bg_color='#00FFFF'))
    .add("", word_cloud_data, word_size_range=[20, 100], shape=SymbolType.DIAMOND,
         word_gap=5, rotate_step=45,
         textstyle_opts=opts.TextStyleOpts(font_family='cursive', font_size=15))
    .set_global_opts(title_opts=opts.TitleOpts(title="天气预报词云图", pos_top="5%", pos_left="center"),
                     toolbox_opts=opts.ToolboxOpts(
                         is_show=True,
                         feature={
                             "saveAsImage": {},
                             "dataView": {},
                             "restore": {},
                             "refresh": {}
                         }
                     )

                     )
)

# 渲染词图到HTML文件
wordcloud.render("天气预报词云图.html")
