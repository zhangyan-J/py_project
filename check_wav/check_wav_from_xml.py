import os
import xml.etree.ElementTree as ET


# 定义函数来遍历目录并获取XML文件
def get_xml_files(xml_directory):
    xml_files = []
    for file_name in os.listdir(xml_directory):
        if file_name.endswith('.xml'):
            xml_files.append(os.path.join(xml_directory, file_name))
    print(xml_files)
    return xml_files


# 定义函数来获取XML文件中使用的WAV文件名列表：
def get_used_wav_filenames(xml_file):
    used_wav_filenames = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elem in root.iter():
        if elem.tag == 'wav':
            wav_filename = elem.text
            used_wav_filenames.append(wav_filename)
    print(used_wav_filenames)
    return used_wav_filenames


# 定义函数来读取指定路径下的WAV文件名列表：
def read_wav_filenames(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        wav_filenames = f.read().splitlines()
    print(wav_filenames)
    return wav_filenames


# 定义函数来对比两个WAV文件名列表：
def compare_wav_filenames(used_wav_filenames, specified_wav_filenames):
    common_filenames = set(used_wav_filenames) & set(specified_wav_filenames)
    return list(common_filenames)

# 调用上述函数来执行遍历和对比操作：
xml_directory = 'D:\\project\\py_project\\check_wav\\x-public'
specified_wav_file = 'D:\\project\\py_project\\check_wav\\audio\\wav_list.txt'
file_path = 'D:\\project\\py_project\\check_wav\\audio'
# specified_wav_file = '/path/to/specified_wav_file.txt'

xml_files = get_xml_files(xml_directory)
used_wav_filenames = get_used_wav_filenames(xml_files)
print(used_wav_filenames)
# specified_wav_filenames = read_wav_filenames(specified_wav_file)

common_filenames = compare_wav_filenames(used_wav_filenames, specified_wav_filenames)
