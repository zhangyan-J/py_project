# #
#
#
# import os
# import xml.etree.ElementTree as ET
#
# # 指定目录路径
# directory_path = r"D:\project\py_project\replace_xml\x-public"
#
#
# def get_xml_file_name(directory):
#     file_names = []
#     # 遍历目录下的所有文件
#     for filename in os.listdir(directory):
#         if filename.endswith(".xml"):  # 只处理XML文件
#             xml_file = os.path.join(directory, filename)
#             # print(xml_file)
#             file_name_without_extension = xml_file.split('\\')[-1].split('.')[0]
#             # print(file_name_without_extension)
#             file_names.append(file_name_without_extension)
#     return file_names
#
#
# # 调用函数
# replacement_values = get_xml_file_name(directory_path)
# print(replacement_values)
# #
# # # print(pxf)
# #
# #
# # def parase_xml_file():
# #     attribute_names = []
# #     for file_name in replacement_values:
# #         xml_file = os.path.join(directory_path, file_name + ".xml")
# #         # print(xml_file)
# #         # 解析XML文件
# #         tree = ET.parse(xml_file)
# #         root = tree.getroot()
# #         for tag in root:
# #             attribute_names.append(tag.attrib['name'])
# #     return attribute_names
# #
# #
# # attribute_name = parase_xml_file()
# #
# #
# # # print(attribute_names)
# #
# # def replace_attribute_in_xml(file_path, values):
# #     # 解析 XML 文件
# #     tree = ET.parse(file_path)
# #     root = tree.getroot()
# #     el = root.iter()
# #     # print(root.attrib)
# #     # 获取所有要替换的标签
# #     elements = list(root.iter())
# #     # print(elements)
# #     # print(elements)
# #     # 确保有足够的值进行替换
# #     num_elements = len(elements)
# #     num_values = len(values)
# #     # # print(num_elements,num_values)
# #     # if num_values < num_elements:
# #     #     raise ValueError("Replacement values list is too short for the number of XML elements")
# #
# #     # 替换指定属性的值
# #     for i, elem in enumerate(elements):
# #         if replacement_values not in elem.attrib:
# #             # print(attribute_name)
# #             elem.attrib[attribute_name] = values[i % replacement_values]
# #
# #     # 保存修改后的 XML 文件
# #     tree.write(file_path, encoding='utf-8', xml_declaration=True)
# #
# #
# # # 批量处理目录中的所有 XML 文件
# # for filename in os.listdir(directory_path):
# #     if filename.endswith('.xml'):
# #         file_path = os.path.join(directory_path, filename)
# #         replace_attribute_in_xml(file_path, replacement_values)
# #
# # replace_attribute_in_xml()
# # print("所有 XML 文件已处理。")


import os
import xml.etree.ElementTree as ET


def check_xml_filename(xml_file):
    # 获取文件名
    file_name = os.path.splitext(os.path.basename(xml_file))[0]
    return file_name
    # 检查文件名和属性名是否一致
    # if file_name != root[0].attrib["name"]:  # 如果不一致，将属性名改为文件名
    #     root[0].attrib["name"] = file_name
    # print(f"属性名已更改为：{file_name}")

def main():
    # 读取XML文件
    xml_file = r"D:\project\py_project\replace_xml\x-public\netease_delete_music.xml"
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # # 获取function的name属性：即function名称
    # # fun_name = root[0].attrib["name"]
    # # print(fun_name)
    file_name = check_xml_filename(xml_file)
    if root[0].attrib["name"] != file_name:
        root[0].attrib["name"] = file_name
    # 遍历XML元素，检查文件名和属性名是否一致
    for elem in root.iter():
        check_xml_filename(xml_file)

    # 保存更改后的XML文件
    tree.write(xml_file)


if __name__ == "__main__":
    main()
