# coding=gbk
# 本文件用于将eval_train_car 的内容写成表格
import pandas as pd
import os
import shutil  # 用于移动文件

# fname = 'train_car.txt'
# # with open(fname, 'r+', encoding='utf-8') as f:
# #     for line in f.readlines():
# #         print(line[:-1].split(' '))
# #     s = [i[:-1].split(' ') for i in f.readlines()]
# with open(fname, 'r', encoding='utf-8') as f:
#     dic = []
#     for line in f.readlines():
#         line = line.strip('\n')  # 去掉换行符\n
#         b = line.split(' ')  # 将每一行以空格为分隔符转换成列表
#         dic.append(b)
# dic = dict(dic)
# print(dic)
#
# key = list(dic.keys())
# value = list(dic.values())
#
# result_excel = pd.DataFrame()
# result_excel["词向量"] = key
# result_excel["词频"] = value
#
# result_excel.to_csv("data1.csv")

# # -------------------------------------------------------------
# # 打开表格文件并读取
# f = open("data.csv", "rb")  # 输入表格所在路径+名称
# list = pd.read_csv(f)
# list["ID"]=list["词向量"]
# path = r'data/'
# # #创建文件夹
# # for i in range(22):
# #  os.mkdir(path+str(i))
# #进行分类
# for i in range(0,22):
#     listnew=list[list["词频"]==i]
#     l=listnew["ID"].tolist()
#     j=path+str(i)
#     for each in l:
#         shutil.move(each,j)
import pandas as pd

data = open(r'train_car.txt')
res = []
for i in data:
    d = [x for x in i.strip().split(' ')]
    res.append(d)
save = pd.DataFrame(columns=['城市代码','城市名称'], index = None, data=list(res)) #columns列名，index索引名，data数据
# print(save)
fh = open(r'data3.csv','w+',newline='')
save.to_csv(fh)
fh.close()
