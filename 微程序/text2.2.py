MonStr = input("请输入带符号的货币值：")
if MonStr[-1] in ['Y','y']:
    D = eval(MonStr[0:-1])/6
    print("转换后的钱是{:.2f}D".format(D))
elif MonStr[-1] in ["D","d"]:
    R = eval(MonStr[0:-1]) * 6
    print("转换后的钱是{:.2f}Y".format(R))
else:
    print("输入格式错误！")
