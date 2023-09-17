import csv
import sys
import pandas as pd

# input_file = sys.argv[1]#要在脚本后加入的参数，表示第一个参数
# output_file = sys.argv[2]#要在脚本后加入的参数，表示第二个参数
#
# file_read = pd.read_csv(input_file) #通过pandas的read_csv()方法读取csv文件的内容
# file_read.to_csv(output_file,index=False)#读取的内容通过to_csv()方法写入到output_file中

# file1 = 'D:\project\py_project\deal_with_csv\data.csv'
# file2 = 'D:\project\py_project\deal_with_csv\data2.csv'
#
# ##打开多个csv文件，将其中一个csv文件中内容写入到新的csv文件中
#
# with open(file1,'r',encoding='utf-8') as fp1, open(file2,'w',encoding='utf-8') as fp2:
#     for line in fp1:
#         fp2.write(line)

# csv_file = 'D:\project\py_project\deal_with_csv\data.csv'
# def parse_csv(csv_file,sep=',',header=False):
#     result = []
#     with open(csv_file,'r',encoding='utf-8') as fp:
#         #如果是True，那么可以跳过第一行
#         if header:
#             fp.readline()
#         for line in fp:
#             result.append(line.split(sep))
#         print(result)
#     return result
#
# parse_csv(csv_file)

# data = [
#     ['liming','12','taian'],
#     ['zhangsan','20','heze'],
#     ['lisi','18','shenzhen']
# ]
# output_file = 'D:\project\py_project\deal_with_csv/output.txt'
# def write_csv(data,oupput_file,sep=','):
#     with open(oupput_file,'w') as fp:
#         for line in data:
#             #使用sep将每一行的数据连接起来
#             #同时在最后加上\n来进行换行
#             fp.write(sep.join(line)+'\n')
#
#
# write_csv(data,output_file)
# df = pd.DataFrame(data)
# df.to_csv(output_file,header=None,index=None)
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 这里保险的就是直接先把绝对路径加入到搜索路径
sys.path.insert(0, os.path.join(BASE_DIR))
sys.path.insert(0,os.path.join(BASE_DIR))
sys.path.insert(0,os.path.join(BASE_DIR,'deal_with_csv'))# 把data所在的绝对路径加入到了搜索路径，这样也可以直接访问dataset.csv文件了
# 这句代码进行切换目录
os.chdir(BASE_DIR) # 把目录切换到当前项目，这句话是关键

print(os.getcwd())# 这样就能看到目前Python搜索路径在哪里，如果报错找不到，多半是你这个路径下没有文件
# l = []
# with open('data.csv','rt',encoding='utf-8') as f:
#     cr = csv.reader(f)
#     for row in cr:
#         print(row)
#         l.append(row)
# with open('./test1.csv','wt',encoding='utf-8') as fw:
#     cw = csv.writer(fw)
#     ##采用writerow()方法
#     for item in l:
#         cw.writerow(item)#将列表的每个元素写道csv文件的一行
    #或采用writerows()方法
    # cw.writerows(l)#将嵌套列表内容写入csv文件，每个外层元素为一行，每个内层元素为一个数据

l = []
with open('test1.csv','rt',encoding='utf-8') as f:
    cr = csv.DictReader(f)
    for row in cr:
        # print(row)
        l.append(row) #将test2.csv内容读入列表l，每行为其一个元素，元素为dict
                     #key为标题（未指定时为读取的第一行），value为对应列的数据
