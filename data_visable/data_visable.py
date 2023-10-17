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
