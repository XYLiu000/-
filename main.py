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
    filelist = os.listdir(base_path)  # filelist是json文件夹下面的json文件名（包括扩展名）
    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 ‘.’ 和’…’即使它在文件夹中。
    filelist.sort()
    print(len(filelist))  # 输出json文件的数目

    # i_count, j_count, k_count = 0, 0, 0
    b = []  # 存放label的列表
    for name in filelist:
        # os.path.splitext(“文件路径”) 分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作
        filename = os.path.splitext(name)[0]
        filename_suffix = os.path.splitext(name)[1]
        # 判断是否为.json文件
        if filename_suffix == ".json":
            fullname = base_path + filename + filename_suffix
            dataJson = json.load(open("{}".format(fullname), encoding='UTF-8'))
            label_name = dataJson["annotations"]
            for _ in label_name:
                b.append(_["label"])  # 将标签值放进列表里面
            f_car = open('train_car.txt', 'w')
            for item in dataJson["annotations"]:
                label = car_list[item['label']]
                file_name = os.path.join(item['filename'].split('\\')[1])
                f_car.write(file_name + ' ' + str(label) + '\n')
            f_car.close()
            print("写入train_car.txt完成！！！")
            ##计算每个label的数量
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

    print(len(b))  # 输出去重前的标签数目
    f = set(b)  ##把列表a强制类型转换成集合,并赋给f完成去重
    print(len(f))  # 输出去重后的标签数目
    print(f)


# 数据集划分并数据均衡
def dataprint():
    data = pd.read_csv('train_car.txt', header=None, sep=' ')
    print(data[1].value_counts())
    data[1].value_counts().plot(kind="bar")
    plt.show()


# 训练集、测试集划分
def split_dataset(data_file):
    # 展示不同的调用方式
    data = pd.read_csv(data_file, header=None, sep=' ')
    train_dataset, eval_dataset = train_test_split(data, test_size=0.2, random_state=42)
    print(f'train dataset len: {train_dataset.size}')
    print(f'eval dataset len: {eval_dataset.size}')
    train_filename = 'train_' + data_file.split('.')[0] + '.txt'
    eval_filename = 'eval_' + data_file.split('.')[0] + '.txt'
    train_dataset.to_csv(train_filename, index=None, header=None, sep=' ')
    eval_dataset.to_csv(eval_filename, index=None, header=None, sep=' ')


# 数据均衡
def data_balance(filename):
    print(50 * '*')
    data = pd.read_csv(filename, header=None, sep=' ')
    print(data[1].value_counts())
    # 查看各个标签的样本量
    print(Counter(data[1]))
    print(50 * '*')
    # 数据均衡

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
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)

    rate = 0.2  # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample_val = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片

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

