import pandas as pd


def count_words_txt(file_path, keyword):
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
        df = pd.read_excel(file_path, engine=engine)
        content = df.to_string()
        # 遍历DataFrame中的每个单元格
        for index, row in df.iterrows():
            # print(f"正在检查第 {index} 行")
            for col_index, column_value in row.items():
                if keyword in str(column_value):
                    print(f"找到关键字 '{keyword}' 在第 {index + 2} 行 {col_index} 列")
        if isinstance(keyword, str):
            words = content.split(keyword)
            # 统计关键字数量
            word_count = len(words)
            return word_count
        else:
            print("关键字类型错误")
            return None


def main():
    file_type = input("请输入文件类型（txt/excel）: ")
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
            print('文件中共有 {} 个关键字。'.format(count), )
        else:
            print("关键字类型错误")
    else:
        print("文件类型错误")


if __name__ == "__main__":
    while True:
        main()
        choice = input("是否继续？(y/n): ")
        if choice.lower() == 'n':
            break
