import openpyxl


def count_words_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

    except FileNotFoundError:
        print("文件不存在")
    else:
        while True:

            keyword = input("请输入要统计的关键字：")
            if keyword == 'q':
                break
            words = content.split(keyword)
            # 统计关键字数量
            word_count = len(words)
            print('文件中共有 {} 个关键字。'.format(word_count))


def count_words_excel(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        content = sheet.cell(row=1, column=1).value
    except FileNotFoundError:
        print("文件不存在")
    else:
        while True:

            keyword = input("请输入要统计的关键字：")
            if keyword == 'q':
                break
            words = content.split(keyword)
            # 统计关键字数量
            word_count = len(words)
            print('文件中共有 {} 个关键字。'.format(word_count))


def main():
    file_type = input("请输入文件类型（txt/excel）: ")
    if file_type == 'txt':
        count_words_txt(file_path)
    elif file_type == 'excel':
        count_words_excel(file_path)
    else:
        print("文件类型错误")


if __name__ == "__main__":
    main()

    # 调用函数并传入文件路径
    file_path = input("请输入文件路径：")
    count_words_txt(file_path)
    count_words_excel(file_path)

