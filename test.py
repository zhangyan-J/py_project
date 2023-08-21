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
import numpy as np
import math
import matplotlib.pyplot as plt

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
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
x_values= list(range(1,1001))
y_values= [x ** 2 for x in x_values]

plt.scatter(x_values,y_values,s=40,edgecolors='none',linewidths=5)
# ##设置图标标题并给坐标轴指定标签
plt.title("Square Numbers",fontsize=12)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Square of Value",fontsize=12)


##设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()

