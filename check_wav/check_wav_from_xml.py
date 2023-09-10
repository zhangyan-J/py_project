import os
import glob
import re

# 匹配文件夹下的所有 XML 文件
folder_path = 'D:\project\py_project\check_wav\\x-public'


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

    return xml_files


xml_files_list = traverse_xml_files(folder_path)
print(xml_files_list)
# file_path = './output.txt'
# # 打开文件以写入模式，并逐行写入列表元素
# with open(file_path, 'w') as file:
#     for item in xml_files_list:
#         file.write(item + '\n')
# 在循环之外遍历 XML 文件列表
wav_list = []
for xml_file_path in xml_files_list:
    # print("处理文件：", xml_file_path)
    # 在这里对每个 XML 文件进行操作
    with open(xml_file_path, 'r', encoding='utf-8') as xml_file:
        xml_content = xml_file.read()
        pattern = r'<param name="path">(.*?)</param>'
        # pattern = '<param name="audio_name">(.*?)</param>'  ##问题所在，匹配的正则表达式不正确，下一个问题是然后匹配多个正则表达[2023.09.07]
        # 使用正则表达式进行匹配
        matches = re.findall(pattern, xml_content)
        for match in matches:
            print(match)
            wav_list.append(match)
# 匹配文件夹下的所有 WAV 文件
wav_path = 'D:\project\py_project\check_wav\\audio'
# # 打印生成的 WAV 文件列表
print("------音频库--WAV--文件列表: ----------")


def get_wav_list(wav_path):
    wav_files = glob.glob(wav_path + '/*.wav')
    wav_lists = []
    # print(wav_files)
    for wav_file in wav_files:
        # print(wav_file)
        wav = wav_file.split('\\')
        # print(wav)
        wav_list = wav[-1]
        # print(wav_list)
        wav_lists.append(wav_list)
    # print(wav_lists)
    return wav_lists  ##函数中利用return返回列表，并且注意缩进，否则只打印一个元素


listb = get_wav_list(wav_path)


# 定义函数来对比两个WAV文件名列表：
def compare_wav_filenames(wav_list, listb):
    for i in wav_list:
        if i in listb:
            print(f'音频:{i} 在 音频库-WAV文件列表中存在')


compare_wav_filenames(wav_list, listb)
