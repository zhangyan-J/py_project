import pandas as pd
import logging
import time
import os
import warnings
warnings.filterwarnings('ignore')

# current_dir = os.path.dirname(os.path.abspath(__file__))
# current_dir = os.path.abspath(os.path.dirname(__file__))
current_dir = os.getcwd()
print(current_dir)
log_dir = os.path.join(current_dir, "logs")
if not os.path.exists(log_dir):
    os.mkdir(log_dir)


class Debugger:
    def __init__(self, log_file):

        if not os.path.exists(log_file):
            os.system(r"touch {}".format(log_file))
        # 创建一个日志器
        logger = logging.getLogger("logger")
        # 设置日志输出的最低等级,低于当前等级则会被忽略
        logger.setLevel(logging.INFO)
        # 创建处理器：sh为控制台处理器，fh为文件处理器
        sh = logging.StreamHandler()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        log_file = os.path.join(log_dir, "check_word_info.log")
        fh = logging.FileHandler(log_file, encoding="UTF-8")
        # 创建格式器,并将sh，fh设置对应的格式
        formator = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                     datefmt="%Y/%m/%d %X")
        sh.setFormatter(formator)
        fh.setFormatter(formator)
        # 将处理器，添加至日志器中
        logger.addHandler(sh)
        logger.addHandler(fh)
        # file_handler = logging.FileHandler(log_file)
        # file_handler.setFormatter(formatter)
        # self.logger.addHandler(file_handler)

    # def count_words_excel(self, file_path, keyword):
    #     pass


def count_words_txt(self, file_path, keyword):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                print("文件为空")
                return None

    except FileNotFoundError:
        print("文件不存在")
        return None

    else:
        if isinstance(keyword, str):
            words = content.split(keyword)
            # 统计关键字数量
            word_count = len(words)
            return word_count
        else:
            print("关键字类型错误")
            return None


def count_words_excel(file_path, keyword):
    # log().info(f"正在检查文件：{file_path}")
    global all_sheets
    try:
        if file_path.endswith('.xls'):
            engine = 'xlrd'

        elif file_path.endswith('.xlsx'):
            engine = 'openpyxl'

        else:
            raise ValueError("Unsupported file format")

    except FileNotFoundError:
        print("文件不存在")
        return None

    else:
        # 【实例】：遍历DataFrame中的每个单元格
        # for index, row in df.iterrows():
        #     # print(f"正在检查第 {index} 行")
        #     for col_index, column_value in row.items():
        #         if keyword in str(column_value):
        #             print(f"找到关键字 '{keyword}' 在第 {index + 2} 行 {col_index} 列")

        excel_file = pd.ExcelFile(file_path)
        sheet_names = excel_file.sheet_names

        for sheet_name in sheet_names:
            all_sheets = pd.read_excel(file_path, sheet_name=sheet_name)
            # print(all_sheets)
            for col_name, sheet_data in all_sheets.items():
                # print(f'col_name: {col_name}')
                # print(type(sheet_data))
                # print('\n')
                sd = sheet_data.to_frame()
                for index, row in sd.iterrows():
                    # print(index)
                    for col_index, column_value in row.items():
                        # print(col_index)
                        # print(type(column_value))
                        if str(keyword) in str(column_value):
                            print(f"找到关键字 '{keyword}' 在{sheet_name}，在第 {index + 2} 行 {col_index} 列")
        content = all_sheets.to_string()
        if isinstance(keyword, str):
            words = content.split(keyword)
            # 统计关键字数量
            word_count = len(words)
            return word_count
        else:
            print("关键字类型错误")
            return None


def main(log_file=None):
    file_tp = input("请输入文件类型（txt/excel）: ")
    file_type = file_tp.lower()
    if file_type == 'txt':
        file_path = input("请输入文件路径：")
        keyword = input("请输入要统计的关键字：")
        count = count_words_txt(file_path, keyword)
        if count is not None:
            print('文件中共有 {} 个关键字。'.format(count))
        else:
            print("关键字类型错误")
    elif file_type == 'excel':
        file_path = input(r"请输入文件路径：")
        # file_path = r'D:\project\py_project\豆瓣电影Top250.xls'
        keyword = input("请输入要统计的关键字：")
        count = count_words_excel(file_path, keyword)
        if count is not None:
            print('文件中共有 {} 个关键字。'.format(count))
        else:
            print("关键字类型错误")
    else:
        print("文件类型错误")

    def debug(self, message):
        self.logger.debug(message)


if __name__ == "__main__":
    while True:
        main()
        choice = input("是否继续？(y/n): ")
        if choice.lower() == 'n':
            break
