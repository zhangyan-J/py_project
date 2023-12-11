import time

import pyecharts
# # print(pyecharts.__version__)
# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis(["衬衫","羊毛衫",'雪纺裤','裤子','高跟鞋','袜子'])
# bar.add_yaxis("商家A",[5,20,36,10,75,90])
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# # bar.render('D:\project\py_project\data_visable\mycharts.html')
#
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# bar.render()

from pyecharts.charts import Bar
from pyecharts import options as opts

#V1 版本开始支持链式调用
#你所看到的格式其实是‘black’ 格式化以后的效果
# 可以执行‘pip install black’下载使用

# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
#     .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
#     # 或者直接使用字典参数
#     # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
# )
# bar.render('D:\project\py_project\data_visable\mycharts.html')
###渲染成图片文件，这部分内容请参考 进阶话题-渲染图片
# from pyecharts.charts import Bar
# from pyecharts.render import make_snapshot
#
# #使用 snapshot-selenium 渲染图片
# from snapshot_selenium import snapshot
#
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# )
# make_snapshot(snapshot,bar.render(),'bar.png')

###使用主题
from pyecharts.charts import Bar
from pyecharts import options as opts
##内置主题类型可以查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
)
bar.render('D:\project\py_project\data_visable\mycharts.html')
####Note:在使用pandas或者Numpy时，确保将数值类型转换成为python原生的int/float。比如整数类型请确保为int，而不是numpy.int32

###使用Notebook
# import random
# import datetime
#
# import pyecharts.options as opts
# from pyecharts.charts import Calendar
#
#
# begin = datetime.date(2017, 1, 1)
# end = datetime.date(2017, 12, 31)
# data = [
#     [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
#     for i in range((end - begin).days + 1)
# ]
#
# (
#     Calendar()
#     .add(
#         series_name="",
#         yaxis_data=data,
#         calendar_opts=opts.CalendarOpts(
#             pos_top="120",
#             pos_left="30",
#             pos_right="30",
#             range_="2017",
#             yearlabel_opts=opts.CalendarYearLabelOpts(is_show=False),
#         ),
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(pos_top="30", pos_left="center", title="2017年步数情况"),
#         visualmap_opts=opts.VisualMapOpts(
#             max_=20000, min_=500, orient="horizontal", is_piecewise=False
#         ),
#     )
#     .render("calendar_heatmap.html")
# )


# import pyecharts.options as opts
# from pyecharts.charts import Bar3D
#
# """
# Gallery 使用 pyecharts 1.1.0
# 参考地址: https://echarts.apache.org/examples/editor.html?c=bar3d-punch-card&gl=1
#
# 目前无法实现的功能:
#
# 1、光照和阴影暂时无法设置
# """
#
# hours = [
#     "12a",
#     "1a",
#     "2a",
#     "3a",
#     "4a",
#     "5a",
#     "6a",
#     "7a",
#     "8a",
#     "9a",
#     "10a",
#     "11a",
#     "12p",
#     "1p",
#     "2p",
#     "3p",
#     "4p",
#     "5p",
#     "6p",
#     "7p",
#     "8p",
#     "9p",
#     "10p",
#     "11p",
# ]
# days = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
#
# data = [
#     [0, 0, 5],
#     [0, 1, 1],
#     [0, 2, 0],
#     [0, 3, 0],
#     [0, 4, 0],
#     [0, 5, 0],
#     [0, 6, 0],
#     [0, 7, 0],
#     [0, 8, 0],
#     [0, 9, 0],
#     [0, 10, 0],
#     [0, 11, 2],
#     [0, 12, 4],
#     [0, 13, 1],
#     [0, 14, 1],
#     [0, 15, 3],
#     [0, 16, 4],
#     [0, 17, 6],
#     [0, 18, 4],
#     [0, 19, 4],
#     [0, 20, 3],
#     [0, 21, 3],
#     [0, 22, 2],
#     [0, 23, 5],
#     [1, 0, 7],
#     [1, 1, 0],
#     [1, 2, 0],
#     [1, 3, 0],
#     [1, 4, 0],
#     [1, 5, 0],
#     [1, 6, 0],
#     [1, 7, 0],
#     [1, 8, 0],
#     [1, 9, 0],
#     [1, 10, 5],
#     [1, 11, 2],
#     [1, 12, 2],
#     [1, 13, 6],
#     [1, 14, 9],
#     [1, 15, 11],
#     [1, 16, 6],
#     [1, 17, 7],
#     [1, 18, 8],
#     [1, 19, 12],
#     [1, 20, 5],
#     [1, 21, 5],
#     [1, 22, 7],
#     [1, 23, 2],
#     [2, 0, 1],
#     [2, 1, 1],
#     [2, 2, 0],
#     [2, 3, 0],
#     [2, 4, 0],
#     [2, 5, 0],
#     [2, 6, 0],
#     [2, 7, 0],
#     [2, 8, 0],
#     [2, 9, 0],
#     [2, 10, 3],
#     [2, 11, 2],
#     [2, 12, 1],
#     [2, 13, 9],
#     [2, 14, 8],
#     [2, 15, 10],
#     [2, 16, 6],
#     [2, 17, 5],
#     [2, 18, 5],
#     [2, 19, 5],
#     [2, 20, 7],
#     [2, 21, 4],
#     [2, 22, 2],
#     [2, 23, 4],
#     [3, 0, 7],
#     [3, 1, 3],
#     [3, 2, 0],
#     [3, 3, 0],
#     [3, 4, 0],
#     [3, 5, 0],
#     [3, 6, 0],
#     [3, 7, 0],
#     [3, 8, 1],
#     [3, 9, 0],
#     [3, 10, 5],
#     [3, 11, 4],
#     [3, 12, 7],
#     [3, 13, 14],
#     [3, 14, 13],
#     [3, 15, 12],
#     [3, 16, 9],
#     [3, 17, 5],
#     [3, 18, 5],
#     [3, 19, 10],
#     [3, 20, 6],
#     [3, 21, 4],
#     [3, 22, 4],
#     [3, 23, 1],
#     [4, 0, 1],
#     [4, 1, 3],
#     [4, 2, 0],
#     [4, 3, 0],
#     [4, 4, 0],
#     [4, 5, 1],
#     [4, 6, 0],
#     [4, 7, 0],
#     [4, 8, 0],
#     [4, 9, 2],
#     [4, 10, 4],
#     [4, 11, 4],
#     [4, 12, 2],
#     [4, 13, 4],
#     [4, 14, 4],
#     [4, 15, 14],
#     [4, 16, 12],
#     [4, 17, 1],
#     [4, 18, 8],
#     [4, 19, 5],
#     [4, 20, 3],
#     [4, 21, 7],
#     [4, 22, 3],
#     [4, 23, 0],
#     [5, 0, 2],
#     [5, 1, 1],
#     [5, 2, 0],
#     [5, 3, 3],
#     [5, 4, 0],
#     [5, 5, 0],
#     [5, 6, 0],
#     [5, 7, 0],
#     [5, 8, 2],
#     [5, 9, 0],
#     [5, 10, 4],
#     [5, 11, 1],
#     [5, 12, 5],
#     [5, 13, 10],
#     [5, 14, 5],
#     [5, 15, 7],
#     [5, 16, 11],
#     [5, 17, 6],
#     [5, 18, 0],
#     [5, 19, 5],
#     [5, 20, 3],
#     [5, 21, 4],
#     [5, 22, 2],
#     [5, 23, 0],
#     [6, 0, 1],
#     [6, 1, 0],
#     [6, 2, 0],
#     [6, 3, 0],
#     [6, 4, 0],
#     [6, 5, 0],
#     [6, 6, 0],
#     [6, 7, 0],
#     [6, 8, 0],
#     [6, 9, 0],
#     [6, 10, 1],
#     [6, 11, 0],
#     [6, 12, 2],
#     [6, 13, 1],
#     [6, 14, 3],
#     [6, 15, 4],
#     [6, 16, 0],
#     [6, 17, 0],
#     [6, 18, 0],
#     [6, 19, 0],
#     [6, 20, 1],
#     [6, 21, 2],
#     [6, 22, 2],
#     [6, 23, 6],
# ]
# data = [[d[1], d[0], d[2]] for d in data]
#
#
# (
#     Bar3D()
#     .add(
#         series_name="",
#         data=data,
#         xaxis3d_opts=opts.Axis3DOpts(type_="category", data=hours),
#         yaxis3d_opts=opts.Axis3DOpts(type_="category", data=days),
#         zaxis3d_opts=opts.Axis3DOpts(type_="value"),
#     )
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(
#             max_=20,
#             range_color=[
#                 "#313695",
#                 "#4575b4",
#                 "#74add1",
#                 "#abd9e9",
#                 "#e0f3f8",
#                 "#ffffbf",
#                 "#fee090",
#                 "#fdae61",
#                 "#f46d43",
#                 "#d73027",
#                 "#a50026",
#             ],
#         )
#     )
#     .render("bar3d_punch_card.html")
# )

#
# from pyecharts import options as opts
# from pyecharts.charts import Pie
#
# c = (
#     Pie()
#     .add_dataset(
#         source=[
#             ["product", "2012", "2013", "2014", "2015", "2016", "2017"],
#             ["Matcha Latte", 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
#             ["Milk Tea", 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
#             ["Cheese Cocoa", 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
#             ["Walnut Brownie", 55.2, 67.1, 69.2, 72.4, 53.9, 39.1],
#             ["Black Tea", 34.5, 23.6, 56.7, 67.9, 26.3, 65.8]
#         ]
#     )
#     .add(
#         series_name="Matcha Latte",
#         data_pair=[],
#         radius=60,
#         center=["25%", "30%"],
#         encode={"itemName": "product", "value": "2012"},
#     )
#     .add(
#         series_name="Milk Tea",
#         data_pair=[],
#         radius=60,
#         center=["75%", "30%"],
#         encode={"itemName": "product", "value": "2013"},
#     )
#     .add(
#         series_name="Cheese Cocoa",
#         data_pair=[],
#         radius=60,
#         center=["25%", "75%"],
#         encode={"itemName": "product", "value": "2014"},
#     )
#     .add(
#         series_name="Walnut Brownie",
#         data_pair=[],
#         radius=60,
#         center=["75%", "75%"],
#         encode={"itemName": "product", "value": "2015"},
#     )
#     .add(
#         series_name="Black Tes",
#         data_pair=[],
#         radius=60,
#         center=["56%", "25%"],
#         encode={"itemName": "product", "value": "2016"},
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="Dataset simple pie example"),
#         legend_opts=opts.LegendOpts(pos_left="30%", pos_top="2%"),
#     )
#     .render("dataset_pie.html")
# )


def add(a:int,b:int):
    return a+b
def test_answer():
    assert add(3,4) == 7




