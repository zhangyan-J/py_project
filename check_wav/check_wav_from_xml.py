import os
import glob
import re

# 匹配文件夹下的所有 XML 文件
folder_path = 'D:\project\py_project\check_wav\\x-public'


# 递归遍历目录下的所有 XML 文件
def traverse_xml_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        files[:] = [f for f in files if f.endswith(".xml")]
        # print(files)
        for file in files:
            # print(os.path.join(root, file))
            # if file.endswith('xml'):
            xml_file_path = os.path.join(root, file)
            print(f"处理文件：{xml_file_path}")

            # 遍历所有文件中的所有行
            with open(xml_file_path, 'r', encoding='utf-8') as fin:
                xml_content = fin.read()
                pattern = r'<param name="path">(.*?)</param>'
                # 使用正则表达式进行匹配
                matches = re.findall(pattern, xml_content)
                # 打印匹配结果
                for match in matches:
                    print(match)
                return matches


# 调用递归函数
lista = traverse_xml_files(folder_path)
print(lista)

# 匹配文件夹下的所有 WAV 文件
wav_path = 'D:\\project\\py_project\\check_wav\\audio'
# print(wav_files)
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
# print(f'------{listb}------')

# 定义函数来对比两个WAV文件名列表：
def compare_wav_filenames(lista, listb):
    for i in lista:
        if i in listb:
            print(f'音频:{i} 在 音频库-WAV文件列表中存在')
        else:
            print(f'音频:{i} 在 音频库-WAV文件列表中不存在')

compare_wav_filenames(lista,listb)

