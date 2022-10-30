# coding=gbk
####从图像文件夹中随机抽取一定比例的图像，并根据图像名字，抽取对应的txt标签
import os
import random
import shutil


def moveFile(Imgdir):
    pathDir = os.listdir(Imgdir)  # 获取图像列表
    filenumber = len(pathDir)
    rate = 0.1  # 定义抽取图片的比例
    random_imgnum = int(filenumber * rate)  # 按照比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, random_imgnum)  # 随机选取random_imgnum数量的样本图片
    print(sample)
    for imgname in sample:
        # name0 = os.path.join(outdir1,os.path.basename(name))
        nametxt = os.path.splitext(imgname)[0]
        shutil.move(Imgdir + imgname, img_target_dir + imgname)
        shutil.move(Txtdir + nametxt + '.txt', Txt_target_dir + nametxt + '.txt')
    return


if __name__ == '__main__':
    Imgdir = "yolov5/data/VOCdevkit/JPEGImages/"  # 图像文件夹
    img_target_dir = "yolov5/data/VOCdevkit/pictures/"  # 划分目标图像文件夹
    Txtdir = "yolov5/data/VOCdevkit/YOLO/"  # 标签文件夹
    Txt_target_dir = "yolov5/data/VOCdevkit/labels/"  # 划分目标标签文件夹
    moveFile(Imgdir)
