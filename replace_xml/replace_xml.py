import os
import xml.etree.ElementTree as ET

#
# # 指定目录路径
directory_path = r"D:\practice\github\py_project\test_xml_file"
# directory_path = r"D:\project\py_project\test_xml_file"


def get_xml_file_path(directory):
    file_paths = []
    # 遍历目录下的所有文件
    for root, dirs, files in os.walk(directory):
        files[:] = [f for f in files if f.endswith(".xml")]
        for file in files:
            xml_file_path = os.path.join(root, file)
            # print( f"处理文件：{xml_file_path}" )
            file_paths.append(xml_file_path)
    return file_paths


xml_paths = get_xml_file_path(directory_path)
# print(xml_paths)


def get_xml_file_name(directory):
    file_names = []
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):  # 只处理XML文件
            xml_file = os.path.join(directory, filename)
            # print(xml_file)
            file_name_without_extension = xml_file.split('\\')[-1].split('.')[0]
            # print(file_name_without_extension)
            file_names.append(file_name_without_extension)
    return file_names


# # 调用函数
file_names = get_xml_file_name(directory_path)


# print(file_names)


def check_xml_filename(xml_file):
    # 获取文件名
    file_name = os.path.splitext(os.path.basename(xml_file))[0]
    return file_name


def main():
    # 读取XML文件
    xml_files = get_xml_file_path(directory_path)
    for xml_file in xml_files:
        # print(f"处理文件：{xml_file}")
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # # 获取function的name属性：即function名称
        fun_name = root[0].attrib["name"]
        print(fun_name)
        file_name = check_xml_filename(xml_file)
        # print(file_name)
        if root[0].attrib["name"] != file_name:
            print(root[0].attrib["name"])
            root[0].attrib["name"] = file_name
        # 遍历XML元素，检查文件名和属性名是否一致
        # for elem in root.iter():
        #     check_xml_filename(xml_file)

        # 保存更改后的XML文件
        tree.write(xml_file)


if __name__ == "__main__":
    main()
