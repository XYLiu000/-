# coding=gbk
import os
import json

json_dir = 'train_dataset/train.json'  # json�ļ�·��
out_dir = 'data/label1/'  # ����� txt �ļ�·��


def main():
    # ��ȡ json �ļ�����
    with open(json_dir, 'r') as load_f:
        content = json.load(load_f)
    # ѭ������
    p=content["annotations"]
    for t in p:
        file_name = os.path.join(t['filename'].split('\\')[1])
        tmp = file_name.split('.')
        filename = out_dir + tmp[0] + '.txt'
        print(filename)

        if os.path.exists(filename):
            # ���� yolo ���ݸ�ʽ����Ҫ�����ĵ�� ��� x, y ����, w,h ��ֵ
            pos=t["box"]
            if pos["xmin"] !=None:
                x = (pos["xmin"] + pos["xmax"]) / 2 + pos["xmin"]
                y = (pos["ymin"] + pos["ymax"]) / 2 + pos["ymin"]
                w = pos["xmax"] - pos["xmin"]
                h = pos["ymax"] - pos["ymin"]
                fp = open(filename, mode="r+", encoding="utf-8")
                file_str = str(car_list[t['label']]) + ' ' + str(round(x, 6)) + ' ' + str(round(y, 6)) + ' ' + str(round(w, 6)) + \
                           ' ' + str(round(h, 6))
                line_data = fp.readlines()

                if len(line_data) != 0:
                    fp.write('\n' + file_str)
                else:
                    fp.write(file_str)
                fp.close()




        # �������򴴽��ļ�
        else:
            fp = open(filename, mode="w", encoding="utf-8")
            fp.close()


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