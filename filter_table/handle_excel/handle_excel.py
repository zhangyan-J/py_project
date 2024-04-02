import pandas as pd
import os
import xlwt

if __name__ == '__main__':

    # file_path = r"D:\project\py_project/语音.xlsx"
    file_path = input('请输入待处理文件路径：')
    print(file_path)
    # if file_path.endswith(".xlsx"):
    #     file_path = file_path[:-1]
    # # elif file_path.endswith(".xls"):
    # else:
    #     file_path = file_path[:-1]
    #     print(file_path)
    df = pd.read_excel(file_path)
    valid_names = []
    invalid_names = []

    index = 0
    while index < len(df):
        # print(index)
        value = df.iloc[index, 0]
        # print(value)
        if str(value).startswith("语音_"):
            next_index = index + 1
            while next_index < len(df) and not df.iloc[next_index, 0].startswith("语音_"):
                next_index += 1

            if next_index - index > 2:
                valid_names.append(value)
            else:
                invalid_names.append(value)

            index = next_index
        else:
            index += 1
    try:
        with pd.ExcelWriter(file_path, engine="openpyxl", mode='a') as writer:
            pd.DataFrame(valid_names, columns=["有效数据"]).to_excel(writer, sheet_name="有效数据", index=False)
            pd.DataFrame(invalid_names, columns=["无效数据"]).to_excel(writer, sheet_name="无效数据", index=False)
    # except ValueError:
        # 如果文件中已经包含有效数据和无效数据，则直接保存
        # workbook = openpyxl.load_workbook(file_path)
        # booksheet = workbook.active
        # for i in range(len(valid_names)):
        #     booksheet.cell(row=i+1, column=1, value=valid_names[i])
        #     booksheet.cell(row=i+1, column=2, value=invalid_names[i])
        # workbook.save(file_path)
        # print("文件已保存")

    except Exception as e:
        # print(e)
    # else:
        # 新建一个excle文件用于存放结果
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet = workbook.add_sheet('有效数据', cell_overwrite_ok=True)
        booksheet = workbook.add_sheet('无效数据', cell_overwrite_ok=True)


        #获取当前目录路径
        current_path = os.path.dirname(os.path.abspath(__file__))
        print(current_path)
        #要创建的文件夹名称
        folder_name = 'output'

        #要创建的文件夹完成路径
        folder_path = os.path.join(current_path,folder_name)

        #判断文件夹是否存在，不存在则创建
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # file_path 是寻找到的文件D:\project\py_project\filter_table\handle_excel\语音.xlsx
        # 带有后缀
        name = os.path.basename(file_path)
        # '语音.xlsx'
        # 不带后缀
        name_all = os.path.splitext(name)
        #  ('语音', '.xlsx')
        name_0 = name_all[0]
        # 生成新文件名,目录和文件名用'\\'隔开
        workbook.save(folder_path + '\\'+ name_0 + '.xlsx')
        print('原文件已经包含有效数据和无效数据，已生成新文件')
        #
        # with pd.ExcelWriter(file_path + ".xlsx", engine="openpyxl", mode='a') as writer:
        #     pd.DataFrame(valid_names, columns=["有效数据"]).to_excel(writer, sheet_name="有效数据", index=False)
        #     pd.DataFrame(invalid_names, columns=["无效数据"]).to_excel(writer, sheet_name="无效数据", index=False)
        #     print("文件已保存")