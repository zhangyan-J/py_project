print("hello world")
polling_active = True
while polling_active:
    num_1 = int(input("请输入一个数字："))
    if num_1 == 'q':
        break
    num_2 = int(input("请输入第二个数字："))
    if num_2 == "q":
        break
    n_sum = num_1+num_2
    print(n_sum)
    repeat = input("还想继续输入吗?(yes/no)")
    if repeat == "no":
        break