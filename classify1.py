# coding=gbk
# ���ļ����ڽ�eval_train_car ������д�ɱ��
import pandas as pd
import os
import shutil  # �����ƶ��ļ�

# fname = 'train_car.txt'
# # with open(fname, 'r+', encoding='utf-8') as f:
# #     for line in f.readlines():
# #         print(line[:-1].split(' '))
# #     s = [i[:-1].split(' ') for i in f.readlines()]
# with open(fname, 'r', encoding='utf-8') as f:
#     dic = []
#     for line in f.readlines():
#         line = line.strip('\n')  # ȥ�����з�\n
#         b = line.split(' ')  # ��ÿһ���Կո�Ϊ�ָ���ת�����б�
#         dic.append(b)
# dic = dict(dic)
# print(dic)
#
# key = list(dic.keys())
# value = list(dic.values())
#
# result_excel = pd.DataFrame()
# result_excel["������"] = key
# result_excel["��Ƶ"] = value
#
# result_excel.to_csv("data1.csv")

# # -------------------------------------------------------------
# # �򿪱���ļ�����ȡ
# f = open("data.csv", "rb")  # ����������·��+����
# list = pd.read_csv(f)
# list["ID"]=list["������"]
# path = r'data/'
# # #�����ļ���
# # for i in range(22):
# #  os.mkdir(path+str(i))
# #���з���
# for i in range(0,22):
#     listnew=list[list["��Ƶ"]==i]
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
save = pd.DataFrame(columns=['���д���','��������'], index = None, data=list(res)) #columns������index��������data����
# print(save)
fh = open(r'data3.csv','w+',newline='')
save.to_csv(fh)
fh.close()
