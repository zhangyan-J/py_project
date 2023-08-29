import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from random_walk import RandomWalk
###下文一直报no module named randomwalk，通过添加PYTHONPATH到系统环境变量，如何重启pycharm解决
### 解决链接：https://blog.csdn.net/NeverLate_gogogo/article/details/107615838

while True:
    # 构建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.BrBG_r, edgecolor='none', s=8)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=100)

    # 隐藏坐标轴
    frame = plt.gca()
    # frame.axes.get_xaxis().set_visable(False)##此处按照视频的弹幕提示改了之后就可以运行起来了
    # frame.axes.get_yaxis().set_visable(False)

    ##书上的内容
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visable(False)

    plt.show()
    # plt.savefig("Squares_plot.png", bbox_inches='tight')

    keep_running = input("Make another walk?(y/n):")  # 多画几次
    if keep_running == 'n':
        break
