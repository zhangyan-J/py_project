# import lxml
# import lxml.etree as ET
import os
#
#
# #
# def read_batfile(bat_path):
#     with open(bat_path, 'r') as file:
#         return file.read()
#
# #
# # # Example usage
# # bat_file = read_batfile(r'D:\project\py_project\replace_xml\demo.bat')
# # print(bat_file)
# # xml = read_xml(r'D:\project\py_project\replace_xml\input.xml')
# # print(xml)
# # # output = open(r'D:\project\py_project\replace_xml\output.xml', 'w')
# # # output.write(xml)
# # # # Output: <root><batfile>echo Hello World</batfile></root>
#
#
# import xml.etree.ElementTree as et
#
#
# # print(et.ElementTree(file=r'D:\project\py_project\replace_xml\input.xml'))
#
# # xml_path = et.ElementTree(file=r'D:\project\py_project\replace_xml\input.xml')
#
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
            new_file_list = []
            new_files = xml_files[-1].split('\\')[-1].split('.')[0]
            new_file_list.append(new_files)
            # print(type(new_file_list))
            # print( f"处理文件：{new_file_list}")
            return new_file_list
            # for file_name in new_files:
                # print(f"处理文件：{file_name}")
                # return file_name
                # print(f"处理文件：{file_name}")
folder_path = r'D:\project\py_project\filter_xml_file\x-public'
# #
xml_files_list = traverse_xml_files(folder_path)
# # print(f"文件数量：{len(xml_files_list)}")
print(xml_files_list)
#
#
# def get_root_name(file_path):
#     # file_path =r'D:\project\py_project\replace_xml\input.xml'
#     # tree = et.ElementTree(file=file_path)
#     tree = et.parse(file_path)
#     root = tree.getroot()
#
#     def traverse_element(element,depth=0):
#         ident = ' ' * depth
#         # print(f"{ident}Tag: {element.tag},Attribute: {element.attrib}")
#         for child in element:
#             traverse_element(child, depth + 1)
#
#     traverse_element(root)
#
#     for root_tag in root:
#         root_tag = root_tag.attrib['name']
#         # return root_tag
#         # root_tag = root.find('name')
#         return root_tag
#
# def main():
#     folder_path = r'D:\project\py_project\filter_xml_file\x-public'
#     file_extension = '.xml'
#
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith(file_extension):
#             file_path = os.path.join(folder_path, file_name)
#             title = get_root_name(file_path)
#             # get_root_name(file_path)
#
#             print(f"Title in xml_file of {file_name} is : {title}")
#
#             # file_name = f'{title}'
#             # print(f"Added filename to {file_name}")
#             # print(new_root_name)
#             # new_file_name = f'{new_root_name}.xml'
#
#
# if __name__ == '__main__':
#     main()

import os
import xml.etree.ElementTree as ET


def get_fun_name(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for tag in root:
        # print(tag.tag, tag.attrib, tag.text)
        # tag.attrib['function name'] = tag.text
        # return tag
        if tag.text is not None:
            return tag

file_path = r'D:\project\py_project\filter_xml_file\x-public\X_common_voice_wake_up.xml'


# def get_file_name():
#     for path in xml_files_list:
#         # if path is not None:
#         path = xml_files_list[0]
#         # print(path)
#         file_name = path.split('\\')[-1].split('.')[0]
#         return file_name
    # get_fun_name(path)



if __name__ == '__main__':
    # path = get_fun_name(file_path)
    # file_name = traverse_xml_files(folder_path)
    # print(file_name)
    get_fun_name(file_path)
    elem = get_fun_name(file_path).tag, get_fun_name(file_path).attrib,get_fun_name(file_path).text
    for key in elem[1].values():
        # print(key)
        # for xml_file_path in xml_files_list:
        #     get_fun_name(xml_file_path)
        if key is not None and key != file_name:
            key.replace(key,file_name)
    # print(get_fun_name(file_path))

