import pandas


def compare_excel(file1, file2):
    # 读取两个Excel文件
    df1 = pandas.read_excel(file1)
    df2 = pandas.read_excel(file2)

    # 比较两个Excel文件中的数据
    diff = pandas.concat([df1, df2]).drop_duplicates(keep=False)

    # 输出结果
    if diff.empty:
        print("两个Excel文件中的数据完全相同")
    else:
        print("两个Excel文件中的数据有差异：")
        # print(type(diff))
        # print("差异数量：", len(diff))
        #测试结果均为fail的行
        diff_both = diff[(diff['测试结果'] == 'fail') & (diff['测试结果'] == 'fail')]

        #file1测试结果fail的
        # diff_1 = diff[diff['测试结果'] == 'fail']

        #file2测试结果fail的
        # diff_2 = diff[diff['测试结果'] == 'fail']

        #将结果保存到新的Excel文件中
        diff_both.to_excel("D:\practice\github\py_project\excel_related\compare_excel\compare_result.xlsx", index=False)
        # diff_1.to_excel("D:\practice\github\py_project\excel_related\compare_excel\compare_result_1.xlsx", index=False)
        # diff_2.to_excel("D:\practice\github\py_project\excel_related\compare_excel\compare_result_2.xlsx", index=False)


# 示例用法
compare_excel(
    "D:\practice\github\py_project\excel_related\compare_excel\SS2.0_6.2.0_内测3-1_X03Pro_理想同学冒烟测试_0D11_RC3_0806_2024-08-06-19-29-18.xlsx",
    "D:\practice\github\py_project\excel_related\compare_excel\SS3_6.2.0_内测3-1_W01Ultra&X01B_Ultra_0C20_BR10_RC3_理想同学冒烟测试_0806_2024-08-06-19-30-05.xlsx")
