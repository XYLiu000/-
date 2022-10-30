# coding=gbk
import os, random, shutil
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
    filePath = "data/"  # 源图片文件夹路径

    train_fileDir = filePath + "train/"
    val_fileDir = filePath + "val/"

    for oneDir in os.listdir(filePath):
        onefileDir = filePath + oneDir + "/"
        onetarDir_train = train_fileDir + oneDir + "/"  # A的二级目录
        onetarDir_val = val_fileDir + oneDir + "/"  # B的二级目录
        print(onefileDir)
        print(onetarDir_train)
        print(onetarDir_val, end="\n\n")

        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists(onetarDir_train):
            os.makedirs(onetarDir_train)
        if not os.path.exists(onetarDir_val):
            os.makedirs(onetarDir_val)

        moveFile(onefileDir, onetarDir_train, onetarDir_val)

        # 删除原文件夹（这个时候文件夹应该是已经空了的）
        os.removedirs(onefileDir)
