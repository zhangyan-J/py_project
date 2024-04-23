import os
import glob
import re

# 匹配文件夹下的所有 XML 文件
folder_path = r'D:\GIT\AutomationTest\Project\SS全平台\Public\Scripts\Function_Script\语音'


# 递归遍历目录下的所有 XML 文件
def traverse_xml_files(folder_path):
    # global xml_files
    xml_files = []
    for root, dirs, files in os.walk(folder_path):
        files[:] = [f for f in files if f.endswith(".xml")]
        # print(files)
        for file in files:
            xml_file_path = os.path.join(root, file)
            # print( f"处理文件：{xml_file_path}" )
            xml_files.append(xml_file_path)
            # print(xml_files)
            # print(len(xml_files))

    with open(r'D:\practice\github\py_project\filter_xml_file\output.txt', 'w', encoding='utf-8') as file:
        [file.write(str(xml_file_path) + '\n') for xml_file_path in xml_files]  ##将list(列表)保存为txt文件自动换行
        file.close()
    return xml_files


xml_files_list = traverse_xml_files(folder_path)

def map_xml(xml_files_list):
    fun_list = []
    # 遍历 XML 文件列表
    for xml_file_path in xml_files_list:
        # print("处理文件：", xml_file_path)
        # 在这里对每个 XML 文件进行操作
        with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
            xml_content = xml_file.read()
            # pattern = r'<param name="path">(.*?)</param>'
            pattern = r'<callFunction name="([^<>]*)">'
            matches = re.findall(pattern, xml_content)
            for match in matches:
                # print(match)
                fun_list.append(match)
    with open(r'D:\practice\github\py_project\filter_xml_file\fun_list.txt', 'w', encoding='utf-8') as file:
        [file.write(str(match) + '\n') for match in fun_list]  ##将list(列表)保存为txt文件自动换行
        ##去重
        old_list = fun_list
        new_list = list(dict.fromkeys(old_list))
        [file.write(str(match) + '\n') for match in new_list]  ##将list(列表)保存为txt文件自动换行

        file.close()
    return fun_list


map_xml(xml_files_list)
# print(xml_files_list)
# file_path = './output.txt'
# # 打开文件以写入模式，并逐行写入列表元素
# with open(file_path, 'w') as file:
#     for item in xml_files_list:
#         file.write(item + '\n')
# 在循环之外遍历 XML 文件列表
# assert_list = []
# for xml_file_path in xml_files_list:
#     # print("处理文件：", xml_file_path)
#     # 在这里对每个 XML 文件进行操作
#     with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
#         xml_content = xml_file.read()
#         # pattern = r'<param name="path">(.*?)</param>'
#         pattern = r'<param name="expected">([^<>]*)</param>'
#         # pattern = '<param name="audio_name">(.*?)</param>'  ##问题所在，匹配的正则表达式不正确，下一个问题是然后匹配多个正则表达[2023.09.07]
#         # 使用正则表达式进行匹配
#         matches = re.findall(pattern, xml_content)
#         for match in matches:
#             # print(match)
#             assert_list.append(match)
#
# # print(assert_list)
# print("------音频库--WAV--文件列表: ----------")
#
#
#
# old_list = assert_list
# new_list = list(dict.fromkeys(old_list))
# print(new_list) # [2, 3, 4, 5, 1]
#
# with open('D:\Practice\github\py_project\\filter_xml_file\\asser_list.txt','w',encoding='utf-8') as f:
#     for line in new_list:
#         # print(line)
#         f.write(line+'\n')
