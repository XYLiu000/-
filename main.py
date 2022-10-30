# coding=gbk
import numpy as np
import pandas as pd
import os
from matplotlib import pyplot as plt
import json

from sklearn import neighbors
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import SMOTE, ADASYN

import os, random, shutil


def main():
    base_path = "train_dataset/"
    filelist = os.listdir(base_path)  # filelist��json�ļ��������json�ļ�����������չ����
    # os.listdir() �������ڷ���ָ�����ļ��а������ļ����ļ��е����ֵ��б�����б�����ĸ˳�� �������� ��.�� �͡�������ʹ�����ļ����С�
    filelist.sort()
    print(len(filelist))  # ���json�ļ�����Ŀ

    # i_count, j_count, k_count = 0, 0, 0
    b = []  # ���label���б�
    for name in filelist:
        # os.path.splitext(���ļ�·����) �����ļ�������չ����Ĭ�Ϸ���(fname,fextension)Ԫ�飬������Ƭ����
        filename = os.path.splitext(name)[0]
        filename_suffix = os.path.splitext(name)[1]
        # �ж��Ƿ�Ϊ.json�ļ�
        if filename_suffix == ".json":
            fullname = base_path + filename + filename_suffix
            dataJson = json.load(open("{}".format(fullname), encoding='UTF-8'))
            label_name = dataJson["annotations"]
            for _ in label_name:
                b.append(_["label"])  # ����ǩֵ�Ž��б�����
            f_car = open('train_car.txt', 'w')
            for item in dataJson["annotations"]:
                label = car_list[item['label']]
                file_name = os.path.join(item['filename'].split('\\')[1])
                f_car.write(file_name + ' ' + str(label) + '\n')
            f_car.close()
            print("д��train_car.txt��ɣ�����")
            ##����ÿ��label������
            # i, j, k = 0, 0, 0
            #     i = i + 1 if _["label"] == "crack" else i
            #     j = j + 1 if _["label"] == "breakage" else j
            #     k = k + 1 if _["label"] == "corrosion" else k

            # i_count = i_count + i
            # j_count = j_count + j
            # k_count = k_count + k

        else:
            pass

    # print("crack, breakage, corrosion = " + str(i_count) + ', ' + str(j_count) + ', ' + str(k_count))

    print(len(b))  # ���ȥ��ǰ�ı�ǩ��Ŀ
    f = set(b)  ##���б�aǿ������ת���ɼ���,������f���ȥ��
    print(len(f))  # ���ȥ�غ�ı�ǩ��Ŀ
    print(f)


# ���ݼ����ֲ����ݾ���
def dataprint():
    data = pd.read_csv('train_car.txt', header=None, sep=' ')
    print(data[1].value_counts())
    data[1].value_counts().plot(kind="bar")
    plt.show()


# ѵ���������Լ�����
def split_dataset(data_file):
    # չʾ��ͬ�ĵ��÷�ʽ
    data = pd.read_csv(data_file, header=None, sep=' ')
    train_dataset, eval_dataset = train_test_split(data, test_size=0.2, random_state=42)
    print(f'train dataset len: {train_dataset.size}')
    print(f'eval dataset len: {eval_dataset.size}')
    train_filename = 'train_' + data_file.split('.')[0] + '.txt'
    eval_filename = 'eval_' + data_file.split('.')[0] + '.txt'
    train_dataset.to_csv(train_filename, index=None, header=None, sep=' ')
    eval_dataset.to_csv(eval_filename, index=None, header=None, sep=' ')


# ���ݾ���
def data_balance(filename):
    print(50 * '*')
    data = pd.read_csv(filename, header=None, sep=' ')
    print(data[1].value_counts())
    # �鿴������ǩ��������
    print(Counter(data[1]))
    print(50 * '*')
    # ���ݾ���

    X, y = make_classification(n_classes=2, class_sep=2,
                               weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0,
                               n_features=20, n_clusters_per_class=1, n_samples=1000,
                               random_state=10)
    print('Original dataset shape %s' % Counter(y))
    print(50 * '*')
    ada = ADASYN(random_state=42)
    X_res, y_res = ada.fit_resample(X, y)
    print('Resampled dataset shape %s' % Counter(y_res))


def moveFile(fileDir, tarDir_train, tarDir_val):
    pathDir = os.listdir(fileDir)  # ȡͼƬ��ԭʼ·��
    filenumber = len(pathDir)

    rate = 0.2  # �Զ����ȡͼƬ�ı������ȷ�˵100�ų�10�ţ��Ǿ���0.1
    picknumber = int(filenumber * rate)  # ����rate�������ļ�����ȡһ������ͼƬ
    sample_val = random.sample(pathDir, picknumber)  # ���ѡȡpicknumber����������ͼƬ

    for name in sample_val:
        shutil.move(fileDir + name, tarDir_val + name)
    for name in os.listdir(fileDir):
        shutil.move(fileDir + name, tarDir_train + name)


if __name__ == '__main__':
    car_list = (
        {'Bike': 0, 'MMcar': 1, 'Pickup': 2, 'OtherCar': 3,
         'BiCyclist': 4, 'Pedestrian': 5, 'TricycleOpenMotor': 6,
         'TricycleOpenHuman': 7, 'EngineTruck': 8, 'MediumBus': 9,
         'Motorcycle': 10, 'LightTruck': 11,
         'PersonSitting': 12, 'MotorCyclist': 13,
         'LargeBus': 14, 'HeavyTruck': 15, 'Truck': 16, 'TricycleClosed': 17,
         'CampusBus': 18, 'Machineshop': 19, 'Car': 20, 'van': 21}
    )

    main()
    dataprint()
    data_file = "train_car.txt"
    split_dataset(data_file)
    filename = 'train_train_car.txt'
    data_balance(filename)
    filename = 'eval_train_car.txt'
    data_balance(filename)
    # --------------------------------------------------------------------

