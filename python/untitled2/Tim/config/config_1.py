#!/usr/bin/puthon
#_*_coding:utf_8  _*_
def  read_data():
    datas = []
    with open(r'C:\Users\hanwl\PycharmProjects\untitled2\Tim\data\data_1','r') as  a:
        b = a.readlines()
        for i in b:
            datas.append(i.replace('\n', '').split(','))
    return datas
print(read_data())