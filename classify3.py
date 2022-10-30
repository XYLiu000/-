# coding=gbk
# 本文件用于将eval_train_car 的内容写成表格
import pandas as pd
import os
import shutil  # 用于移动文件

def getfiles():
    filenames=os.listdir(r'car_data/images/val')
    print(filenames)
    for filename in filenames:

if __name__=='__main__':
    getfiles()
