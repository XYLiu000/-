# coding=gbk
####��ͼ���ļ����������ȡһ��������ͼ�񣬲�����ͼ�����֣���ȡ��Ӧ��txt��ǩ
import os
import random
import shutil


def moveFile(Imgdir):
    pathDir = os.listdir(Imgdir)  # ��ȡͼ���б�
    filenumber = len(pathDir)
    rate = 0.1  # �����ȡͼƬ�ı���
    random_imgnum = int(filenumber * rate)  # ���ձ������ļ�����ȡһ������ͼƬ
    sample = random.sample(pathDir, random_imgnum)  # ���ѡȡrandom_imgnum����������ͼƬ
    print(sample)
    for imgname in sample:
        # name0 = os.path.join(outdir1,os.path.basename(name))
        nametxt = os.path.splitext(imgname)[0]
        shutil.move(Imgdir + imgname, img_target_dir + imgname)
        shutil.move(Txtdir + nametxt + '.txt', Txt_target_dir + nametxt + '.txt')
    return


if __name__ == '__main__':
    Imgdir = "yolov5/data/VOCdevkit/JPEGImages/"  # ͼ���ļ���
    img_target_dir = "yolov5/data/VOCdevkit/pictures/"  # ����Ŀ��ͼ���ļ���
    Txtdir = "yolov5/data/VOCdevkit/YOLO/"  # ��ǩ�ļ���
    Txt_target_dir = "yolov5/data/VOCdevkit/labels/"  # ����Ŀ���ǩ�ļ���
    moveFile(Imgdir)
