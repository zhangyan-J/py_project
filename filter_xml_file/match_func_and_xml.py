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
        file.close()
    # 去除重复元素

    new_fun_list = list(set(fun_list))
    with open(r'D:\practice\github\py_project\filter_xml_file\new_fun_list.txt', 'w', encoding='utf-8') as file:
        [file.write(str(fun) + '\n') for fun in new_fun_list]  ##将list(列表)保存为txt文件自动换行
        # file.write('\n'.join(new_fun_list))
        # print(new_fun_list)
        file.close()
    # print(type(fun_list))
    # new_fun_list = list({}.fromkeys(fun_list).keys())
    return new_fun_list


map_xml(xml_files_list)

folder_path = r'D:\GIT\AutomationTest\Project\SS全平台\Public\Script_Resource\Functions'
def check_dict_xml(folder_path):

    file_names = []
    for root, dirs, files in os.walk(folder_path):
        files[:] = [f for f in files if f.endswith(".xml")]
        # print(files)
        for file in files:
            xml_file_path = os.path.join(root, file)
            # print( f"处理文件：{xml_file_path}" )
            file_names.append(xml_file_path)
            # print(xml_files)
    fun_names = []
    for fun_name in file_names:
        fun_name_before = fun_name.split('\\')[-1]
        last_fun_name = fun_name_before.split('.')[0]
        fun_names.append(last_fun_name)
        print(fun_names)
    # 读取字典文件
    with open(r'D:\practice\github\py_project\filter_xml_file\fun_names.txt', 'w', encoding='utf-8') as file:
        [file.write(str(fun_name) + '\n') for fun_name in fun_names]
        # file.write('\n'.join(fun_names))
        file.close()
    # return name


check_dict_xml(folder_path)
# old_list = assert_list
# new_list = list(dict.fromkeys(old_list))
# print(new_list) # [2, 3, 4, 5, 1]
#
# with open('D:\Practice\github\py_project\\filter_xml_file\\asser_list.txt','w',encoding='utf-8') as f:
#     for line in new_list:
#         # print(line)
#         f.write(line+'\n')
