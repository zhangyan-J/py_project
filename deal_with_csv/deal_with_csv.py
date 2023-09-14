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

data = [
    ['liming','12','taian'],
    ['zhangsan','20','heze'],
    ['lisi','18','shenzhen']
]
output_file = '././output.txt'
def write_csv(data,oupput_file,sep=','):
    with open(oupput_file,'w') as fp:
        for line in data:
            #使用sep将每一行的数据连接起来
            #同时在最后加上\n来进行换行
            fp.write(sep.join(line)+'\n')

write_csv(data,output_file)