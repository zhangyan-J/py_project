import openpyxl


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
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        content = ""
        for row in sheet.iter_rows():
            for cell in row:
                content += cell.value
                print(content)
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
        file_path = input("请输入文件路径：")
        keyword = input("请输入要统计的关键字：")
        count = count_words_excel(file_path, keyword)
        if count is not None:
            print('文件中共有 {} 个关键字。'.format(count))
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

