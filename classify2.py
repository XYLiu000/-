# coding=gbk
import os, random, shutil
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
    filePath = "data/"  # ԴͼƬ�ļ���·��

    train_fileDir = filePath + "train/"
    val_fileDir = filePath + "val/"

    for oneDir in os.listdir(filePath):
        onefileDir = filePath + oneDir + "/"
        onetarDir_train = train_fileDir + oneDir + "/"  # A�Ķ���Ŀ¼
        onetarDir_val = val_fileDir + oneDir + "/"  # B�Ķ���Ŀ¼
        print(onefileDir)
        print(onetarDir_train)
        print(onetarDir_val, end="\n\n")

        # �ж��ļ����Ƿ���ڣ��������򴴽�
        if not os.path.exists(onetarDir_train):
            os.makedirs(onetarDir_train)
        if not os.path.exists(onetarDir_val):
            os.makedirs(onetarDir_val)

        moveFile(onefileDir, onetarDir_train, onetarDir_val)

        # ɾ��ԭ�ļ��У����ʱ���ļ���Ӧ�����Ѿ����˵ģ�
        os.removedirs(onefileDir)
