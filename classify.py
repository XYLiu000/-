# coding=gbk
# ���ļ����ڽ�eval_train_car ������д�ɱ��
import pandas as pd
import os
import shutil  # �����ƶ��ļ�

fname = 'eval_train_car.txt'
# with open(fname, 'r+', encoding='utf-8') as f:
#     for line in f.readlines():
#         print(line[:-1].split(' '))
#     s = [i[:-1].split(' ') for i in f.readlines()]
with open(fname, 'r', encoding='utf-8') as f:
    dic = []
    for line in f.readlines():
        line = line.strip('\n')  # ȥ�����з�\n
        b = line.split(' ')  # ��ÿһ���Կո�Ϊ�ָ���ת�����б�
        dic.append(b)
dic = dict(dic)
print(dic)

key = list(dic.keys())
value = list(dic.values())

result_excel = pd.DataFrame()
result_excel["������"] = key
result_excel["��Ƶ"] = value

result_excel.to_csv("eval.csv")

# -------------------------------------------------------------
# �򿪱���ļ�����ȡ
f = open("eval.csv", "rb")  # ����������·��+����
list = pd.read_csv(f)
list["ID"]=list["�ʻ���"]

#���з���
for i in range(0,20):
    listnew=list[list["CATEGORY_ID"]==i]
    l=listnew["FILE_ID1"].tolist()
    j=str(i)
    for each in l:
        shutil.move(each,j)
